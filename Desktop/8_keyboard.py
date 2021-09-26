import pyautogui as auto

aw = auto.getWindowsWithTitle("제목 없음")[0]
aw.activate()
auto.sleep(2)

# auto.write("Hello World", interval=0.1)  # interval : 타이핑 딜레이 시간
# auto.write('\n')  # 줄바꿈 먹음
# auto.write('Hello Line 3')
# auto.write("안녕 한국어")  # 한국어는 안먹음

# 배열 안에 있는 거 순서대로 적음
#auto.write(["H", "e", "l", "enter", "l", "o", "left", "home", "end"], interval=0.3)
# left는 왼쪽, enter는 엔터 end는 마지막, home은 처음 [] 안에 들어가면 2글자부터는 명령어로 취급해서 안써짐

# 특수기호 
# auto.keyDown("shift") # shift 누른 상태
# auto.press("6") # 6 눌렀다 때기
# auto.keyUp("shift") # shift 때기

# 조합키 (전체 선택 후 지운 후 복구)
def CtrlClcik(key):
    auto.keyDown("ctrl")
    auto.press(key)
    auto.keyUp("ctrl")
# CtrlClcik("a")
# auto.sleep(2)
# auto.press("backspace")
# auto.sleep(2)
# CtrlClcik("z")


# 간편한 조합키
#auto.hotkey("ctrl", "a") 
# ctrl 누르고 > a 누르고 > a 때고 > ctrl 때는 순서로 진행


# 한국어 입력
import pyperclip as clip # 클릭보드 : 복사한 내용을 임시로 가지고 있는 공간
clip.copy("안녕 세상")
auto.hotkey("ctrl", "v")

# 키보드 자동화 작업 강제종료법 : ctrl + alt + delete