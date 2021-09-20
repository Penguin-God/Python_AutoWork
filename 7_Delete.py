from openpyxl import load_workbook
wb = load_workbook("C:/Users/parkj/Desktop/프로그래밍/python/RPA/Excel/File/Sample.xlsx")
ws = wb.active

# 6번째 행 삭제
ws.delete_rows(6, 2) # 6번째 행부터 2줄 삭제

# 2번째 열 삭제
ws.delete_cols(2, 2) # 2번째 열부터 2줄 삭제

wb.save("C:/Users/parkj/Desktop/프로그래밍/python/RPA/Excel/File/Sample_Delete.xlsx")