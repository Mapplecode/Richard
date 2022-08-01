import json,os
import PyPDF2

pdf_file_name= 'Test.pdf'
pdf_path = os.path.abspath(pdf_file_name)
pdfFileObj = open(pdf_path, 'rb')
emp_list = list()
search_text = 'казачество'
text = ["январ","феврал","март","апрел","май","июн","июл","авгус","сентябр","октябр","ноябр","декабр"]
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
# print(pdfReader.numPages)
pageObj = pdfReader.getPage(0)
store = pageObj.extractText()
get_len = store[:350]
dt = ''
if search_text in store:
    for i in text:
        if i in get_len:
            index = get_len.index(i)
            

            date = get_len[index-3:index+13]
            
            dt+=date
            break
        else:
            pass
    emp_list.append({'Date':dt,'Title':pdf_file_name,'Content':store})
    pdfFileObj.close()

    with open('store.json','w',encoding="utf8")as f:
        json.dump(emp_list,f,ensure_ascii=False,indent=4)
else:
    print("It doesn't match any record.")








