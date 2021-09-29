'''

유니티 티셔츠를 뿌립니다. 신청은 이메일로 받으며 선착순 3명한테 티셔츠를 줍니다. 조건에 해당하는 메일을 조회하여 선정된 분들에게는 선정 메일을 그렇지 못한 분들은 탈락 메일을 보내고 선정된 사람들의 정보를 바탕으로 엑셀 파일을 만드세요

[신청 메일 양식]
제목 : 유니티 티셔츠 내놔
봅문 : 닉네임/전화번호 뒤 4자리

[선정 안내 메일]
제목 : 추카추카
본문 : xx님 축하요 님 x번째임

[탈락 안내 메일]
제목 : 유감
본문 : xx님 유감임 암튼 그럼 참고로 x번째 밀려서 탈락함

[선정 명단 엑셀]
순번    닉네임    전화번호 뒷자리

'''
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
 
import smtplib  
from email.message import EmailMessage
from imap_tools import MailBox
from Email.email_data import *
from random import *

name_list = ["PenguinGod", "kd", "Goldmetal", "베르", "고라니"]

msg = EmailMessage()
msg["Subject"] = "유니티 티셔츠 내놔"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS

def SendMail(text):
    msg.set_content(text)
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def GetRandomNumber():
    number = ""
    for i in range(0, 4):
        number += str(randint(0, 9))
    return number

for name in name_list:
    text = name + "/" + GetRandomNumber()
    SendMail(text)
