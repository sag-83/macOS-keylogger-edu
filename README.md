# 🛡️ macOS Educational Keylogger

This Python-based keylogger was created for **educational and ethical use only**, specifically on **macOS**. It's designed to demonstrate how input capturing works, how permissions are managed, and how defenders can identify such behavior.

> ⚠️ **Disclaimer**: Do not use this tool on any device without **explicit permission**. This is strictly for cybersecurity education and training purposes.

---

## 🚀 Key Features
- ✅ Logs all keystrokes in real-time
- ✅ Live terminal output (updates every 10s)
- ✅ Recognizes special keys like Enter, Space, and Backspace
- ✅ Multithreaded for smooth performance
- ✅ macOS Accessibility API compatible
- ✅ Log files auto-ignored via `.gitignore`

---

## 🧭 How to Run

1. **Create a virtual environment**
   ```bash
   python3 -m venv keylogger-env
   source keylogger-env/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install pynput
   ```

3. **Navigate to your script location**
   ```bash
   cd ~/Desktop/key_logger
   ```

4. **Run the keylogger**
   ```bash
   python3 keylogger.py
   ```

Logs are saved as `.txt` files with timestamps in the filename.

---

## 📦 Demo Output (Sample Log)
```
<shift_r>I am so happy right now that my first project is working.
```

---

## 🧹 Note
Make sure `keylog_*.txt` is listed in `.gitignore` to prevent sensitive logs from being uploaded.

---

## 👨‍💻 Author
Built  by Sparsh for educational purposes.
