from openpyxl import Workbook

def createxls(name, age, bornPlace, socialMedia, podiums, victories, years, nextevents, news):
    wb = Workbook()
    ws = wb.active

    ws["A1"].value = "Nombre: "
    ws["B1"].value = name
    ws["A2"].value = "Edad: "
    ws["B2"].value = age
    ws["A3"].value = "Lugar de nacimiento: "
    ws["B3"].value = bornPlace
    ws["A4"].value = "Redes sociales: "
    socialPrint = ""
    for social in socialMedia:
        socialPrint.join("; "+social) 
    ws["B4"].value = socialPrint
    ws["A5"].value = "Podios: "
    ws["B5"].value = podiums
    ws["A6"].value = "Victorias: "
    ws["B6"].value = victories
    ws["A7"].value = "Años en F1: "
    ws["B7"].value = years

    ws["A9"].value = "Proximos eventos"
    ws["A10"].value = nextevents[0]
    ws["A11"].value = nextevents[3]
    ws["A12"].value = nextevents[4]
    ws["B9"].value = "Temp. Min."
    ws["C9"].value = "Temp. Max."

    ws["E1"].value = "Noticias."
    ws["E2"].value = news[0]
    ws["E3"].value = news[1]
    ws["E4"].value = news[2]

    wb.save("info.xlsx")

    return "Archivo creado con éxito."