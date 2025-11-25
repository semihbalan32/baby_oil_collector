
#!/usr/bin/env python3
import argparse
import json
from baby_oil_collector import get_system_info

def main():
    parser = argparse.ArgumentParser(
        description="Baby Oil Collector: Open-source hardware inventory tool.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  $ python baby_oil_collector_cli.py
  $ python baby_oil_collector_cli.py --json
  $ python baby_oil_collector_cli.py --output inventory.json
  $ python baby_oil_collector_cli.py --verbose
"""
    )

    parser.add_argument(
        "--json", action="store_true", help="Output in JSON format (default: pretty-print)"
    )
    parser.add_argument(
        "--output", metavar="FILE", help="Save output to a file (e.g., inventory.json)"
    )
    parser.add_argument(
        "--verbose", action="store_true", help="Show detailed information"
    )
    parser.add_argument(
        "--version", action="version", version="Baby Oil Collector v1.0"
    )

    args = parser.parse_args()

    # Get system info
    info = get_system_info()

    # Output based on flags
    if args.output:
        try:
            with open(args.output, "w") as f:
                json.dump(info, f, indent=2)
            print(f"✅ System info saved to {args.output}")
        except Exception as e:
            print(f"❌ Failed to save to {args.output}: {e}")
            return

    # Print to stdout
    if args.json:
        print(json.dumps(info, indent=2))
    elif args.verbose:
        # Pretty-print with sections
        print("📦 System Inventory")
        print("-" * 50)
        print(f"OS: {info['os']}")
        print(f"Hostname: {info['hostname']}")
        print()

        # CPU
        print("🧠 CPU")
        print(f"  Logical Cores: {info['cpu']['count']}")
        print(f"  Physical Cores: {info['cpu']['physical_count']}")
        if info['cpu']['frequency_mhz']['current']:
            print(f"  Current Frequency: {info['cpu']['frequency_mhz']['current']} MHz")
        print()

        # Memory
        print("💾 Memory")
        mem = info['memory']
        print(f"  Total: {mem['total'] / (1024**3):.1f} GB")
        print(f"  Used: {mem['used'] / (1024**3):.1f} GB")
        print(f"  Available: {mem['available'] / (1024**3):.1f} GB")
        print(f"  Usage: {mem['percent']}%")
        print()

        # Network
        print("🌐 Network Interfaces")
        for iface, addrs in info['network'].items():
            print(f"  {iface}:")
            for addr in addrs:
                if isinstance(addr, dict):  # Skip error entries
                    print(f"    {addr.get('family', 'N/A')}: {addr.get('address', 'N/A')}")
            print()
    else:
        print("📦 System Inventory (use --json or --verbose for more details)")
        print(f"OS: {info['os']}")
        print(f"Hostname: {info['hostname']}")
        print(f"CPU Cores: {info['cpu']['count']} (logical)")
        print(f"Memory Used: {info['memory']['percent']}%")
        print(f"Network Interfaces: {len(info['network'])} found")

if __name__ == "__main__":
    main()
