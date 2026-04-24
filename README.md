# Port Status Monitoring Tool

**Name:** Muaz Iqubal  
**SRN:** PES2UG24AM091  

---

## Overview

This project is a Python-based real-time port monitoring tool that checks the availability of network services running on a system. It continuously monitors specified ports and displays their status (UP/DOWN) along with uptime tracking and alerts.

---

## Topology
    +---------------------+
    |   Monitoring Tool   |
    |   (port_monitor.py) |
    +----------+----------+
               |
    -------------------------
    |        |        |     |
 SSH(22)  HTTP(80) HTTPS(443) MySQL(3306)
    |        |        |     |


---

## Topology Explanation

The system follows a **client-server model** where the monitoring tool acts as a client that continuously checks the availability of services running on a host machine.

The tool sends TCP connection requests to specific ports (such as 22, 80, 443, 3306). If the target system accepts the connection, the service is considered active (UP); otherwise, it is marked as DOWN.

---

## Detailed Description

This project is a real-time port monitoring system developed using Python. It is designed to continuously check the availability of network services by attempting TCP connections to predefined ports.

The tool operates by creating a socket and sending connection requests to target ports on a host system. If the connection is successfully established, the port is marked as **UP**, indicating that the service is running and accessible. If the connection fails due to timeout or refusal, the port is marked as **DOWN**.

The system runs in a continuous loop, updating the status of each monitored port at regular intervals. It also maintains an uptime counter for each service, allowing users to track how long a service has been active.

Additionally, the tool detects changes in port status and logs these events with timestamps, making it useful for monitoring service reliability and diagnosing network issues.

The project currently monitors services on the local machine (localhost), but it can be easily extended to monitor remote systems by changing the target IP address.

---

## Features

- Real-time port monitoring  
- TCP socket-based checking  
- Uptime tracking  
- Alerts for status changes  
- Logging of port activity  

---

## Technologies Used

- Python  
- Socket Programming  

---

## How It Works

The tool attempts to establish a TCP connection to specific ports.  
- If the connection succeeds → Port is **UP**  
- If the connection fails → Port is **DOWN**

---

## Example Ports Monitored

- SSH (Port 22)  
- HTTP (Port 80)  
- HTTPS (Port 443)  
- MySQL (Port 3306)  

---

## How to Run

```bash
python3 port_monitor.py

---

## Topology Explanation

The system follows a **client-server model** where the monitoring tool acts as a client that continuously checks the availability of services running on a host machine.

The tool sends TCP connection requests to specific ports (such as 22, 80, 443, 3306). If the target system accepts the connection, the service is considered active (UP); otherwise, it is marked as DOWN.

---

## Detailed Description

This project is a real-time port monitoring system developed using Python. It is designed to continuously check the availability of network services by attempting TCP connections to predefined ports.

The tool operates by creating a socket and sending connection requests to target ports on a host system. If the connection is successfully established, the port is marked as **UP**, indicating that the service is running and accessible. If the connection fails due to timeout or refusal, the port is marked as **DOWN**.

The system runs in a continuous loop, updating the status of each monitored port at regular intervals. It also maintains an uptime counter for each service, allowing users to track how long a service has been active.

Additionally, the tool detects changes in port status and logs these events with timestamps, making it useful for monitoring service reliability and diagnosing network issues.

The project currently monitors services on the local machine (localhost), but it can be easily extended to monitor remote systems by changing the target IP address.

---

## Features

- Real-time port monitoring  
- TCP socket-based checking  
- Uptime tracking  
- Alerts for status changes  
- Logging of port activity  

---

## Technologies Used

- Python  
- Socket Programming  

---

## How It Works

The tool attempts to establish a TCP connection to specific ports.  
- If the connection succeeds → Port is **UP**  
- If the connection fails → Port is **DOWN**

---

## Example Ports Monitored

- SSH (Port 22)  
- HTTP (Port 80)  
- HTTPS (Port 443)  
- MySQL (Port 3306)  

---

## How to Run

```bash
python3 port_monitor.py
