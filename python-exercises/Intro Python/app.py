from name_generator import NameGenerator

def get_user_input(prompt):
    user_input = input(prompt)
    return user_input.strip().lower()

def game_loop():
    name_generator = NameGenerator()

    while True:
        name = get_user_input("Enter your name: ")
        if name == "exit":
            break

        month_of_birth = get_user_input("Enter your month of birth: ")
        if month_of_birth == "exit":
            break

        name_type = get_user_input("Enter 'dragon' for dragon name or 'penguin' for penguin name: ")
        if name_type == "exit":
            break

        if name_type == "dragon":
            new_name = name_generator.dragon_name(name, month_of_birth)
        elif name_type == "penguin":
            new_name = name_generator.penguin_name(name, month_of_birth)
        else:
            print("Invalid name type. Please try again.")
            continue

        print("Your new name is:", new_name)
        print()

if __name__ == "__main__":
    game_loop()
