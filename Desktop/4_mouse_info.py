import pyautogui as auto

auto.mouseInfo() # 현재 위치한 좌표, 갖다대고 있는 이미지의 RGB등 여러 정보를 카피할 수 있는 GUI창이 뜸
# vs code icon : 28,19 90,165,236 #5AA5EC

#auto.FAILSAFE = False # 마우스 막 움직여도 종료 안함
auto.PAUSE = 1 # 모든 동작에 1초 대기 (너무 빠르게 움직여서 동작이나 종료가 안되는 버그 방지용)

# 데스크탑 업무 자동화는 window를 왔다갖다해서 Ctrl + c 강제종료가 안먹으므로 마우스를 구석에 갖다대서 종료함
for i in range(0,5):
    auto.move(100,100)