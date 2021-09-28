import smtplib
from email_data import *

with smtplib.SMTP("smtp.gmail.com", 587) as smtp: # smtplib 객체 생성
    smtp.ehlo() # 연결이 잘 되었는지 확인
    smtp.starttls() # 이메일 내용 암호화
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD) # 로그인

    subject = "Test email" # 제목 변수
    body = "this is python RPA email" # 본문 내용 변수
    # 정해진 형태로 메시지 만듬 (뛰어쓰기까지 하나도 틀리면 안됨)
    message = f"Subject: {subject}\n{body}"

    # 발신자, 수신자, 정해진 형태의 메시지 
    smtp.sendmail(EMAIL_ADDRESS, "gkswh4860@naver.com", message)