from file import *

c ='Y'
while c == 'Y' or c == 'y' or c == 'yes':
    print("""
        1 - Afficher le menu proposant un choix sur l’ensemble des requêtes (1 à 25)
        2 - Menu Principal excepté des requetes déjà choisies
        3 - Taper (E ou e) pour afficher les requêtes déjà choisi pour les ré exécuter
        4 - Taper (R ou r) pour réafficher tout le menu (exécuter ou non)

    """)
    affiche = (input("TAPER 1,2,3,4 pour choisir l'option à faire\n"))
    dico = dic.copy()
    dictionnaire = {}
    if affiche == '1':
        
        c='y'
        while c == 'y' or c=='Y':
            choix(dic)
            choice = int(input("Faire le choix dans le menu afficher ci-dessus\n"))

            dictionnaire.setdefault(choice,dico[choice])
            del dico[choice]
            # print("La nouvelle dictionnaire :")
            # print(dictionnaire)
            if choice == 1:
                choice_1_()

            elif choice == 2:
                choice_2_()

            elif choice == 3:
                choice_3_()

            elif choice == 4:
                choice_4_()
            elif choice == 5:
                choice_5_()

            elif choice == 6:
                choice_6_()

            elif choice == 7:
                choice_7_()  

            elif choice == 8:
                choice_8_()

            elif choice == 9:
                choice_9_()

            elif choice == 10:
                choice_10_()

            elif choice == 11:
                choice_11_()
            elif choice == 12:
                choice_12_()

            elif choice == 13:
                choice_13_()

            elif choice == 15:
                choice_14_()  

            elif choice == 16:
                choice_16_()

            elif choice == 17:
                choice_17_()
            elif choice == 18:
                choice_18_()

            elif choice == 19:
                choice_19_()

            elif choice == 20:
                choice_20_()  

            elif choice == 21:
                choice_21_()
            elif choice == 22:
                choice_22_()

            elif choice == 23:
                choice_23_()
             
            c = input('Continuer (Y/N) avec le menu ?:\n')
    
    elif affiche == '2':
        try:
            print("""
                ########################### REQUETES DÉJÀ EXECUTÉES ####################################
            """)
            dico = dic.copy()
            dictionnaire = {}
            dictionnaire.setdefault(choice,dico[choice])
            # print(dictionnaire)
            del dico[choice]
            for element in dico.items():
                print(element)
        except Exception as e:
            print("Vous n'avez pas encore rien fait comme réquetes")
        
    elif affiche == 'E' or affiche == 'e':
        print('============================ REQUETES DÉJÀ VUES ================================')
        for key,values in enumerate(dictionnaire.values()):
            print('->',values)
        choice_ = int(input('choisir le requete à réexecuter\n'))
        n = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
        if choice_ in n:
            
            if choice_ == 1:
                choice_1_()

            elif choice_ == 2:
                choice_2_()

            elif choice_ == 3:
                choice_3_()

            elif choice_ == 4:
                choice_4_()
            elif choice_ == 5:
                choice_5_()

            elif choice_ == 6:
                choice_6_()

            elif choice_ == 7:
                choice_7_()  

            elif choice_ == 8:
                choice_8_()

            elif choice_ == 9:
                choice_9_()

            elif choice_ == 10:
                choice_10_()

            elif choice_ == 11:
                choice_11_()
            elif choice_ == 12:
                choice_12_()

            elif choice_ == 13:
                choice_13_()

            elif choice_ == 15:
                choice_14_()  


    elif affiche == 'R' or affiche == 'r':
        print("""
                    ##################### MENU PRINCIPALE ######################## 
        """)
        choix(dic)
    
    c = input("Taper (Y|y) pour revenir au menu principal sino quitter\n")

# print("La nouvelle dictionnaire :")
# print(dictionnaire)