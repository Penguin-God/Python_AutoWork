'''
1. 그림판 실행 후 최대화 win + r 후 mspaint 입력 
2. 상단의 텍스트 기능을 이용해 흰 영역 아무 곳에나 글자 입력
3. 5초 대기 후 그림판 종료 이 때 저장하지 않음을 선택
'''

import pyautogui as auto
import pyperclip as clip
import sys
import time
auto.PAUSE = 2

# 1. 그림판 실행 후 최대화
auto.hotkey("win", "r")
auto.write("mspaint")
auto.press("enter")
paint_window = auto.getActiveWindow()
paint_window.maximize()

# 2. 한국어 글자 입력
text_icon = auto.locateOnScreen("Desktop/File/paint_window_text_icon.png")
auto.click(text_icon)

auto.click(paint_window.right - 1000, paint_window.top + 500)

# 보너스 가변적인 이미지일 때 상대 좌표로 작업하기 (글자 폰트 바꾸기)
text_icon = auto.locateOnScreen("Desktop/File/text_btn.png")
auto.click(text_icon.left + 155, text_icon.top + 50)

# 원하는 폰트 이미지 찾을 때까지 스크롤하면서 찾기
font_icon = auto.locateOnScreen("Desktop/File/my_font_btn.png", region = (100, 50, 200, 900))

start_time = time.time()
while font_icon == None:
    auto.scroll(100)
    font_icon = auto.locateOnScreen("Desktop/File/my_font_btn.png", region = (100, 50, 200, 900))

    if(time.time() - start_time > 15):
        print("Time Up")
        sys.exit()

auto.click(font_icon)

# 한글 복붙
clip.copy("안녕 그림판")
auto.hotkey("ctrl", "v")

# 3. 저장 안하고 나가기

# 박준의 창의적이지 못한 풀이
# auto.click(paint_window.right - 10, paint_window.top + 20)
# auto.click(1000, 530) # print(auto.position()) 으로 마우스 값 가져옴

paint_window.close()
auto.sleep(1)
auto.press("n")