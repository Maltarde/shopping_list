import json
import logging


logging.basicConfig(level=logging.DEBUG,
                    filename="list.log",
                    filemode="w",
                    format="%(asctime)s - %(levelname)s - %(message)s")


class ShoppingList:
    """Shopping list gestoin class"""
    def __init__(self) -> None:
        try:
            logging.debug(f"Create a new list with a file")
            self.list: list = self._read()
        except FileNotFoundError:            
            logging.debug(f"Create a new empty list")
            self.list: list = []

    def __str__(self) -> str:
        logging.debug(f"Display the list")
        list = [f"{i+1}. {element}" for i, element in enumerate(self.list)]
        return "\n".join(list)

    def add(self) -> None:
        """Add an item to the list"""
        logging.debug(f"Add a new element")
        self.list.append(input("Entrer le nom d'un élément à ajouter à la liste de courses : "))
        print(f"L'élément {self.list[-1]} a bien été ajouté à la liste.")

    def remove(self) -> None:
        """Remove a given element from the list"""
        element = input("Entrer le nom d'un élément à retirer de la liste de courses : ")
        logging.debug(f"Remove {element} element")
        try:
            self.list.remove(element)
            print(f"L'élément {element} a bien été supprimé de la liste.")
        except ValueError:
            print(f"L'élément {element} n'est pas dans la liste.")

    def clear(self) -> None:
        """Empty the list"""
        logging.debug(f"Clear list")
        self.list.clear()
        print("La liste a été vider de son contenu")

    def save(self) -> None:
        """Save the list to a 'list.json' file"""
        logging.debug(f"save the list in the file list.json")
        with open("list.json", "w") as f:
            json.dump(self.list, f, indent=4)
            print("La liste a bien été enregistrée")

    def _read(self) -> list:
        logging.debug(f"Read the list in the file list.json")
        """Get the list in the 'list.json' file"""
        with open("list.json", "r") as f:
            return json.load(f)

# ----------------------------------------------------------------------

MENU = """\nChoisssez parmi les 5 options suivantes:
1: Ajouter un élément à la liste
2: Retirer un élément de la liste
3: Afficher la liste
4: Vider la liste
5: Enregistrer la liste
6: Quitter"""

shoopping_list: ShoppingList = ShoppingList()
while True:
    print(MENU)
    choice = input(">> Votre choix : ")
    logging.debug(f"Choose user: {choice}")
    if choice == "1":
        shoopping_list.add()
    elif choice == "2":
       shoopping_list.remove()
    elif choice == "3":
        print(shoopping_list)
    elif choice == "4":
        shoopping_list.clear()
    elif choice == "5":
        shoopping_list.save()
    elif choice == "6":
        logging.debug(f"End of program")
        print("A bientôt !")
        break

    print("-"*50)
