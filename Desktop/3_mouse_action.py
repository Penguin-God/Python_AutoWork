import pyautogui as auto

#auto.click(64, 17) # 지정한 좌표로 이동 후 마우스 클릭 (좌표 안넣으면 현재 마우스 위치 클릭)

# auto.doubleClick() # 클릭 2번
# auto.clicks(500) # 500번 클릭

#auto.sleep(2)
# auto.mouseDown() # 마우스 누른 상태
# auto.move(200, 200, duration=2) # 마우스 누른채로 이동
# auto.mouseUp() # 마우스 뗌 (이거 안하면 계속 누르고 있는 상태가 됨)

# auto.rightClick() # 우클릭
# auto.middleClick() # 휠 클릭

auto.drag(100, 200, duration=2) # 좌표 크기만큼 드래그하면서 이동 (너무 빠르면 작동 안함)
auto.dragTo(100, 200, duration=2) # 지정한 좌표로 드래그하면서 이동

auto.scroll(300) # 위 방향으로 300만큼 스크롤
# 양수는 +, 음수는 -