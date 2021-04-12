import json
import pymysql
from tkinter import *

file = "C:/Users/Main/MERN/test.json"
json_data = open(file).read()
json_obj = json.loads(json_data)

OPTIONS = [
    "2013",
    "2014",
    "2017"
]  

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0])  # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()


def ok():
    print("value is:" + variable.get())


button = Button(master, text="OK", command=ok)
button.pack()


def validate_string(val):
    if val is not None:
        if type(val) is int:
            # for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


# connect to MySQL
con = pymysql.connect(host='localhost', user='root', passwd='', db='testjson')
cursor = con.cursor()

for i, item in enumerate(json_obj):
    person = validate_string(item.get("person", None))
    year = validate_string(item.get("year", None))
    company = validate_string(item.get("company", None))


    cursor.execute("INSERT INTO testp (person,	year,	company) VALUES (%s,	%s,	%s) WHERE year= "+variable.get(),
                   (person, year, company))
con.commit()
con.close()
mainloop()
