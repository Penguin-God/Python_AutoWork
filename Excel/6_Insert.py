from openpyxl import load_workbook
wb = load_workbook("Sample.xlsx")
ws = wb.active

# 엑셀 삽입 단축키
# Crtl + Spacebar + +(Shift + =) : 입력 시 삽입선택창이 뜨며 어떤식으로 셀을 삽입할지 선택가능
# Shift + Spacebar : 입력 시 행(row) 한 줄 선택 삽입선택창 단축키를 입력하면 지정한 행에 한 줄 추가됨
# Ctrl + Spacebar : 입력 시 열(column) 한 줄 선택 삽입선택창 단축키를 입력하면 지정한 열에 한 줄 추가됨

# 8번째 행에 빈 줄 삽입
ws.insert_rows(8, 5) # 빈 행 5줄 추가

# B열에 빈 줄 삽입
ws.insert_cols(2,3) # 빈 열 3줄 추가

wb.save("Sample_Insert.xlsx")

