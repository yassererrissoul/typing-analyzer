⚠️ IMPORTANT NOTE ⚠️

PLEASE RUN THE SCRIPT WITH ADMINISTRATOR/ROOT PRIVILEGES TO ENABLE PROPER KEY LOGGING FUNCTIONALITY.  
WITHOUT THESE ELEVATED PERMISSIONS, THE PROGRAM WILL NOT CAPTURE ANY KEYBOARD EVENTS.

---

WHY?  
Key logging requires low-level access to keyboard events that normal users usually don’t have.  
Running as admin/root allows the program to listen to all system keyboard events.

---

HOW TO RUN WITH ELEVATED PERMISSIONS?

WINDOWS:  
- Run Command Prompt or PowerShell as Administrator (Right-click → Run as administrator).  
- Then run:  
  python "Keyboard Typing Behavior Analyzer.py"

LINUX / macOS:  
- Run the script with sudo:  
  sudo python3 "Keyboard Typing Behavior Analyzer.py"

---

HOW TO INSTALL PYTHON AND REQUIRED PACKAGES?

1. Check Python installation:  
   python3 --version  
   If not installed, install it with your system’s package manager:  

   - Ubuntu/Debian:  
     sudo apt update && sudo apt install python3 python3-pip  
   
   - Fedora:  
     sudo dnf install python3 python3-pip  
   
   - macOS (with Homebrew):  
     brew install python

2. Install required packages:  
   pip3 install keyboard rich  
   (If pip3 not found, try: python3 -m pip install keyboard rich)

---

USAGE

- Run the script with admin/root privileges as above.  
- Press any key to record it.  
- Press ESC to stop and save data in key_events.json.

---

IMPORTANT NOTES

- Without root/admin privileges, keyboard events won’t be captured.  
- On Linux, you might need to use sudo or run terminal as root.  
- On macOS, you might need to grant Accessibility permissions for your terminal app:  
  System Preferences → Security & Privacy → Privacy → Accessibility.

---

ENJOY YOUR TYPING ANALYSIS! 🚀
