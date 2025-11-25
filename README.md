# baby_oil_collector
System Information Collector

🛠️ Requirements
Install the required dependencies:


Copy
bash
pip install psutil


📦 Usage Example

Copy
python
from baby_oil_collector import get_system_info

info = get_system_info()
print(info)

This will return a structured dictionary like:

{
  "os": "Windows-10-10.0.19045-SP0",
  "hostname": "DESKTOP-ABC123",
  "cpu": {
    "count": 8,
    "physical_count": 4,
    "frequency_mhz": {
      "current": 3800.0,
      "min": 800.0,
      "max": 4200.0
    },
    ...
  },
  "memory": {
    "total": 17179869184,
    "available": 8000000000,
    ...
  },
  "network": {
    "Ethernet": [
      {
        "family": "AF_INET",
        "address": "192.168.1.100",
        "netmask": "255.255.255.0",
        ...
      }
    ],
    ...

🛠️ How to Use
Save the file as baby_oil_collector_cli.py in the same directory as baby_oil_collector.py.

Make it executable (Linux/macOS):


Copy
bash
chmod +x baby_oil_collector_cli.py
Run it:


Copy
bash
python baby_oil_collector_cli.py

🔧 CLI Examples
Command	Description
python baby_oil_collector_cli.py	Show summary in terminal
python baby_oil_collector_cli.py --json	Output as JSON
python baby_oil_collector_cli.py --verbose	Detailed output with all fields
python baby_oil_collector_cli.py --output inventory.json	Save to file
python baby_oil_collector_cli.py --version	Show version
    
  }
}
