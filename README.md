# 📧 Multiple Email Sender Application

This Python-based application is designed for sending bulk emails using multiple sender accounts in a round-robin fashion. It efficiently handles rate-limiting and sender rotation, making it ideal for campaigns, academic promotions, and internship offers.

---

## 🚀 Features

- Bulk email sending via Gmail SMTP
- Sender rotation using round-robin logic
- Rate-limiting support (100 emails per sender)
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

