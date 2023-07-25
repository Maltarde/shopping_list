class ShoppingList:
    def __init__(self) -> None:
        self.list = [] 

    def add(self) -> None:
        self.list.append(input("Entrer le nom d'un élément à ajouter à la liste de courses : "))
        print(f"L'élément {self.list[-1]} a bien été ajouté à la liste.")

    def remove(self) -> None:
        element = input("Entrer le nom d'un élément à retirer de la liste de courses : ")
        try:
            self.list.remove(element)
            print(f"L'élément {element} a bien été supprimé de la liste.")
        except ValueError:
            print(f"L'élément {element} n'est pas dans la liste.")

    def print(self) -> None:
        for i, element in enumerate(self.list):
            print(f"{i+1}. {element}")

    def clear(self) -> None:
        self.list.clear()
        print("La liste a été vider de son contenu")

# ----------------------------------------------------------------------

MENU = """\nChoisssez parmi les 5 options suivantes:
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Quitter"""

shoopping_list: ShoppingList = ShoppingList()
while True:
    print(MENU)
    choice = input(">> Votre choix : ")
    if choice == "1":
        shoopping_list.add()
    elif choice == "2":
       shoopping_list.remove()
    elif choice == "3":
        shoopping_list.print()
    elif choice == "4":
        shoopping_list.clear()
    elif choice == "5":
        print("A bientôt !")
        break

    print("-"*50)
