import pyautogui
size = pyautogui.size() # 현재 화면의 스크린 사이즈를 튜플로 가져옴
print(size)
print(size[0]) # width
print(size[1]) # height     