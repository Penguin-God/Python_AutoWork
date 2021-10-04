import pyautogui as auto

# 스크린샷 찍고 저장
auto.sleep(5)
img = auto.screenshot() # 현재 활성화된 창을 찍음
img.save("C:/Users/parkj/Desktop/프로그래밍/python/RPA/Desktop/File/screenshot.png")

#auto.mouseInfo()
#31,18 92,167,236 #5CA7EC 왼쪽 위에 vscode에 마우스 갖다대면 나오는 정보

rgb = auto.pixel(31,18) # 해당 좌표의 rgb를 튜플로 가져옴
print(rgb)

print(auto.pixelMatchesColor(31, 18, rgb)) # 해당 좌표의 rgb와 인수의 rgb가 같은지 비교
print(auto.pixelMatchesColor(31, 18, (92,167,236))) # 그냥 바로 값 넣어도 됨
print(auto.pixelMatchesColor(31, 18, (92, 167, 235))) # rgb값이 1만 틀려도 False 출력