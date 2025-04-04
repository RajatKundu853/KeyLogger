# KeyLogger
A simple stealth keylogger that captures keyboard events.

## 🚀 Features

- Captures all key presses.
- Sends data via Telegram Bot.
- Uses built-in libraries for system and network info.
- Lightweight and easy to deploy & undetectable.

## 🧰 Requirements

- Python 3.x

### 📦 Python Libraries Used

| Library   | Description                        | 
|-----------|------------------------------------|
| requests  | HTTP requests handler              | 
| pynput    | Keyboard event monitoring          | 

> `time`, `os`, `sys`, and `socket` are built-in and require no installation.

## 🧪 Installation & Usage

1. **Unzip the project.**
2. **Move it in a folder which is not used regularly by users.**
3. **Set your own BOT Token & Chat ID in `keylogger.py` and save it (ctrl+s).**
4. **Now just double click on `start_keylogger.bat` to start.**
5. **Double click on `stop.cmd` to stop keylogger.**
     -(If you Add It to Windows Task Scheduler (Auto-Start on Boot) then `stop.cmd` can stop the keylogger upto next start-up)

## ⚙️ Add It to Windows Task Scheduler (Auto-Start on Boot)

You can configure the keylogger to run automatically when the system starts by adding it to **Windows Task Scheduler**.

### 📌 Step-by-Step Guide

1. Press `Win + R`, type `taskschd.msc`, and press **Enter** to open Task Scheduler.
2. Click **Create Basic Task** (on the right panel).
3. Name it something stealthy like: `KeyLogger`.   (You can change the name & details for your purpose)
4. Click **Next** → Select **When the computer starts**.
5. Click **Next** → Choose **Start a program**.
6. Browse to and select your `start_keylogger.bat` file.
7. Click **Finish**.

## 🔧 Modify Task Scheduler Settings for Stealth & Reliability

1. Open Task Scheduler (`Win + S`, search “Task Scheduler”).
2. Locate your task under **Task Scheduler Library** (left panel).
3. Double-click the task to open properties.

### 🛡️ General Tab
- Check **Run with highest privileges** (if admin rights are needed).
- Set **Configure for**: `Windows 10`.   (Heighest version)

### ⏱️ Triggers Tab
- Double-click the trigger “At startup”.
- Check **Enabled**.
- Add a delay of **30 seconds**:
  - New → Begin the task: **At startup** → **Delay task for 30 seconds**.

### ⚙️ Conditions Tab
- Uncheck **Start the task only if the computer is on AC power**.
- Uncheck **Start only if the following network connection is available** (if applicable).

### 🧪 Actions Tab
- Click **Edit**.
- Confirm the correct `.bat` file is selected.

### 🔄 Settings Tab
- Check **Allow task to be run on demand**.
- Check **Run task as soon as possible after a scheduled start is missed**.
- Set **If the task fails, restart every**: 1 minute, up to 3 times.
- Uncheck **Stop the task if it runs longer than:**.
- Uncheck **If the running task does not end when requested,force it to stop**.
- Uncheck **If the task is not scheduled to run again, delete it after:**.
- Set **If the task is already running,then the following rule applies**: Do not start a new instance.

➡️ Click **OK** and **restart PC** to start keylogger.


## ❌ How to Stop Auto-Start?

If you want to disable or remove the task:

1. Open **Task Scheduler** (`taskschd.msc`).
2. Find your task under **Task Scheduler Library**.
3. Right-click → Choose **Disable** or **Delete**.


## ⚠️ Disclaimer
This tool is developed strictly for **educational and research purposes only**. Any form of **unauthorized monitoring, data logging, or spying** is **illegal**, **unethical**, and may be punishable under cybercrime laws.

> **The author does not condone or support any malicious or illegal use of this tool.**  
> **Use it only in environments where you have full permission and legal authority.**  

The author **is not responsible** for any damage, data loss, legal consequences, or misuse caused by this tool. By using this project, you agree to take full responsibility for your actions and ensure compliance with all applicable laws.

## 🧑‍💻 Author
Rajat Kundu
Cybersecurity & IoT Enthusiast
