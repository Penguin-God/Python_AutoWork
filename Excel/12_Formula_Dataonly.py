from openpyxl import load_workbook
# data_only=True 안하면 수식을 그대로 가져옴
wb = load_workbook("C:/Users/parkj/Desktop/프로그래밍/python/RPA/Excel/File/Sample_Formula.xlsx", data_only=True)
ws = wb.active

# evaluate(평가) 되지 않은 데이터는 None으로 읽음
# 수식은 엑셀 파일을 열면서 계산되는 것이지 python 런타임 과정에서는 그냥 string 값만 들어감
# 수식이 계산되 값을 가져오고 싶으면 엑셀 파일을 한 번 열어서 수식을 계산하게 한 후 파일을 저장해야됨
for row in ws.values:
    print(row[0])

