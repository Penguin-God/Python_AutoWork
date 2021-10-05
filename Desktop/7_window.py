import pyautogui as auto

auto.sleep(2)
active_window = auto.getActiveWindow()  # 현재 활성화된 창
print(active_window.title)  # 창의 제목 정보
print(active_window.size)  # 창의 크기 정보 (width, height)
print(active_window.left, active_window.right,  # 창의 좌표 정보
      active_window.top, active_window.bottom)

# 활성화된 창 기준으로 좌표 구하고 클릭
auto.click(active_window.left + 25, active_window.top + 90)

#for window in auto.getAllWindows():
#    print(window)  # 모든 윈도우 출력

for w in auto.getWindowsWithTitle("Groove 음악"):  # 해당 이름을 가진 window만 가져옴
    print(w)

name = "Chrome"
youtube = auto.getWindowsWithTitle(name)[0]  # 크롬 탭은 활성화 되있는것만 가져올 수 있음
print(youtube)
if(youtube.isActive == False):  # 현재 활성화가 되지 않았다면
    youtube.activate()  # window 활성화

auto.sleep(2)

if(youtube.isMaximized == False):  # 창 최대가 아니면 창 최대화
    youtube.maximize()

auto.sleep(2)

# if(youtube.isMinimized == False):  # 창 내려가 있는 상태 아니면 창 내림
#     youtube.minimize()

youtube.restore()

auto.sleep(1)

#youtube.close()  # 크롬 탭 닫으면 그냥 전체 창을 닫아버림
# 크롬 탭을 하나의 window로 인식하는 것 같음
