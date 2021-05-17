import json
import pymysql
import easygui


def validate_string(val):
    if val is not None:
        if type(val) is int:
            # for x in val:
            #   print(x)
            return str(val).encode('utf-8')
        else:
            return val


def insert_data():
    # open the explorer so the user can select the desired file
    file = easygui.fileopenbox()
    json_data = open(file).read()
    json_obj = json.loads(json_data)

    # connect to MySQL
    con = pymysql.connect(host='localhost', user='root', passwd='', db='testjson')
    cursor = con.cursor()

    for i, item in enumerate(json_obj):
        person = validate_string(item.get("person", None))
        year = validate_string(item.get("year", None))
        company = validate_string(item.get("company", None))

        cursor.execute("INSERT INTO testp (person,	year,	company) VALUES (%s,	%s,	%s)",
                       (person, year, company))
    con.commit()
    con.close()


def choices():
    print("Insetion base de données")
    print("1 - Afficher les données")
    print("2 - Insertion des données")
    print("3 - Fermer l'interface")


def view_data():
    file = easygui.fileopenbox()
    with open(file, "r") as f:
        temp = json.load(f)
        for entry in temp:
            person = entry["person"]
            year = entry["year"]
            company = entry["company"]
            print(f"le nom : {person}")
            print(f"l annee : {year}")
            print(f"la compagnie : {company}")
            print("\n\n")


while True:
    choices()
    choice = input("entrez un numero :")
    if choice == "1":
        view_data()
    elif choice == "2":
        insert_data()
    elif choice == "3":
        break
    else:
        print("Erreur")
