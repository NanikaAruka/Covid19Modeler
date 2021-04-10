import json
import pymysql


file = "C:/Users/Main/MERN/test.json"
json_data = open(file).read()
json_obj = json.loads(json_data)



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

    cursor.execute("INSERT INTO testp (person,	year,	company) VALUES (%s,	%s,	%s)", (person, year, company))
con.commit()
con.close()
