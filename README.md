# Keylogger

## Overview
This is a simple Python-based keylogger that captures keystrokes along with timestamps and the active application name. The logged data is saved in a text file and periodically sent via email.

## Features
- Captures all keystrokes.
- Logs timestamps for each key press.
- Captures the name of the active application.
- Sends the recorded key logs via email every 30 seconds.
- Runs as a background process.

## Requirements
- Python 3.x
- Required Python Libraries:
  - `pynput`
  - `smtplib`
  - `email`
  - `datetime`
  - `psutil`
  - `threading`
  - `os`

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/keylogger.git
   ```
2. Navigate to the project folder:
   ```sh
   cd keylogger
   ```
3. Install the required dependencies:
   ```sh
   pip install pynput psutil
   ```

## Usage
1. Update the script with your email credentials.
2. Run the script:
   ```sh
   python keylogger.py
   ```
3. To run it silently in the background, rename it to a `.pyw` file:
   ```sh
   mv keylogger.py keylogger.pyw
   ```
4. To stop the keylogger, use Task Manager or Taskkill:
   ```sh
   taskkill /F /IM pythonw.exe
   ```

## Disclaimer
This software is for educational purposes only. Unauthorized use of a keylogger is illegal and unethical. The author is not responsible for any misuse.

