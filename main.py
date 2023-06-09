import PyPDF2


def func_pdfChecker(name):
    with open('AgroBook.pdf', 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        text_done = 'None \n'
        for page_num in range(len(pdf_reader.pages)):
            pdf_page = pdf_reader.pages[page_num]
            text_page = pdf_page.extract_text().replace('\n','').replace('\r','')
            if name in text_page:
                text_done = f'{name} {page_num + 1} - стр \n'
                break
        return text_done

def func_writeToDoneText():
    list_of_names = []
    with open('ListOfNames.txt', encoding='utf-8') as list_names:
        list_of_names = list_names.readlines()
    list_names.close()

    with open('AgroBookNamesDone.txt', 'w') as ff:
        for name in list_of_names:
            if name != 'None \n':
            text = func_pdfChecker(name.strip())
            ff.write(text)
            print(text)
    ff.close()
