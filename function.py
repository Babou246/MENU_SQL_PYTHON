
import mysql.connector as ps

print("""
            ######### #   ##   ######  ##    ##  ##       #  #######  ##    ##  ##     #  #######
            ###        #  ##   ##      ###   ##   ##     #   ##       ###   ##  ##     #  ##
            ######### #   ##   #####   ## #  ##    ##   #    ######   ## #  ##  ##     #  #####      
            ###        #  ##   ##      ##  # ##     ## #     ##       ##  # ##  ##     #  ##
            ###########   ##   ######  ##   ###      ##      #######  ##   ###  ########  #######
    """)
config = {
        'host':'localhost',
        'user':'root',
        'database':'base_exo',
        'password':'passer'
    }


db = ps.connect(**config)
curseur = db.cursor()




dic = {

        1 : "Lister les tous les agences",
        2 : "Lister tous les caissiers par ordre croissant de leur nom",
        3 :"Lister tous chef d’agence ainsi que le nom de l’agence",
        4 :"Lister les comptes de transaction de l’agence Plateau par ordre croissant du solde",
        5 :"Lister la somme des montants déposés par un caissier dans un compte de transaction de l’agence dont le chef est moussa dop par ordre croissant du montant",
        6 :"Lister les utilisateurs de l’agence Plateau",
        7 :"Lister le nombre de compte par agence",
        8 :"Lister les comptes affectés à l’utilisateur moussa diop durant le mois de Mai 2021",
        9 :"Lister les utilisateurs à qui on a affecté le compte numéro 001 durant année 2021",
        10:"Lister le montant des transactions effectué par utilisateur et par date dans l’agence dont le numéro est 001",
        11: "Lister le nombre d’affectation par utilisateur et numéro de compte durant le premier trimestre de l’année 2021 par ordre croissant de ce nombre d’affectation dans l’agence dont le numéro est 001",
        12: "Lister les dépôts effectués et les retraits par jour dans l’agence dont le chef est moussa diop par ordre croissant du montant",
        13: "Lister les montants de transactions et les frais associés effectués par l’utilisateur Assane Faye dans l’agence dont le chef est moussa diop .",
        14: "Lister la somme des parts de l’agence, de l'état et de l’état des transactions par date dans l’agence dont le numéro est 001.",
        15: "Lister la somme des parts de l’agence et de l'état par agence durant deuxième de l’année 2021",
        16: "Lister l’agence qui a fait le plus de transfert durant le mois de Juin 2021",
        17: "Lister l’agence qui a fait le moins de transfert de dépôt le 10-08-2021",
        18: "Lister l’agence qui a fait le retrait le plus grand durant le mois de MAI 221",
        19: "Lister les agences qui n’ont pas fait de dépôt le 10-08-2021",
        20: "Lister les noms utilisés par l’agence numéro 001 durant le mois de MAI 221",
        21: "Lister le ou les clients qui ont effectué le dépôt le plus petit durant le mois de MAI 2021",
        22: "Lister le ou les clients qui ont effectué le plus de dépôt durant le mois de MAI 221",
        23: "Lister les 5 agences qui ont effectué le plus de transactions durant l’année 2021",
        24: "Lister les 5 agences dont le montant gagné (somme des frais gagnés sur les transactions) sont les plus faibles en 2021.",
        25: "Lister l’utilisateur qui fait le plus de transfert dans l’agence dont le chef est moussa diop"

    }

def choix(dic):
    print("========================================= MENU =================================================\n")
    for key,values in enumerate(dic.values()):
        print(key+1,'->',values)

def choice_1_():
    
    print("=======================================LES AGENCES SONT :=====================================\n")

    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT adresse_AGENCE FROM AGENCE\n"
    curseur.execute(query)
    result = curseur.fetchall()
    for element in result:
        print(element[0])

def choice_2_():
    print("""
                ################## les caissiers par ordre croissant de leur nom ##############
    """)
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT nom_USER FROM USERS WHERE id_PROFIL_PROFIL = 3 ORDER BY nom_USER DESC\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element[0])

def choice_3_():
    print("""
                ######################### chef d’agence ainsi que le nom de l’agence #####################
    """)
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT nom_USER,adresse_AGENCE FROM `USERS`,`AGENCE` WHERE id_PROFIL_PROFIL = 1\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        space = '   '
        print(element[0],space,element[1])


    def choice_4_():
        print("""
            ###################### les comptes de transaction de l’agence Plateau par ordre croissant du solde #############
        """)
        db = ps.connect(**config)
        curseur = db.cursor()
        query = "SELECT * FROM `COMPTE_TRANSACTION` ORDER BY solde_COMPTE_TRANSACTION ASC;\n"
        curseur.execute(query)
        resultats = curseur.fetchall()
        for element in resultats:
            print(element[0],' ',element[1],' ',element[2])

    def choice_5_():
        db = ps.connect(**config)
        curseur = db.cursor()
        query = "SELECT num_TRANSACTION,montant_TRANSACTION FROM `TRANSACTIONS` WHERE numero_AGENCE_AGENCE = 3 ;\n"
        curseur.execute(query)
        resultats = curseur.fetchall()
        for element in resultats:
            print(element)

    def choice_6_():
        db = ps.connect(**config)
        curseur = db.cursor()
        query = "SELECT nom_USER,id_USER_USER FROM `USERS`,`AGENCE`;\n"
        curseur.execute(query)
        resultats = curseur.fetchall()
        for element in resultats:
            print(element[0],'  ',element[1])

    def choice_7_():
        pass
    def choice_8_():
        pass
    def choice_9_():
        pass


def choice_4_():
    print("""
        ###################### les comptes de transaction de l’agence Plateau par ordre croissant du solde #############
    """)
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT * FROM `COMPTE_TRANSACTION` ORDER BY solde_COMPTE_TRANSACTION ASC;\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element[0],' ',element[1],' ',element[2])

def choice_5_():
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT num_TRANSACTION,montant_TRANSACTION FROM `TRANSACTIONS` WHERE numero_AGENCE_AGENCE = 3 ;\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element)

def choice_6_():
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT nom_USER,id_USER_USER FROM `USERS`,`AGENCE`;\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element[0],'  ',element[1])

def choice_7_():
    pass
def choice_8_():
    pass
def choice_9_():
    pass



def choice_10_():
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT montant_TRANSACTION,date_TRANSACTION,numero_AGENCE_AGENCE FROM `TRANSACTIONS` WHERE numero_AGENCE_AGENCE = 1;\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element)


def choice_11_():

    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT count(numero_COMPTE_TRANSACTION) as nombre_affectation FROM `TRANSACTIONS` WHERE numero_AGENCE_AGENCE = 1;\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print('Le nombre d\'affectations est de :',element[0])

def choice_12_():
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT montant_TRANSACTION,num_DEPOTouRETRAIT  FROM `TRANSACTIONS` where numero_AGENCE_AGENCE = 3 ORDER BY montant_TRANSACTION ASC;\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element)
    
def choice_13_():
    print("""
    ################## les montants de transactions et les frais associés effectués par l’utilisateur Assane Faye ##############
    """)
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT montant_TRANSACTION,frais_TRANSACTION, nom_USER FROM `TRANSACTIONS`, `USERS` WHERE TRANSACTIONS.numero_AGENCE_AGENCE = 7 AND nom_USER = 'Winton';\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element[0],'  ',element[1],'  ',element[2])
   
def choice_14_():
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element)

def choice_15_():
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element)

def choice_16_():
    print("""
        ###################### les comptes de transaction de l’agence Plateau par ordre croissant du solde #############
    """)
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT * FROM `COMPTE_TRANSACTION` ORDER BY solde_COMPTE_TRANSACTION ASC;\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element[0],' ',element[1],' ',element[2])

def choice_17_():
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT num_TRANSACTION,montant_TRANSACTION FROM `TRANSACTIONS` WHERE numero_AGENCE_AGENCE = 3 ;\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element)

def choice_18_():
    db = ps.connect(**config)
    curseur = db.cursor()
    query = "SELECT nom_USER,id_USER_USER FROM `USERS`,`AGENCE`;\n"
    curseur.execute(query)
    resultats = curseur.fetchall()
    for element in resultats:
        print(element[0],'  ',element[1])

def choice_19_():
    pass
def choice_20_():
    pass
def choice_21_():
    pass
def choice_22_():
    pass
def choice_23_():
    pass