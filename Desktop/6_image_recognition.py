from PIL.ImageOps import grayscale
import pyautogui as auto

# 현재 화면에서 인자값으로 받은 이미지를 찾은 후 이미지가 있는 위치, 크기 정보를 반환
# file_menu = auto.locateOnScreen("Desktop/File/file_menu.png")
# print(file_menu) # 이미지 못찾으면 None 출력

# auto.click(file_menu) # 이미지 위치 가운데 클릭
# auto.moveTo(file_menu) # 이미지 위치 가운데로 이동

# pyautogui는 이미지 기반이므로 해상도나 화면이 바뀌면 높은 확률로 실패하기 때문에 실행되었을 때와 같은 환경을 만드는 것이 중요

# 이미지가 여러개일 때
# auto.sleep(2)
# checkbox = auto.locateAllOnScreen("Desktop/File/checkbox.png") # 중복되는 이미지 다 가져옴
# for img in checkbox:
#     print(img)
#     auto.click(img, duration=0.25)

# All 안쓰면 첫번째 이미지만 가져옴


# 속도 개선

# 기본
# plus_icon = auto.locateOnScreen("Desktop/File/plus_icon.png")
# auto.moveTo(plus_icon)

# # 1. GrayScale : 다 흑백으로 하고 비교 대신 정확도 좀 떨어짐
# plus_icon = auto.locateOnScreen("Desktop/File/plus_icon.png", grayscale = True)
# auto.moveTo(plus_icon)

# 2. 비교 범위 지정
# plus_icon = auto.locateOnScreen("Desktop/File/plus_icon.png", region=(1300, 700, 600, 400))
# auto.moveTo(plus_icon)

# 3. 정확도 조정 (이미지가 잘 인식되지 않을 때 정확도를 낮춰 인식되게 함)
#plus_icon = auto.locateOnScreen("Desktop/File/plus_icon.png", confidence=0.9)
# confidence : 기본값을 0.999 즉 일치율 99.9% 낮출 수 있음 너무 낮추면 이상한데로 감
#auto.moveTo(plus_icon)



# 이미지 대기 (자동화 대상이 로딩 등의 이유로 보여지지 않을 때도 있어서)
import time
import sys

timeout = 5

def Return_Imginfo(filename, timeout):
    start_time = time.time()
    edit_menu = auto.locateOnScreen(filename)

    while edit_menu == None:
        end = time.time()
        print(f"{filename} 파일 발견못함 현재 소요시간 : {end - start_time}")
        auto.sleep(0.3)
        edit_menu = auto.locateOnScreen(filename)

        if(end - start_time > timeout) : # 지정한 시간보다 오래 대기했다면
            print("멈춰!!")
            sys.exit()

    return edit_menu

#auto.click(Return_Imginfo("Desktop/File/edit_menu.png", timeout))