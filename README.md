# 🔍 Network Scanner Pro v2

> **Author:** @k4lashhnikov | **Security & Ethical Hacking**

## 📜 Description

**Network Scanner Pro v2** is a powerful and user-friendly Python tool designed for scanning local networks using ARP requests. It allows ethical hackers, penetration testers, and network administrators to discover live hosts on a local subnet efficiently. The tool features a colorful and simple command-line interface, making it perfect for those who need quick network reconnaissance without overwhelming complexity.

---

## 🚀 Features

- 📡 **Scan network** using ARP requests.
- 🎨 **Colorful and clear terminal output** for easy identification of hosts.
- 🛡️ **Detect IP and MAC addresses** of live devices in the network.
- 💨 **Fast and efficient** network scanning.
- 🔄 Graceful error handling and keyboard interrupt support.

---

## 🧩 Requirements

- **Python 3.6+** (Python 3.9 recommended)
- **Kali Linux** or any Debian-based distro
- Required Python modules:
  - `scapy`
  - `colorama`

### 🧾 Install dependencies

```bash
pip3 install -r requirements.txt

Create a requirements.txt file with the following:

scapy
colorama

⚙️ Installation

    Clone the repository:

git clone https://github.com/k4lashhnikov/Network-Scanner-Pro-v2.git

    Navigate to the project directory:

cd Network-Scanner-Pro-v2

🖥 Usage
Scan the entire subnet:

sudo python3 nwscanner2.py -i 192.168.1.0/24

Scan a single IP address:

sudo python3 nwscanner2.py -i 192.168.1.5

🛑 Keyboard Interrupt

You can stop the scan anytime with Ctrl + C — the tool will exit gracefully.
📸 Sample Output

📡 Scanning Network...

IP Address              MAC Address
-----------------------------------------
192.168.1.1             aa:bb:cc:dd:ee:ff
192.168.1.5             11:22:33:44:55:66
...

⚠️ Legal & Ethical Use

Important: This tool is only for authorized use. Unauthorized network scanning without explicit permission is illegal and unethical.

    Always ensure you have permission to scan the network before using this tool.

📞 Contact

    GitHub: @k4lashhnikov

    LinkedIn: @k4lashhnikov

    E-mail: fiftharmando@gmail.com
