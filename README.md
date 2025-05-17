
# 📧 Multiple Email Sender Application

This Python-based application sends bulk emails using multiple sender accounts in a round-robin fashion. It efficiently handles rate limiting and sender rotation, making it ideal for campaigns, academic promotions, and internship offers.

---

## 🚀 Features

- Bulk email sending via Gmail SMTP  
- Sender rotation using round-robin logic  
- Rate-limiting support (e.g., 500 emails per sender)  
- Loads email subject and HTML body from `message.txt`  
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

```
├── app.py     # Main script for sending emails  
├── senders.txt             # Sender emails and app passwords, format: email-->app_password  
├── emails.txt              # Recipient emails, one per line  
├── message.txt             # Email subject and HTML body separated by a line with "---"  
```

---

## 📝 Setup Instructions

1. **Clone or Download the Project Folder**

2. **Prepare the `senders.txt` File**  
Each line should contain a sender email and its app password separated by `-->`:  
```
sender1@gmail.com-->app_password1
sender2@gmail.com-->app_password2
```

3. **Prepare the `emails.txt` File**  
Add recipient emails, one per line:  
```
recipient1@gmail.com
recipient2@gmail.com
```

4. **Prepare the `message.txt` File**  
The first line is the email subject, then a line containing only `---`, followed by the HTML email body. For example:  
```
Exciting Training & Internship Program | IIT-Kharagpur & LaunchEd
---
<html>
<body>
  <h1>Hello Students!</h1>
  <p>This is the email content in HTML format.</p>
</body>
</html>
```

5. **Run the Script**  
Make sure Python 3 is installed, then run:  
```
python send_bulk_emails.py
```

---

## 💌 Email Template

The email content is fully customizable via the `message.txt` file, allowing for rich HTML formatting, including headings, lists, buttons, and links.

---

## 🧪 Testing & Validation

- Verified sender rotation logic for proper batch processing  
- Handled SMTP exceptions and errors gracefully  
- Tested with valid and invalid email addresses  
- Ensured logs reflect email delivery status  

---

## ⚠️ Notes

- Gmail limits apply (usually 500 emails/day per account)  
- Use **App Passwords** instead of regular Gmail passwords  
- Enable 2FA on Gmail before generating app passwords  
- Keep your app passwords confidential and avoid exposing them in public repos  

---

## 📃 License

This project is for educational and internal use only. Modify and extend it as per your requirements.
