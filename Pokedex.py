# docstring - Luke Thompson - Pokemon database application - Pokedex
# imports
import sqlite3

# constants and variables
DATABASE = "pokedex.db"

# functions


def print_all_pokemon():
    """Print all Pokémon in the database"""
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    # search for all pokemon
    sql = ("SELECT "
           "pokedex_number, "
           "pokemon, "
           "Pokedex.generation, "
           "Generation.region, "
           "Evolution_Stage.evolution_stage, "
           "GROUP_CONCAT ( "
           "DISTINCT Typing.typing "
           "ORDER BY "
           "Typing.typing_id) "
           "FROM Pokedex "
           "JOIN Typing_ID ON Pokedex.pokedex_id = "
           "Typing_ID.pokedex_id "
           "JOIN Typing ON Typing_ID.typing_id = "
           "Typing.typing_id "
           "JOIN Evolution_Stage ON Pokedex.evolution_stage_id = "
           "Evolution_Stage.evolution_stage_id "
           "JOIN Generation ON Pokedex.generation = "
           "Generation.generation "
           "GROUP BY Pokedex.pokedex_id;")
    cursor.execute(sql)
    results = cursor.fetchall()
    # print results neatly
    print(
        ("Pokedex Number | Pokemon | Generation | Region | "
         "Evolution Stage | Types")
    )
    for pokemon in results:
        print(
            f"{pokemon[0]:<14} | {pokemon[1]:<7} | {pokemon[2]:<10} | "
            f"{pokemon[3]:<6} | {pokemon[4]:<15} | {pokemon[5]:<5}"
        )
    db.close()


# Main code for pokedex user input
while True:
    # ask for user input
    user_input = input(
        "\nWhat would you like to do?\n "
        "1. Search for all Pokémon\n "
        "2. Search for a specific Pokémon\n "
        "3. Search for Pokémon from a specific generation\n "
        "4. Search for a Pokémon from a specific Region\n "
        "5. Search for Pokémon with a specefic Evolution Stage\n "
        "6. Search for Pokémon with a specific Regional Form\n "
        "7. Search for Pokémon with a specific typing\n "
        "8. Search for Pokémon with specific dual typings\n "
        "9. Exit\n "
    )
    if user_input == "1":
        # Search for all Pokémon
        print_all_pokemon()
    elif user_input == "2":
        # Search for a specific Pokémon
        pokemon_name = input("How would you like to search for a Pokémon?\n"
                             "1. By name\n"
                             "2. By Pokedex number\n")
        if pokemon_name == "1":
            # ask for name of pokemon
            name = input("Enter the name of the Pokémon: ")
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            # search for pokemon by name
            cursor.execute(
                "SELECT pokedex_number, "
                "pokemon, "
                "Pokedex.generation, "
                "Generation.region, "
                "Evolution_Stage.evolution_stage, "
                "GROUP_CONCAT("
                "DISTINCT Typing.typing "
                "ORDER BY Typing.typing_id) "
                "FROM Pokedex "
                "JOIN Typing_ID ON Pokedex.pokedex_id = "
                "Typing_ID.pokedex_id "
                "JOIN Typing ON Typing_ID.typing_id = "
                "Typing.typing_id "
                "JOIN Evolution_Stage ON Pokedex.evolution_stage_id = "
                "Evolution_Stage.evolution_stage_id "
                "JOIN Generation ON Pokedex.generation = "
                "Generation.generation "
                "WHERE pokemon LIKE ? "
                "GROUP BY Pokedex.pokedex_id",
                (f"%{name}%",)
            )
            results = cursor.fetchall()
            # print results neatly
            if results:
                print(
                    "Pokedex Number | Pokemon | Generation | Region | "
                    "Evolution Stage | Types"
                )
                for pokemon in results:
                    print(
                        f"{pokemon[0]:<14} | {pokemon[1]:<7} | "
                        f"{pokemon[2]:<10} | "
                        f"{pokemon[3]:<6} | {pokemon[4]:<15} | {pokemon[5]:<5}"
                    )
            else:
                # if no results print message
                print("No Pokémon found with that name.")
            db.close()
        elif pokemon_name == "2":
            # ask for number of pokemon
            number = input("Enter the Pokedex number of the Pokémon(1-1025): ")
            db = sqlite3.connect(DATABASE)
            cursor = db.cursor()
            # search for pokemon by number
            cursor.execute(
                "SELECT pokedex_number, pokemon, Pokedex.generation, "
                "Generation.region, Evolution_Stage.evolution_stage, "
                "GROUP_CONCAT("
                "DISTINCT Typing.typing "
                "ORDER BY Typing.typing_id) "
                "FROM Pokedex "
                "JOIN Typing_ID ON Pokedex.pokedex_id = "
                "Typing_ID.pokedex_id "
                "JOIN Typing ON Typing_ID.typing_id = Typing.typing_id "
                "JOIN Evolution_Stage ON Pokedex.evolution_stage_id = "
                "Evolution_Stage.evolution_stage_id "
                "JOIN Generation ON Pokedex.generation = "
                "Generation.generation "
                "WHERE pokedex_number = ? "
                "GROUP BY Pokedex.pokedex_id",
                (f"%{number}%",)
            )
            results = cursor.fetchall()
            if results:
                # print results neatly
                print(
                    "Pokedex Number | Pokemon | Generation | Region | "
                    "Evolution Stage | Types"
                )
                for pokemon in results:
                    print(
                        f"{pokemon[0]:<14} | {pokemon[1]:<7} | "
                        f"{pokemon[2]:<10} | "
                        f"{pokemon[3]:<6} | {pokemon[4]:<15} | {pokemon[5]:<5}"
                    )
            else:
                # if no results print message
                print("No Pokémon found with that number.")
            db.close()
        else:
            print("Invalid option. Please try again.\n")
    elif user_input == "3":
        # Search for Pokémon from a specific generation
        generation = input("Enter the generation number\n"
                           "1.Kanto\n"
                           "2.Johto\n"
                           "3.Hoenn\n"
                           "4.Sinnoh\n"
                           "5.Unova\n"
                           "6.Kalos\n"
                           "7.Alola\n"
                           "8.Galar\n"
                           "9.Hisui\n"
                           "10.Paldea\n"
                           )
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        # search for pokemon by generation
        cursor.execute(
            "SELECT pokedex_number, pokemon, Pokedex.generation, "
            "Generation.region, Evolution_Stage.evolution_stage, "
            "GROUP_CONCAT(DISTINCT Typing.typing ORDER BY Typing.typing_id) "
            "FROM Pokedex "
            "JOIN Typing_ID ON Pokedex.pokedex_id = Typing_ID.pokedex_id "
            "JOIN Typing ON Typing_ID.typing_id = Typing.typing_id "
            "JOIN Evolution_Stage ON Pokedex.evolution_stage_id = "
            "Evolution_Stage.evolution_stage_id "
            "JOIN Generation ON Pokedex.generation = Generation.generation "
            "WHERE Pokedex.generation = ? "
            "GROUP BY Pokedex.pokedex_id",
            (generation,)
        )
        results = cursor.fetchall()
        if results:
            # print results neatly
            print(
                "Pokedex Number | Pokemon | Generation | Region | "
                "Evolution Stage | Types"
            )
            for pokemon in results:
                print(
                    f"{pokemon[0]:<14} | {pokemon[1]:<7} | {pokemon[2]:<10} | "
                    f"{pokemon[3]:<6} | {pokemon[4]:<15} | {pokemon[5]:<5}"
                )
        else:
            # if no results print message
            print("That generation has no Pokémon.")
        db.close()
    elif user_input == "4":
        # Search for Pokémon from a specific Region
        region = input(
            "Enter the region (Kanto, Johto, Hoenn, Sinnoh, Unova, Kalos, "
            "Alola, Galar, Hisui, Paldea): "
        )
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        # search for pokemon by region
        cursor.execute(
            "SELECT pokedex_number, pokemon, Pokedex.generation, "
            "Generation.region, Evolution_Stage.evolution_stage, "
            "GROUP_CONCAT(DISTINCT Typing.typing ORDER BY Typing.typing_id) "
            "FROM Pokedex "
            "JOIN Typing_ID ON Pokedex.pokedex_id = Typing_ID.pokedex_id "
            "JOIN Typing ON Typing_ID.typing_id = Typing.typing_id "
            "JOIN Evolution_Stage ON Pokedex.evolution_stage_id = "
            "Evolution_Stage.evolution_stage_id "
            "JOIN Generation ON Pokedex.generation = Generation.generation "
            "WHERE Generation.region = ? "
            "GROUP BY Pokedex.pokedex_id",
            (region,)
        )
        results = cursor.fetchall()
        if results:
            # print results neatly
            print(
                "Pokedex Number | Pokemon | Generation | Region | "
                "Evolution Stage | Types"
            )
            for pokemon in results:
                print(
                    f"{pokemon[0]:<14} | {pokemon[1]:<7} | {pokemon[2]:<10} | "
                    f"{pokemon[3]:<6} | {pokemon[4]:<15} | {pokemon[5]:<5}"
                )
        else:
            # if no results print message
            print("That region has no Pokémon.")
        db.close()
    elif user_input == "5":
        # Search for Pokémon with a specific Evolution Stage
        evolution_stage = input(
            (
                "Enter the evolution stage (Unevolved, 1st Evolution, "
                "2nd Evolution): "
            )
        )
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        # search for pokemon by evolution stage
        cursor.execute(
            "SELECT pokedex_number, pokemon, Pokedex.generation, "
            "Generation.region, Evolution_Stage.evolution_stage, "
            "GROUP_CONCAT(DISTINCT Typing.typing ORDER BY Typing.typing_id) "
            "FROM Pokedex "
            "JOIN Typing_ID ON Pokedex.pokedex_id = "
            "Typing_ID.pokedex_id "
            "JOIN Typing ON Typing_ID.typing_id = "
            "Typing.typing_id "
            "JOIN Evolution_Stage ON Pokedex.evolution_stage_id = "
            "Evolution_Stage.evolution_stage_id "
            "JOIN Generation ON Pokedex.generation = "
            "Generation.generation "
            "WHERE Evolution_Stage.evolution_stage = ? "
            "GROUP BY Pokedex.pokedex_id",
            (evolution_stage,)
        )
        results = cursor.fetchall()
        if results:
            # print results neatly
            print(
                "Pokedex Number | Pokemon | Generation | Region | "
                "Evolution Stage | Types"
            )
            for pokemon in results:
                print(
                    f"{pokemon[0]:<14} | {pokemon[1]:<7} | {pokemon[2]:<10} | "
                    f"{pokemon[3]:<6} | {pokemon[4]:<15} | {pokemon[5]:<5}"
                )
        else:
            # if no results print message
            print("That is not a valid evolution stage.")
        db.close()
    elif user_input == "6":
        # Search for Pokémon with a specific Regional Form
        regional_form = input(
            "Enter the regional form (Galarian, Alolan, Hisuian): "
        )
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        # search for pokemon by regional form
        cursor.execute(
            "SELECT pokedex_number, pokemon, Pokedex.generation, "
            "Generation.region, Evolution_Stage.evolution_stage, "
            "GROUP_CONCAT(DISTINCT Typing.typing ORDER BY Typing.typing_id) "
            "FROM Pokedex "
            "JOIN Typing_ID ON Pokedex.pokedex_id = "
            "Typing_ID.pokedex_id "
            "JOIN Typing ON Typing_ID.typing_id = "
            "Typing.typing_id "
            "JOIN Evolution_Stage ON Pokedex.evolution_stage_id = "
            "Evolution_Stage.evolution_stage_id "
            "JOIN Generation ON Pokedex.generation = "
            "Generation.generation "
            "WHERE pokemon LIKE ? "
            "GROUP BY Pokedex.pokedex_id",
            (f"%{regional_form}%",)
        )
        results = cursor.fetchall()
        if results:
            # print results neatly
            print(
                "Pokedex Number | Pokemon | Generation | Region | "
                "Evolution Stage | Types"
            )
            for pokemon in results:
                print(
                    f"{pokemon[0]:<14} | {pokemon[1]:<7} | {pokemon[2]:<10} | "
                    f"{pokemon[3]:<6} | {pokemon[4]:<15} | {pokemon[5]:<5}"
                )
        else:
            # if no results print message
            print("That is not a valid regional form.")
        db.close()
    elif user_input == "7":
        # Search for Pokémon with a specific typing
        typing = input(
            "Enter the typing (Normal, Grass, Water, Fire, Electric, Bug, "
            "Flying, Poison, Ground, Rock, Fighting, Psychic, Ice, Ghost, "
            "Dragon, Dark, Steel, Fairy): "
        )
        typing3 = typing.title()
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        # search for pokemon by typing
        cursor.execute(
            "SELECT Pokedex.pokedex_number, "
            "Pokedex.pokemon, Pokedex.generation, "
            "Generation.region, Evolution_Stage.evolution_stage, "
            "GROUP_CONCAT(DISTINCT Typing.typing ORDER BY typing) "
            "FROM Pokedex "
            "JOIN Typing_ID ON Pokedex.pokedex_id = "
            "Typing_ID.pokedex_id "
            "JOIN Typing ON Typing_ID.typing_id = "
            "Typing.typing_id "
            "JOIN Evolution_Stage ON Pokedex.evolution_stage_id = "
            "Evolution_Stage.evolution_stage_id "
            "JOIN Generation ON Pokedex.generation = "
            "Generation.generation "
            "WHERE Pokedex.pokedex_id "
            "IN (SELECT Typing_ID.pokedex_id "
            "FROM Typing_ID "
            "JOIN Typing ON Typing_ID.typing_id = "
            "Typing.typing_id WHERE Typing.typing = ?) "
            "GROUP BY Pokedex.pokedex_id "
            "ORDER BY Pokedex.pokedex_number; ",
            (typing3.strip(),)
        )
        results = cursor.fetchall()
        # print results neatly
        if results:
            print(
                "Pokedex Number | Pokemon | Generation | Region | "
                "Evolution Stage | Types"
            )
            for pokemon in results:
                print(
                    f"{pokemon[0]:<14} | {pokemon[1]:<7} | {pokemon[2]:<10} | "
                    f"{pokemon[3]:<6} | {pokemon[4]:<15} | {pokemon[5]:<5}"
                )
        else:
            # if no results print message
            print("No Pokémon found with that typing.")
    elif user_input == "8":
        # Search for Pokémon with specific dual typings
        typing1 = input(
            "Enter the first typing (Normal, Grass, Water, Fire, Electric, "
            "Bug, Flying, Poison, Ground, Rock, Fighting, Psychic, Ice, "
            "Ghost, Dragon, Dark, Steel, Fairy): "
        )
        typing2 = input(
            "Enter the second typing (Normal, Grass, Water, Fire, Electric, "
            "Bug, Flying, Poison, Ground, Rock, Fighting, Psychic, Ice, "
            "Ghost, Dragon, Dark, Steel, Fairy): "
        )
        typing11 = typing1.title()
        typing22 = typing2.title()
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        # search for pokemon by their dual typing
        cursor.execute(
            "SELECT pokedex_number, pokemon, Pokedex.generation, "
            "Generation.region, Evolution_Stage.evolution_stage, "
            "GROUP_CONCAT(DISTINCT Typing.typing) "
            "FROM Pokedex "
            "JOIN Generation ON Pokedex.generation = "
            "Generation.generation "
            "JOIN Evolution_Stage ON Pokedex.evolution_stage_id = "
            "Evolution_Stage.evolution_stage_id "
            "JOIN Typing_ID ON Pokedex.pokedex_id = "
            "Typing_ID.pokedex_id "
            "JOIN Typing ON Typing_ID.typing_id = "
            "Typing.typing_id "
            "WHERE Typing.typing IN (?, ?) "
            "GROUP BY Pokedex.pokedex_id "
            "HAVING COUNT(DISTINCT Typing.typing) = 2",
            (typing11.strip(), typing22.strip())
        )
        results = cursor.fetchall()
        # print results neatly
        if results:
            print(
                "Pokedex Number | Pokemon | Generation | Region | "
                "Evolution Stage | Types"
            )
            for pokemon in results:
                print(
                    f"{pokemon[0]:<14} | {pokemon[1]:<7} | {pokemon[2]:<10} | "
                    f"{pokemon[3]:<6} | {pokemon[4]:<15} | {pokemon[5]:<5}"
                )
        else:
            # if no results print message
            print("No Pokémon found with those typings.")
        db.close()
    elif user_input == "9":
        # Exit the program
        print("Goodbye!")
        break
    else:
        # Invalid input handling
        print("Invalid option. Please try again.\n")
