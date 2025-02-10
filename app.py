import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import itertools

# Load senders (email & app password) from a file
with open("senders.txt", "r") as file:
    senders = [line.strip().split("-->") for line in file if "-->" in line.strip()]

# Read recipient emails from a text file
with open("emails.txt", "r") as file:
    recipient_emails = [line.strip() for line in file if line.strip()]  # Remove empty lines

# Email content
subject = "🚀 Exclusive Opportunity | IIT-Kharagpur & LaunchEd Training!"
body = """\
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; font-size: 16px; }
        .container { padding: 20px; border-radius: 10px; background: #f4f4f4; }
        .highlight { color: #ff6600; font-weight: bold; font-size: 18px; }
        .cta { background: #ff6600; color: #fff; font-size: 18px; padding: 12px 18px; border-radius: 5px; text-decoration: none; display: inline-block; margin-top: 10px; }
        .footer { font-size: 14px; color: #666; margin-top: 20px; }
        .original-link { font-size: 14px; color: #000; font-weight: bold; word-wrap: break-word; }
    </style>
</head>
<body>
    <div class="container">
        <h2>🚀 Exciting Opportunity with <span class="highlight">IIT-Kharagpur & LaunchEd!</span></h2>
        <p style="font-size:18px;"><b>Dear Students,</b></p>
        <p style="font-size:16px;">Are you ready to take your skills to the next level? 😃</p>
        <h3 style="font-size:18px;">✨ Program Highlights:</h3>
        <ul style="font-size:16px;">
            <li>📚 <b>Training + Internship</b></li>
            <li>🔥 <b>10+ Minor Projects</b></li>
            <li>🎓 <b>1 Capstone Project</b></li>
            <li>📝 <b>Resume Building & Mock Interviews</b></li>
            <li>✅ <b>Wipro Dice ID Verification</b></li>
            <li>🏆 <b>AICTE Approved Internships</b></li>
        </ul>
        <p style="font-size:18px;"><b>💡 Stop Wondering & Start Building Your Future!</b> 🚀</p>
        <p>
            <a class="cta" href="https://docs.google.com/forms/d/e/1FAIpQLSdeD_dzCR5rGfKKe7nGM4fKnhofD_l8H6JYTFQJk1MV2ZMfmw/viewform?usp=sharin">
                👉 Register Now
            </a>
        </p>
        <p class="footer">Don't miss this golden opportunity! 🌟</p>
        <p class="original-link">🔗Registration Link: <br> 
            <a href="https://docs.google.com/forms/d/e/1FAIpQLSdeD_dzCR5rGfKKe7nGM4fKnhofD_l8H6JYTFQJk1MV2ZMfmw/viewform?usp=sharin">
                https://docs.google.com/forms/d/e/1FAIpQLSdeD_dzCR5rGfKKe7nGM4fKnhofD_l8H6JYTFQJk1MV2ZMfmw/viewform?usp=sharin
            </a>
        </p>
    </div>
</body>
</html>
"""

# Round-robin sender selection
senders_cycle = itertools.cycle(senders)  # Rotates through senders

# Batch size (100 emails per sender)
batch_size = 100

# Sending emails in batches
try:
    for i in range(0, len(recipient_emails), batch_size):
        sender_email, sender_password = next(senders_cycle)  # Get next sender

        batch_recipients = recipient_emails[i:i + batch_size]  # Get the next 100 recipients

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            for recipient in batch_recipients:
                msg = MIMEMultipart()
                msg["Subject"] = subject
                msg["From"] = sender_email
                msg["To"] = recipient

                msg.attach(MIMEText(body, "html"))

                server.sendmail(sender_email, recipient, msg.as_string())
                print(f"✅ Email sent to {recipient} from {sender_email}")

except Exception as e:
    print(f"❌ Error: {e}")
