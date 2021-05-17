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
        date = validate_string(item.get("date", None))
        nombreDeTest = validate_string(item.get("nombreDeTest", None))
        positifs = validate_string(item.get("positifs", None))
        tauxPositifs = validate_string(item.get("tauxPositifs", None))
        cas_contact = validate_string(item.get("cas_contact", None))
        cas_communautaire = validate_string(item.get("cas_communautaire", None))

        cursor.execute("INSERT INTO testp (date, nombreDeTest,	positifs, tauxPositifs, cas_contact, "
                       "cas_communautaire) VALUES (%s,	%s,	%s,	%s,	%s,	%s )",
                       (date, nombreDeTest, positifs, tauxPositifs, cas_contact, cas_communautaire))
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
            date = entry["date"]
            nombreDeTest = entry["nombreDeTest"]
            positifs = entry["positifs"]
            tauxPositifs = entry["tauxPositifs"]
            cas_contact = entry["cas_contact"]
            cas_communautaire = entry["cas_communautaire"]
            print(f"La date : {date}")
            print(f"Le nombres de tests : {nombreDeTest}")
            print(f"Le nombre de tests positifs : {positifs}")
            print(f"Le taux de positivité : {tauxPositifs}")
            print(f"Le nombre de cas contacts : {cas_contact}")
            print(f"Le nombre de cas communautaires : {cas_communautaire}")
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
