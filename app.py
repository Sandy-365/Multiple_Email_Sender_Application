import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import itertools

with open("senders.txt", "r") as f:
    senders = [line.strip().split("-->") for line in f if "-->" in line.strip()]

with open("emails.txt", "r") as f:
    recipients = [line.strip() for line in f if line.strip()]

with open("message.txt", "r") as f:
    lines = f.read().splitlines()

sub = lines[0]
sep_index = lines.index("---")
body = "\n".join(lines[sep_index+1:])

senders_cycle = itertools.cycle(senders)
batch = 100

try:
    for i in range(0, len(recipients), batch):
        sender_email, sender_pass = next(senders_cycle)
        batch_recipients = recipients[i:i+batch]

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, sender_pass)

            for r in batch_recipients:
                msg = MIMEMultipart()
                msg["Subject"] = sub
                msg["From"] = sender_email
                msg["To"] = r
                msg.attach(MIMEText(body, "html"))
                server.sendmail(sender_email, r, msg.as_string())
                print(f"✅ Email sent to {r} from {sender_email}")

except Exception as e:
    print(f"❌ Error: {e}")
