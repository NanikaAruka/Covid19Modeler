import os
import pdfplumber


covid='covidFile1.pdf'
os.system(f'ocrmypdf {covid} output.pdf')

with pdfplumber.open('output.pdf') as pdf:
    page = pdf.pages[0]
    text = page.extract_text(x_tolerance=2)
    print(text)
