'''

유니티 티셔츠를 뿌립니다. 신청은 이메일로 받으며 선착순 3명한테 티셔츠를 줍니다. 조건에 해당하는 메일을 조회하여 선정된 분들에게는 선정 메일을 그렇지 못한 분들은 탈락 메일을 보내고 선정된 사람들의 정보를 바탕으로 엑셀 파일을 만드세요

[신청 메일 양식]
제목 : 유니티 티셔츠 내놔
본문 : 닉네임/전화번호 뒤 4자리

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

# msg["Subject"] = "유니티 티셔츠 내놔"
# msg["To"] = EMAIL_ADDRESS

def SendMail(subject, to, text):
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = to
    msg["Subject"] = subject
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

#메일 5개 보내기
def SendFiveMail():
    for name in name_list:
        #text = name + "/" + GetRandomNumber()
        text = "/".join(name, GetRandomNumber()) # 내용 많아지면 .join() 이 좋은듯
        SendMail(text)
#SendFiveMail()


# 당첨 결과 답장 보내기

winners_datas = []

def ReplyMail():
    with MailBox("imap.gmail.com", 993) as mail_box:
        mail_box.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

        order = 0
        order_out = 3
        subject = ""
        text = ""
        to = ""

        for mail in mail_box.fetch('SENTSINCE 28-Sep-2021'): # 2021/09/28 부터 온 메일
            if("유니티 티셔츠 내놔" in mail.subject ):
                to = mail.from_
                order += 1
                if(order <= order_out):
                    subject = "[선정]"
                    text = "{}님 축하요 님{} 번째임".format(mail.text.split("/")[0], str(order))
                    winners_datas.append([str(order), mail.text.split("/")[0], mail.text.split("/")[1]])
                else:
                    subject = "[탈락]"
                    text = "{}님 유감임 암튼 그럼 참고로 {}번째 빌려서 탈락함".format(mail.text.split("/")[0], str(order - order_out))
                SendMail(subject, to, text)

ReplyMail()


# 당첨자 엑셀 파일 만들기
from openpyxl import Workbook
wb = Workbook()
ws = wb.active

ws.append(("당첨 번호", "닉네임", "전화번호"))
# column = x축, row = y축
# for winner_index, winner_data in enumerate(winners_datas):
#     for data_index, data in enumerate(winner_data):
#         ws.cell(column=data_index + 1, row= winner_index + 2, value=winner_data[data_index])

for winner_data in winners_datas:
    ws.append(winner_data)

wb.save("project/project_answer.xlsx")