# Main code for pokedex user input
while True:
    user_input = input("\nWhat would you like to do?\n1. Search for all Pokémon\n2. Search for a specific Pokémon\n3. Search for Pokémon from a specific generation\n4. Search for a Pokémon from a specific Region\n5. Search for Pokémon with a specefic Evolution Stage\n6. Search for Pokémon with a specific Regional Form\n7. Exit\n")
    if user_input == "1":
        # Search for all Pokémon
    elif user_input == "2":
        # Search for a specific Pokémon
    elif user_input == "3":
        # Search for Pokémon from a specific generation
    elif user_input == "4":
        # Search for Pokémon from a specific Region
    elif user_input == "5":
        # Search for Pokémon with a specific Evolution Stage
    elif user_input == "6":
        # Search for Pokémon with a specific Regional Form
    elif user_input == "7":
        # Exit the program
        print("Goodbye!")
        break
    else:
        # Invalid input handling
        print("Invalid option. Please try again.\n")
        
