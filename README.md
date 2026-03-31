# 🔐 Port Scanner

A command-line based port scanner built in Python to identify open ports on a target system using TCP connections.

---

## 📌 Overview

This tool performs a TCP connect scan on a specified target (IP address or domain) and reports open ports within a given range. It is designed to be lightweight, fast, and dependency-free, making it suitable for basic network reconnaissance and learning purposes.

---

## ⚙️ Features

* TCP port scanning using socket connections
* Custom port range support
* Command-line interface (CLI) arguments
* Fast and efficient scanning
* No external libraries required

---

## 🛠️ Tech Stack

* Python 3
* Built-in `socket` module
* Built-in `argparse` module

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/aadithynn/port_scanner.git
cd port_scanner
```

---

## ▶️ Usage

Run the scanner using:

```bash
python port_scanner.py -t <target> -s <start_port> -e <end_port>
```

---

## 💡 Example

```bash
python port_scanner.py -t scanme.nmap.org -s 1 -e 1000
```

Example output:

```
[+] Port 22 is OPEN
[+] Port 80 is OPEN
```

---

## 📂 Project Structure

```
port_scanner/
│── port_scanner.py
│── README.md
│── .gitignore
```

---

## ⚠️ Disclaimer

This tool is intended for educational and authorized testing purposes only.
Do not use it on systems without proper permission.

---

## 📈 Future Improvements

* Multithreaded scanning for better performance
* Service/banner detection
* Output export (JSON or CSV)
* Improved error handling and logging

---

## 👤 Author

Adithyan V
Cybersecurity Enthusiast | Python Developer

---
