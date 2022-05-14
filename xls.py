'''
De toda la información obtenida de scrapping y weather, 
la vamos a tener en main, y main se la va a pasar a xls para que la mande a excel
'''
import openpyxl as xl


wb = xl.workbook()
ws = wb.acrtive

ws["A1"].value = "Nombre: "
ws["B2"].value = name
ws["A2"].value = "Edad: "
ws["B2"].value = age
ws["A3"].value = "Lugar de nacimiento: "
ws["B3"].value = bornPlace
ws["A4"].value = "Redes sociales: "
ws["B4"].value = socialMedia
ws["A5"].value = "Podios: "
ws["B5"].value = podiums
ws["A6"].value = "Victorias: "
ws["B6"].value = victories
ws["A7"].value = "Años en F1: "
ws["B7"].value = years

ws["A9"].value = "Proximos 3 eventos"
ws["B9"].value = "Fecha"
ws["C9"].value = "Temp. Min."
ws["D9"].value = "Temp. Max."

ws["E1"].value = "Noticias."
ws["E2"].append = news

wb.save("info.xlsx")