from imap_tools import MailBox
from email_data import *

mail_box = MailBox("imap.gmail.com", 993)
mail_box.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

# limit : 최대 메일 개수
# reverse : True면 최근 메일부터, False면 과거 메일부터
for msg in mail_box.fetch(limit=1, reverse=True):
    print("제목 : ", msg.subject)
    print("발신자 : ", msg.from_)
    print("수신자 : ", msg.to)
    # print("참조자", msg.cc)
    # print("비밀참조자", msg.bcc)
    print("날짜 : ", msg.date)
    print("본문 : ", msg.text)
    print("HTML 메시지 : ", msg.html)
    print("=" * 100)

    # 첨부파일
    print(len(msg.attachments))
    for att in msg.attachments: # 메일의 파일들
        print("파일 이름 : ", att.filename)
        print("타입 : ", att.content_type)
        print("크기 : ", att.size)

        #파일 다운로드
        with open("자소서.hwp", "wb") as f: # 이름이 주소라서 그냥 filename 쓰면 안될 수도 있음 
            f.write(att.payload)
            print("첨부 파일 {} 다운로드".format(att.filename))

mail_box.logout()