from pet import Pet, CuddlyPet
from toy import Toy
from treat import Treat, ColdPizza, Bacon, VeganSnack
from menu import Menu

# Begin with no pets.
pets = []

main_menu = [   
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Give a toy to your pets",
    "Give a treat to your pets",
    "Do nothing",
]

adoption_menu = [
    "Pet",
    "Cuddly Pet"
]

treat_menu = [
    "Cold Pizza",
    "Bacon",
    "VeganSnack"
]

def main():
    main = Menu("Please choose an option:", main_menu)
    type = Menu("Please choose the type of pet:", adoption_menu)
    treat = Menu("Please choose the type of treat:", treat_menu)
    while True:
        choice = main.get_choice()
        if choice == 1:
            pet_name = input("What would you like to name your pet? ")
            type_choice = type.get_user_choice()
            if type_choice == 1:
                pets.append(Pet(pet_name))
            elif type_choice == 2:
                pets.append(CuddlyPet(pet_name))
            print("You now have %d pets" % len(pets))
        if choice == 2:
            for pet in pets:
                pet.get_love()
            print("Pets have been loved!")
        if choice == 3:
            for pet in pets:
                pet.eat_food()
            print("Pets have been fed!")
        if choice == 4:
            for pet in pets:
                print(pet)
        if choice == 5:
            for pet in pets:
                pet.get_toy(Toy())
            print("Pets got a toy!")
        if choice == 6:
            treat_choice = treat.get_user_choice()
            if treat_choice == 1:
                treat_type = ColdPizza()
            if treat_choice == 2:
                treat_type = Bacon()
            if treat_choice == 3:
                treat_type = VeganSnack
            for pet in pets:
                pet.get_treat(treat_type)
            print("Pets got a treat!")
        if choice == 7:
            for pet in pets:
                pet.be_alive()
            print("Pets did nothing!")
main()
