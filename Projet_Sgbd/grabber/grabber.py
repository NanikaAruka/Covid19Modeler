from glob import glob
from PIL import Image
from os import path
import json
import pytesseract
import easyocr
import cv2
import numpy as np
from pdf2image import convert_from_path
import PyPDF2 as pdf_ocr
import argparse
import shutil

'''
    Fusionner deux images quand on a un fichier avec deux pages on convertit chaque page en image et
    on fusionne les deux images en une seule image
'''
def merge_pdf(img1, img2):
    return cv2.vconcat([img1,img2])

'''
    Puisque les fichier pdf sont des images qui sont colées sur le fichier ce qui empêche d'extraire les informations
    donc on convertit le fichier pdf en image
'''
def convert_all_pdf_to_image(file, extension="*"):
    # files_path = sorted(glob(path.join(location, extension)))
    # print(files_path)
    # if(files_path):
    # for file in files_path:
    name = file.split("/")[-1].split(".")[0]
    print(name)
    try:
        pages = convert_from_path(file, 500)
        print("nombre de pages " + pages)
        k = 1
        if(len(pages) == 2):
            open_cv_image1 = np.array(pages[0]) 
            # Convert RGB to BGR 
            open_cv_image1 = open_cv_image1[:, :, ::-1].copy()
            open_cv_image2 = np.array(pages[1]) 
            # Convert RGB to BGR 
            open_cv_image2 = open_cv_image2[:, :, ::-1].copy()
            img = merge_pdf(open_cv_image1, open_cv_image2)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            im_pil = Image.fromarray(img)
            im_pil.save("../source/img/{0}.jpg".format(name), 'JPEG')
        else:
            pages[0].save("../source/img/{0}.jpg".format(name), 'JPEG')
    except print(0):
        print("Error lors de la conversion de "+name)
            


'''
    Récupérer la position d'une chaine de caractères
'''
def get_value_from_index(line, index):
    return int([int(s) for s in line[index].split(" ") if s.isdecimal()][0])


def ocr_from_pdf(location,reader, extension="*"):
    convert_all_pdf_to_image(location)
    ocr_from_img("../source/img", reader)


def ocr_from_img(file, reader):
    data = {}
    # print("i'm in the function")
    # files_paths = sorted(glob(path.join(location, extension)))
   
    # print(files_paths)
    # for file in files_paths:
    result = reader.readtext(file, detail = 0, paragraph=True)
    print(result)
    for line in result:
        print(line+"\n\n")
        if(line.startswith("Ce")):
            infos = line.split(",")
            data['date'] = " ".join(infos[0].split(" ")[1:])
            data['nombreDeTest'] = get_value_from_index(infos, 1)
            data['positifs'] = get_value_from_index(infos, 2)
            tmp = line.split(" ")
            # print(tmp)
            taux = tmp[tmp.index("positivité") + 2]
            data['tauxPositifs'] = taux.replace(".","")
            data["cas_contact"] = tmp[tmp.index("contacts") - 2] if tmp[tmp.index("contacts") - 2].isdigit() else 0
            data["cas_importe"] = tmp[tmp.index("enregistré") - 3] if tmp[tmp.index("enregistré") - 3].isdigit() else 0
            data["cas_communautaire"] = tmp[tmp.index("issus") - 2] if tmp[tmp.index("issus") - 2].isdigit() else 0
            name_output_file = "".join(infos[0].split(" ")[1:])
            file_output = open('../data/{0}.json'.format(name_output_file), "w+")
            try:
                json.dump(data, file_output, indent=4)
                shutil.move(file, f"../archives")
            finally :
                file_output.close()
            pass
        

def ocr():
    reader = easyocr.Reader(['fr'])
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", '--type', type=str, required=True, help="Définissez le type que vous voulez (image ou pdf)")
    args = parser.parse_args()
    if(args.type.lower() == "image"):
        location = "../source/img"
        files_paths = sorted(glob(path.join(location, "*")))
        for file in files_paths:
            ocr_from_img(file, reader)
    elif(args.type.lower() == "pdf"):
        location = "../source/file"
        ocr_from_pdf(location, reader)
    else:
        print("Type de fichier non pris en compte")
 
 

if __name__ == '__main__':
    # ocr()
    convert_all_pdf_to_image('../source/file/covidFile1.pdf')
    