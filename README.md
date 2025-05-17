# 📧 Multiple Email Sender Application

This Python-based application is designed for sending bulk emails using multiple sender accounts in a round-robin fashion. It efficiently handles rate-limiting and sender rotation, making it ideal for campaigns, academic promotions, and internship offers.

---

## 🚀 Features

- Bulk email sending via Gmail SMTP
- Sender rotation using round-robin logic
- Rate-limiting support (500 emails per sender)
- HTML-formatted email content
- Exception handling with error reporting
- Status printing after each sent email
- Easy integration with sender and recipient files

---

## 🛠️ Technologies Used

- Python 3
- `smtplib` for SMTP communication
- `email.mime` for message formatting
- `itertools` for sender rotation
- Gmail SMTP (`smtp.gmail.com`, Port: 587)

---

## 📂 Project Structure

├── send_bulk_emails.py # Main script for sending emails
├── senders.txt # Contains sender emails and app passwords in format: email-->app_password
├── emails.txt # Contains recipient email addresses, one per line

---

## 📝 Setup Instructions

1. **Clone or Download the Project Folder.**

2. **Prepare the `senders.txt` File**

   Each line should contain a sender email and its app password separated by `-->`:
sender1@gmail.com-->app_password1
sender2@gmail.com-->app_password2


3. **Prepare the `emails.txt` File**

Add all recipient emails, one per line:
recipient1@gmail.com
recipient2@gmail.com


4. **Run the Script**

Make sure you have Python 3 installed and run:
python send_bulk_emails.py


---

## 💌 Email Template

The application sends visually styled HTML emails containing:

- Eye-catching headings
- List of benefits
- A clear call-to-action button
- Registration link
- Polished formatting using inline CSS

---

## 🧪 Testing & Validation

- Sender rotation logic tested for proper batching
- Fault injection used to simulate SMTP failures
- Validated logging and retry mechanisms
- Functional tests for all input scenarios (valid/invalid emails, empty fields)

---

## ⚠️ Notes

- Gmail limits apply (typically 500 emails/day for personal accounts)
- Use **App Passwords** (not your regular Gmail password)
- Enable 2FA on your Gmail account before generating an app password
- Do not share your app password or expose it in public repositories

---

## 📃 License

This project is provided for educational and internal use only.
Feel free to modify and extend it based on your needs.
