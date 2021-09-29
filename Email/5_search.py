from imap_tools import MailBox
from email_data import *

# with 문은 끝날 때 자동으로 close()가 실행되므로 logout() 안해도 됨
with MailBox("imap.gmail.com", 993) as mail_box:
    mail_box.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

    # 모든 메일 가져오기 (접근한 메일은 읽음 처리됨)
    # for mail in mail_box.fetch(reverse=True): 
    #     print("[{}] : {}".format(mail.from_, mail.subject))


    # 읽지 않은 메일 가져오기
    # for mail in mail_box.fetch("(UNSEEN)", limit=10, reverse=True): 
    #     print("[{}] : {}".format(mail.from_, mail.subject))


    # 특정인이 보낸 메일 가져오기
    # for mail in mail_box.fetch("(FROM info@unity3d.com)", reverse=True):
    #     print("[{}] : {}".format(mail.from_, mail.subject))


    # 어떤 글자를 포함하는 메일 (제목, 본문)
    # '' 로 먼저 감싸고 실제로 찾을 텍스트는 ""로 감싸야 함 
    # 뛰어쓰기로 구분하여 만나보세요, unity 각각의 단어가 포함된 메일을 찾음 (한국어는 안됨)
    # for mail in mail_box.fetch('(TEXT "hi unity")', reverse=True): 
    #     print("[{}] : {}".format(mail.from_, mail.subject))


    # 어떤 글자를 포함하는 메일 (제목만)
    # for mail in mail_box.fetch('(SUBJECT "Unity")', reverse=True): 
    #     print("[{}] : {}".format(mail.from_, mail.subject))


    # 한국어 서치
    # for mail in mail_box.fetch(reverse=True):
    #     if("만나보세요" in mail.subject):
    #         print("[{}] : {}".format(mail.from_, mail.subject))


    # 특정 날짜 이후의 메일 가져옴
    # 일 - 월 - 년
    # for mail in mail_box.fetch('(SENTSINCE 01-Jun-2021)', reverse=True): 
    #     print("[{}] : {}".format(mail.from_, mail.subject))


    # 특정 날짜에 온 메일 가져옴    
    # for mail in mail_box.fetch('(ON 29-Sep-2021)', reverse=True): 
    #     print("[{}] : {}".format(mail.from_, mail.subject))


    # 두 가지 이상의 조건을 만족하는 매일 가져오기 (&& 조건)
    # for mail in mail_box.fetch('(ON 29-Sep-2021 SUBJECT "python")', reverse=True):
    #     print("[{}] : {}".format(mail.from_, mail.subject))


    # 여러 조건 중 하나의 조건이라도 만족하는 메일 가져오기 (|| 조건)
    for mail in mail_box.fetch('(OR ON 29-Sep-2021 SUBJECT "Unity")', reverse=True):
        print("[{}] : {}".format(mail.from_, mail.subject)) 
