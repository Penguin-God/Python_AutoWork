import pyautogui as auto
# 업무 자동화 중에 사람이 개입이 필요할 수도 있는데 이를 위한 코드들

# print("카운트다운 시작!!")
# auto.countdown(3)
# print("카운트다운 끝!!")

#auto.alert("경고 경고 경고") # 확인 버튼만 있는 팝업

# result = auto.confirm("GoGo?") # 확인, 취소 버튼 있는 팝업
# print(result) # 확인 : OK, 취소 : Cancle

# prompt : 사용자의 입력을 받는 창
# result = auto.prompt("요즘 뭐하고 삼?", "인생") # 질문, 제목
# print(result) # 입력받은 값, Cancel하면 None

result = auto.password("암호") # 암호 입력
print(result) # 입력받은 값