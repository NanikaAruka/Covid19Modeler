from glob import glob
from PIL import Image
from os import path
import json
import pytesseract
import easyocr
import cv2
import numpy as np
from pdf2image import convert_from_path
# import PyPDF2 as pdf_ocr
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
    name = file.split("/")[-1].split(".")[0]
    print(name)
    try:
        pages = convert_from_path(file, 500)
        k = 1;
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

def extract_cas_from_locality(filee, reader):
    result = reader.readtext(filee, detail = 0, paragraph=True)
    k= 1
    text_cas = []
    for line in result:
        # print(f"{k} : {line}\n\n")
        if(k == 5):
            text_cas.append(line)
        elif(k > 5):
            return text_cas
        k+=1

def locality_from_text(text_cas):
    i = 0
    # if(len(text_cas) > 0): i = 1
    split_text = text_cas[i].split()
    k = 0
    cpt = 0
    tab = []
    for i in split_text:
        tmp = {}
        if(i.isdigit()):
            tmp[i] = []
            first = True
            #print(i)
            #print(split_text[k+1:])
            for j in split_text[k+1:]:
                if(j.isdigit()):
                    break
                if(j not in ["à", "et", "aux","au", "dont", "cas"]):
                    tmp[i].append(j)
                   
               
            tab.append(tmp)
        else:
            pass
        k+=1
    return tab

'''
    Récupérer la position d'une chaine de caractères
'''
def get_value_from_index(line, index):
    if(len(line) >= index):
        return int([int(s) for s in line[index].split(" ") if s.isdecimal()][0])
    else: return 'pas pris'


def ocr_from_pdf(location,reader, extension="*"):
    files_paths = sorted(glob(path.join(location, "*")))
    for file in files_paths:
        convert_all_pdf_to_image(file)
        name = file.split("/")[-1].split(".")[0]
        ocr_from_img("../source/img/{0}.jpg".format(name), reader)



def ocr_from_img(file, reader):
    print(file)
    data = {}
    extracted_text = []
    # print("i'm in the function")
    # files_paths = sorted(glob(path.join(location, extension)))
   
    # print(files_paths)
    # for file in files_paths:
    result = reader.readtext(file, detail = 0, paragraph=True)
    # print(result)
    for line in result:
        # print(line+"\n\n")
        if(line.startswith("Ce")):
            infos = line.split(",")
            data['date'] = " ".join(infos[0].split(" ")[1:])
            data['nombreDeTest'] = get_value_from_index(infos, 1)
            data['positifs'] = get_value_from_index(infos, 2)
            tmp = line.split(" ")
            taux = tmp[tmp.index("positivité") + 2]
            data['tauxPositifs'] = taux.replace(".","")
            data["cas_contact"] = tmp[tmp.index("contacts") - 2] if tmp[tmp.index("contacts") - 2].isdigit() else 0
            data["cas_importe"] = tmp[tmp.index("enregistré") - 3] if tmp[tmp.index("enregistré") - 3].isdigit() else 0
            data["cas_communautaire"] = tmp[tmp.index("issus") - 2] if tmp[tmp.index("issus") - 2].isdigit() else 0
            name_output_file = "".join(infos[0].split(" ")[1:])
            file_output = open('../data/{0}.json'.format(name_output_file), "w+")
            extracted_text.append(" ".join(tmp[tmp.index("dont"): len(tmp) - 6]))
            print(extracted_text)
            localities = locality_from_text(extracted_text)
            data['localities'] = localities
            # localities_output = open('../localities/{0}.json'.format(name_output_file), "w+")

            try:
                json.dump(data, file_output, indent=4, ensure_ascii=False)
                # json.dump(localities, localities_output, indent=4, )
                name = file.split("/")[-1].split(".")[0]
                shutil.move(file, f"../archives/{name}.jpg")
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
 
 

if _name_ == '_main_':
   ocr()