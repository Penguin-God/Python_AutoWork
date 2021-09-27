import os

# 주어진 경로가 파일인지 폴더인지 구분 
print(os.path.isdir("Desktop")) # Desktop은 폴더인가? : True
print(os.path.isfile("Desktop")) # Desktop은 파일인가? : False
print(os.path.isdir("aaa")) # 경로가 존재하지 않으면 False 반환

# 주어진 경로에 파일 또는 폴더가 존재하는가?
print(os.path.exists("Desktop/2_mouse_move.py"))
print(os.path.exists("DESSSS"))


folder_path = "Desktop/File/" 
# 파일 만들기
# open(folder_path + "new_file.txt", "a").close()

# 파일 이름 변경
# os.rename(folder_path + "new_file.txt", folder_path + "new_file_rename.txt")  # 파일 이름을 new_file_rename.txt로 변경

# 파일 삭제
# os.remove(folder_path + "new_file_rename.txt")


# 폴더 생성 : 이미 폴더가 있는데 생성하면 에러가 남 (파일은 안 남)
# os.mkdir(folder_path + "new_folder")

# 하위 폴더를 가지는 폴더 생성
# os.makedirs(folder_path + "new_folders/a/b/c") # a 안에 b 안에 c 식으로 생성됨

# 폴더명 변경
# os.rename(folder_path + "new_folder", folder_path + "new_folder_rename")

# 폴더 삭제
# os.rmdir(folder_path + "new_folder_rename") # 폴더 안이 비어 있을 때만 삭제

import shutil # shell utilities
#shutil.rtree(folder_path + "new_folders") # 폴더에 내용이 있어도 삭제 가능
# 모든 파일이 삭제될 수 있으니 주의 (휴지통에도 안가고 ctrl + z 도 안먹음 그냥 완전삭제)


# 파일 복사하기
#shutil.copy("Excel/File/Sample_Formula.xlsx", "Desktop/File") # 원본 파일 경로, 대상 경로 
# 다른 이름으로 파일 복사하기
#shutil.copy("Excel/File/Sample_Formula.xlsx", "Desktop/File/copy.xlsx")
# copyfile은 대상 경로를 무조건 파일명으로 써아함
#shutil.copyfile("Excel/File/Sample_Formula.xlsx", "Desktop/File/Spmple_Formula_copy_2.xlsx")
# copy2
#shutil.copy2("Excel/File/Sample_Formula.xlsx", "Desktop/File/copy_2.xlsx")

# copy, copyfile : 메타 정보 복사 X
# copy2 : 메타정보 복사 O 
# 메타 정보 : 생성 날짜 정보 등을 가짐   


# 폴더 복사
#shutil.copytree("Desktop", "Desktop/File2") # 원본 폴더 경로, 복사할 경로

# 폴더 이동
# shutil.move("Desktop/File2", ".")
shutil.move("File2", "File_Move_Rename") # 폴더를 못찾으면 이름을 바꿈
