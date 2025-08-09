# ESP8266 Wi-Fi Packet Sniffer for Network Vulnerability Analysis

## 📌 Overview
This project implements a **Wi-Fi packet sniffer** using the **ESP8266** microcontroller to capture and analyze wireless network traffic.  
It demonstrates core concepts in **network security**, **device monitoring**, and **traffic analysis** — skills essential for cybersecurity and risk advisory roles.

The system captures packets from nearby devices in monitor mode, extracts key information (MAC address, RSSI, uptime), and transmits the data via **UDP** to a Python-based collector for further analysis.  

---

## 🚀 Features
- 📡 **Packet Sniffing in Monitor Mode** – Captures packets from all nearby devices without connecting to them.
- 📶 **Signal Strength (RSSI) Monitoring** – Measures the received signal power for each detected device.
- ⏱ **Device Uptime Tracking** – Estimates how long a device has been active on the network.
- 📤 **UDP Transmission** – Sends real-time data to a Python receiver for storage/visualization.
- 🔍 **Potential for Network Security Auditing** – Helps identify unauthorized devices or unusual network patterns.

---

## 🛠️ Tech Stack
- **Hardware:** ESP8266 Wi-Fi module
- **Firmware:** Arduino IDE (C/C++)
- **Backend Receiver:** Python 3 (UDP Sockets)
- **Analysis Tools:** Wireshark (for packet verification), Excel (for reports)


---

## ⚙️ How It Works
1. ESP8266 in Monitor Mode** – Listens for Wi-Fi packets in the air.
2. Packet Filtering** – Extracts device MAC address, RSSI, and uptime.
3. UDP Transmission** – Sends data to a laptop/PC running the Python receiver.
4. Data Analysis** – View logs in CSV format or analyze in Wireshark/Excel.

---

## 🔐 Cybersecurity Relevance
- Can be used in **network audits** to identify unknown or rogue devices.
- Supports **signal analysis** for physical network mapping.
- Introduces concepts in **intrusion detection** and **network monitoring**.
- Useful for **privacy awareness** by demonstrating how easily metadata can be captured from open Wi-Fi signals.

---

## 📜 Future Enhancements
- Integration with **GRC tools** for risk assessment reporting.
- **Visualization dashboard** in Power BI or Grafana.
- Packet type classification for deeper traffic profiling.

---

## 📄 License
This project is open-source under the MIT License — free to use and modify for educational and security research purposes.

---

## 👤 Author
**Partha Dey**  
[GitHub Profile](https://github.com/Partha-Dey001)  

