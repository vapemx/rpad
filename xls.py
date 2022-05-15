import openpyxl as xl

def createxls(name, age, bornPlace, socialMedia, podiums, victories, years, nextevents, news):
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

    ws["A9"].value = "Proximos eventos"
    ws["A10"].value = nextevents
    ws["B9"].value = "Temp. Min."
    ws["C9"].value = "Temp. Max."

    ws["E1"].value = "Noticias."
    ws["E2"].value = news[0]
    ws["E3"].value = news[1]
    ws["E4"].value = news[2]

    wb.save("info.xlsx")

    return "Archivo creado con éxito."