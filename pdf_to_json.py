from pdf2image import convert_from_path
import os,json,time
import pytesseract as tess
from PIL import Image

PDF_file_1 = "Test.pdf"  
path = os.path.abspath(PDF_file_1)

image_file_list = []

tess.pytesseract.tesseract_cmd = r'C:\Users\Mapple\AppData\Local\Tesseract-OCR\tesseract.exe'
images = convert_from_path(path, 500,poppler_path=r'C:\Program Files\poppler-0.68.0\bin')

for i, image in enumerate(images):
    fname = 'image'+str(i)+'.png'

    created_date =  "%s" % time.ctime(os.path.getctime(fname))
 
    image.save(fname, "PNG")
    image_file_list.append(fname)

    with open(fname, "a",encoding="utf8") as output_file:
        for image_file in image_file_list:
            text = str(((tess.image_to_string(Image.open(image_file)))))
            text = text.replace("-\n", "")
       
            data= []
       
            data.append({'Date':created_date,'Title':PDF_file_1,'Content':text})
            with open('test.json','w',encoding="utf8") as f:
                json.dump(data, f,ensure_ascii=False,indent=4)

