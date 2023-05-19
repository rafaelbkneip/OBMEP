import xlsxwriter

def salvar(unica):

    workbook = xlsxwriter.Workbook('OBMEP.xlsx')
    sheet = workbook.add_worksheet()   

    try:
        for i in range(len(unica)):
            for j in range(len(unica[0])):
                sheet.write(i+1, j, unica[i][j])

    except Exception as e:
        print(e)

    workbook.close()

    return print("Finalizado!")