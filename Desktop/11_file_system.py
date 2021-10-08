import os

print(os.getcwd()) # cws : current working directory (현재 작업 공간)
# os.chdir("Desktop") # Desktop으로 작업 공간 이동
# print(os.getcwd())
# os.chdir("..") # 부모 폴더로 이동
# print(os.getcwd())
# os.chdir("../..") # 조부모 폴더로 이동 (무한 반복 가능)
# print(os.getcwd())
# os.chdir("c:/") # 주어진 절대 경로로 이동
# print(os.getcwd())

# 파일 경로 만들기
file_path = os.path.join(os.getcwd(), "Desktop", "File","text_file.txt") # 절대 경로 생성
print(file_path)

# 파일 경로에서 파일 빼고 폴더 경로만 가져오기
forder_path = os.path.dirname(r"C:\Users\parkj\Desktop\프로그래밍\python\RPA\Desktop\File\text_file.txt")
# r : 이스케이프문 무시하고 문자 그대로 읽기
print(forder_path)

# 파일 정보 가져오기
import datetime

# 파일 생성 날짜 가져오기
create_time = os.path.getctime("Desktop/11_file_system.py")
print(create_time)
# 날짜 정보를 strftime을 통해서 연월일 시분초 형태로 출력
print(datetime.datetime.fromtimestamp(create_time).strftime("%Y/%m/%d %H:%M:%S"))

# 파일 수정 날짜 가져오기
modifide_time = os.path.getmtime("Desktop/11_file_system.py")
print(datetime.datetime.fromtimestamp(modifide_time).strftime("%Y/%m/%d %H:%M:%S"))

# 파일 접근 날짜 가져오기
access_time = os.path.getatime("Desktop/7_window.py")
print(datetime.datetime.fromtimestamp(access_time).strftime("%Y/%m/%d %H:%M:%S"))

# 파일 크기 가져오기
file_size = os.path.getsize("Desktop/11_file_system.py")
print(file_size) # 바이트 단위로 파일 크기 가져옴


# 파일 목록 가져오기
#print(os.listdir()) # 현재 폴더 아래의 폴더, 파일 목록 가져옴
#print(os.listdir("Desktop"))


# 파일 목록 가져오기 (하위 폴더 모두 포함)
# any_files = os.walk("Desktop") # . : 현재 폴더 기준으로
# print(any_files) # 객체 정보 출력
# for aa in any_files:
#     #상위 폴더, 상위 폴더에 포함된 폴더, 상위 폴더에 포함된 파일
#     print(aa ) 

# 폴더에서 특정 파일 찾기
search_name = "11_file_system.py"
for root, dirs, files in os.walk("."):
    if(search_name in files): # files 안에 search_name이 있으면
        print(os.path.join(root, search_name))

import fnmatch
pattern = "8*.py" # 1로 시작하고 .py로 끝나는 모든 파일
result = []
for root, dirs, files in os.walk("."):
    for name in files:
        if(fnmatch.fnmatch(name, pattern)): # 파일 이름과 패턴이 일치하면
            result.append(os.path.join(root, name))

print(result)