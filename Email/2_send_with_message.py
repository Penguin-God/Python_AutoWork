import smtplib  
from email_data import *
from email.message import EmailMessage

msg = EmailMessage()

msg["Subject"] = "테스트 메일" # 제목
msg["From"] = EMAIL_ADDRESS # 보내는 사람
msg["To"] = "gkswh4860@naver.com" # 받는 사람

# 여러 사람에게 보낼 때 ( ", " 로 구분)
#msg["To"] = "gkswh4860@naver.com, parkjun141@gmail.com"

# 리스트를 이용해서 여러 사람에게 이메일 보내기
to_list = ["gkswh4860@naver.com", "parkjun141@gmail.com"]
#msg["To"] = ", ".join(to_list) # ", " 로 구분해서 리스트 요소를 묶은 string 값 반환
print(", ".join(to_list)) 

msg.set_content("테스트 본문") # 본문

# 참조
#msg["Cc"] = "gkswh4860@naver.com"

# 비밀 참조
#msg["Bcc"] = "gkswh4860@naver.com"

with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)