import socket
import csv
import os
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt

PORT = 1234
BUFFER_SIZE = 4096
CSV_FILE = "wifi_data.csv"
DEVICE_TIMEOUT = 60  # in seconds

device_last_seen = {}
rssi_values = []

def save_to_csv(timestamp, data_line):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, mode='a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Timestamp', 'Millisecond', 'Packet Length', 'Channel', 'RSSI'])
        writer.writerow([timestamp] + data_line.split(','))

def parse_packet(line):
    parts = line.split(',')
    if len(parts) == 4:
        return parts
    return None

def update_device_seen(identifier):
    device_last_seen[identifier] = datetime.now()

def analyze_devices():
    now = datetime.now()
    missing_devices = []
    for dev, last_seen in device_last_seen.items():
        delta = (now - last_seen).total_seconds()
        if delta > DEVICE_TIMEOUT:
            missing_devices.append(dev)
    return missing_devices

def plot_rssi():
    if not rssi_values:
        print("No RSSI data to plot.")
        return
    plt.plot(rssi_values)
    plt.title("RSSI over time")
    plt.xlabel("Sample Index")
    plt.ylabel("RSSI (dBm)")
    plt.grid(True)
    plt.show()

def sniffer_mode():
    print("Starting Sniffer Mode...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("0.0.0.0", PORT))
    print(f"Listening for UDP packets on port {PORT}...")

    try:
        while True:
            data, addr = sock.recvfrom(BUFFER_SIZE)
            decoded = data.decode(errors="ignore").strip()
            timestamp = datetime.now().isoformat()
            for line in decoded.splitlines():
                parts = parse_packet(line)
                if parts:
                    print(f"[{timestamp}] From {addr}: {parts}")
                    save_to_csv(timestamp, line)
                    update_device_seen(addr[0])
                    rssi_values.append(int(parts[3]))
    except KeyboardInterrupt:
        print("\nSniffer mode stopped.")
        sock.close()

def analysis_mode():
    print("Running Analysis Mode...")
    missing = analyze_devices()
    if missing:
        print("Missing Devices (not seen in last 60s):")
        for dev in missing:
            print(f" - {dev}")
    else:
        print("No missing devices.")

    if rssi_values:
        print(f"Average RSSI: {sum(rssi_values) / len(rssi_values):.2f} dBm")
    else:
        print("No RSSI data collected yet.")

def visualization_mode():
    print("Launching Visualization...")
    plot_rssi()

def menu():
    while True:
        print("\n=== WiFi Packet Listener Modes ===")
        print("1. Sniffer Mode (listen and save)")
        print("2. Analysis Mode (device status, average RSSI)")
        print("3. Visualization Mode (RSSI chart)")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            sniffer_mode()
        elif choice == '2':
            analysis_mode()
        elif choice == '3':
            visualization_mode()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()
