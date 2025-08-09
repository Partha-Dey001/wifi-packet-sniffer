#include <ESP8266WiFi.h>
#include <WiFiUdp.h>

// WiFi Credentials
const char* ssid = "DESKTOP-LHC063N 9595";
const char* password = "6$84kB95";

// Laptop IP (check via `ipconfig` on your laptop, likely 192.168.4.100)
IPAddress laptopIP(192, 168, 137, 1);
const int udpPort = 1234;

WiFiUDP udp;

void setup() {
  Serial.begin(115200);
  delay(1000);

  Serial.println("[TEST] Connecting to WiFi...");
  WiFi.begin(ssid, password);

  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(500);
    Serial.print(".");
    attempts++;
  }

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("\n[TEST] Failed to connect to WiFi.");
    return;
  }

  Serial.println("\n[TEST] Connected!");
  Serial.print("ESP IP: ");
  Serial.println(WiFi.localIP());

  delay(1000);
  sendTestPacket();
}

void loop() {
  // Nothing here
}

void sendTestPacket() {
  String testData = "Hello from ESP8266!";

  Serial.println("[TEST] Sending test message...");
  udp.beginPacket(laptopIP, udpPort);
  udp.write(testData.c_str());
  udp.endPacket();
  Serial.println("[TEST] Packet sent.");
}
