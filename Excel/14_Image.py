from openpyxl import Workbook
from openpyxl.drawing.image import Image
wb = Workbook()
ws = wb.active

img = Image("C:/Users/parkj/Desktop/프로그래밍/python/RPA/Excel/File/ExeclTestImage.png")
# C3 위치에 이미지 삽입
ws.add_image(img, "C3")

wb.save("C:/Users/parkj/Desktop/프로그래밍/python/RPA/Excel/File/Sample_Image.xlsx")