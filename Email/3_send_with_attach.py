import smtplib  
from email_data import *
from email.message import EmailMessage

msg = EmailMessage()

msg["Subject"] = "python RPA 메일" # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = DAHAN_ADDRESS # 받는 사람
msg.set_content("자소서 파일 뽑아줘 다현")

with open("Email/file/자소서.hwp", "rb") as hwp:
    # attach : 붙이다
    # MIME 타입 : 인터넷에 전달되는 파일 포맷을 위한 식별자 (인터넷에 MIME type 검색해서 파일에 맞는 타입을 찾을 수 있음)
    msg.add_attachment(hwp.read(), maintype = "text", subtype = "plain", filename = hwp.name)

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)