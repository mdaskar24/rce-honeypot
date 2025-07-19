# 🕵️‍♂️ Real-Time RCE Honeypot

A Python-based real-time honeypot that simulates a vulnerable command-line environment and detects Remote Code Execution (RCE) attempts. Automatically logs the intruder’s actions and captures a webcam snapshot to identify the attacker.

## 🎯 Project Purpose

This honeypot is designed to raise awareness about remote command execution attacks. It's ideal for:
- Educational demos
- Security testing labs
- Showcasing logging and detection techniques

## 🔐 Features

✅ Simulated CLI commands (`ls`, `uname`, `cat`)  
✅ Snapshot capture using webcam on suspicious input  
✅ Logs attacker commands with timestamp to a local database  
✅ Flask-based admin dashboard for viewing logs  
✅ Modular Python code with separate components

## 🗂️ Project Structure

rce-honeypot/
├── app/
│ ├── init.py
│ ├── logger.py # Logs intruder activity to SQLite DB
│ ├── server.py # Simulated command server
│ └── webcam.py # Captures snapshots
├── templates/
│ ├── index.html # Fake login page
│ ├── login.html # Admin login
│ └── dashboard.html # Log viewer
├── static/ # (Optional static assets like CSS/images)
├── client.py # Simulated client (attacker interface)
├── web_interface.py # Flask web interface
├── database/ # Contains the SQLite DB file
├── requirements.txt # Python dependencies
├── README.md # Project info
└── .gitignore # Ignore DB and snapshots

bash
Copy
Edit

## ⚙️ Installation

1. **Clone the repo:**
```bash
git clone https://github.com/mdaskar24/rce-honeypot.git
cd rce-honeypot
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
🚀 Usage
1. Start the honeypot server
bash
Copy
Edit
python app/server.py
2. Run the attacker simulation
bash
Copy
Edit
python client.py
3. Start the admin dashboard (in new terminal)
bash
Copy
Edit
python web_interface.py
Go to http://localhost:5000

Login with username: admin, password: admin

View logs and webcam snapshots

🧠 Educational Use Only
⚠️ This project is for educational and demonstration purposes only. Do not use it for malicious purposes.

📸 Sample Log
Timestamp	Command Entered	Snapshot File
2025-07-19 20:12:34	uname -a	20250719_201234.jpg
2025-07-19 20:13:01	ls	20250719_201301.jpg

🧰 Requirements
Python 3.x

Flask

OpenCV (cv2)

SQLite3 (auto-used)

🤝 Contribution
Pull requests and suggestions welcome!

🛡️ License
MIT License

Made with ❤️ by Askar for cybersecurity awareness.