def add_element(shooting_list: list) -> None:
    shooting_list.append(input("Entrer le nom d'un élément à ajouter à la liste de courses : "))
    print(f"L'élément {shooting_list[-1]} a bien été ajouté à la liste.")

def remove_element(shooting_list: list) -> None:
    element = input("Entrer le nom d'un élément à retirer de la liste de courses : ")
    try:
        shooting_list.remove(element)
        print(f"L'élément {element} a bien été supprimé de la liste.")
    except ValueError:
        print(f"L'élément {element} n'est pas dans la liste.")

def print_list(shooting_list: list) -> None:
    for i, element in enumerate(shooting_list):
        print(f"{i+1}. {element}")

def clear_list(shooting_list: list) -> None:
    shooting_list.clear()
    print("La liste a été vider de son contenu")

# ----------------------------------------------------------------------

MENU = """\nChoisssez parmi les 5 options suivantes:
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter"""

shooting_list: list = []
while True:
    print(MENU)
    choice = input(">> Votre choix : ")
    if choice == "1":
        add_element(shooting_list)
    elif choice == "2":
       remove_element(shooting_list)
    elif choice == "3":
        print_list(shooting_list)
    elif choice == "4":
        clear_list(shooting_list)
    elif choice == "5":
        print("A bientôt !")
        break

    print("-"*50)
