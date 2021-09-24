import pyautogui

# 전역 좌표 기준으로 지정한 위치에 마우스 이동 (왼쪽 위가 (0, 0) )
pyautogui.moveTo(100, 100, duration=3) # 인수 : x, y, 지속시간 (x는 오른쪽이 +, y는 아래쪽이 +)

# 기존 위치에서 지정한 크기만큼 미우스 이동
pyautogui.move(130, 222, duration=3)

# 마우스 위치 : point(x, y) 형식
print(pyautogui.position())
p = pyautogui.position()
print(p.x, p.y)