import re

class Helpers:


    def nbCas_per_loc(text):
        textArr = re.split(',',text)
        notAllowed = [",","à","aux","",";"]
        textArr = [i.strip().replace('.','') for i in textArr if i not in notAllowed]
        nbCas = textArr[0].split(" ")[0]
        regions = textArr[1:]
        myDict = {}
        for r in regions:
            myDict[r]= nbCas
        myDict[textArr[0].split(" ")[-1]] = nbCas
        return myDict

    # text = "01 à reubeuss, fann residence, lib 6, ouest foire."

    # dico = nbCas_per_loc(text)

    # print(dico)