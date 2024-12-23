import random

def hangman_game(check=True):

    while True:
            if check:  # Show rules only on the first start
                print("\nIn order to start the game write: 'start en' to play with English and 'start hu' to play with Hungarian or 'start es' to play with Spanish words.")
                print("Or if you want to stop the game write: 'stop'")
                print("During the game you can't stop the game by typing 'stop' since it can be a word to be guessed.")
                print("To see the already guessed characters type 'help'. Help can not be a word to guess.\n")
            try:
                starter = input("\nEnter the choice of yours: ")
                if starter not in ["start en","start hu","start es","stop"]:
                    raise ValueError("Invalid input!")
                elif starter == "stop":
                    print("Exiting the game.")
                    exit()
                elif starter == "start en":
                    language = "en"
                    print("Starting the game...")
                    break
                elif starter == "start hu":
                    language = "hu"
                    print("Starting the game...")
                    break
                elif starter == "start es":
                    language = "es"
                    print("Starting the game...")
                    break
            except ValueError as e:
                print(e)     

    def word_reader(value):
        import os

        file_path = os.path.join(os.path.dirname(__file__), f"hangman_{value}_words.txt")
        
        try:
            with open(file_path, "r") as file:
                content = file.read()
                words = content.replace(",", "").split()
                return words
        except FileNotFoundError:
            print(f"Error: The file 'hangman_{value}_words.txt' was not found.")
            return []

    game_dictionary = word_reader(language)
    
    random_choice = random.choice(game_dictionary)
    count_till_death = 0

    random_word = ["_"] * len(random_choice)
    guessed_chars = []
    print(random_word)
    print("The number to help with the length: ", len(random_choice))
    
    while True:
        guess = input("\nType guess: ")

        if guess == "help":
            print("These are the guessed characters: ", guessed_chars)
            continue

        guess_filtered = ''.join(char for char in guess if char.isalpha())

        if len(guess_filtered) != 1:
            print("Please type one letter at a time.")
            continue

        if guess_filtered in random_word or guess_filtered in guessed_chars:
            print("The letter was already guessed! Here take a look at the guessed wrong letters: ", guessed_chars, "\nNow try again!\n")
            continue

        if guess_filtered in random_choice:
            for count, char in enumerate(random_choice):            
                if char == guess_filtered:
                    random_word[count] = guess_filtered
                    print(random_word)
        else:
            guessed_chars.append(guess_filtered)
            count_till_death += 1

            # do it with dictionary too
            if count_till_death == 1:
                print("         {I}     {I}")
                print(random_word)
            elif count_till_death == 2:
                print("          I       I\n         {I}     {I}")
                print(random_word)
            elif count_till_death == 3:
                print("          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                print(random_word)
            elif count_till_death == 4:
                print("          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                print(random_word)
            elif count_till_death == 5:
                print("              | \n              | \n              | \n          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                print(random_word)
            elif count_till_death == 6:
                print("              ł\n              |\n              | \n              | \n              | \n          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                print(random_word)
            elif count_till_death == 7:
                print("        ------ł\n              |\n              | \n              | \n              | \n          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                print(random_word)
            elif count_till_death == 8:
                print("  @-----------ł\n              |\n              | \n              | \n              | \n          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                print(random_word)
            elif count_till_death == 9:
                print("  @-----------ł\n  O           |\n              | \n              | \n              | \n          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                print("It has begun...")
                print(random_word)
            elif count_till_death == 10:
                print("  @-----------ł\n  O           |\n  |           | \n              | \n              | \n          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                #print("  O\n  |")
                print("It's starting to hurt...")
                print(random_word)
            elif count_till_death == 11:
                print("  @-----------ł\n  O           |\n /|           | \n              | \n              | \n          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                #print("  O\n /|")
                print("Please help me!")
                print(random_word)
            elif count_till_death == 12:
                print("  @-----------ł\n  O           |\n /|\\          | \n              | \n              | \n          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                #print("  O\n /|\\")
                print("I don't want to die! Help me!")
                print(random_word)
            elif count_till_death == 13:
                print("  @-----------ł\n  O           |\n /|\\          | \n  |           | \n              | \n          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                #print("  O\n /|\\\n  |")
                print("It's getting cold...")
                print(random_word)
            elif count_till_death == 14:
                print("  @-----------ł\n  O           |\n /|\\          | \n  |           | \n /            | \n          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                #print("  O\n /|\\\n  |\n /")
                print("I see the light in the tunnel...")
                print(random_word)
            elif count_till_death == 15:
                print("  @-----------ł\n  O           |\n /|\\          | \n  |           | \n / \\          | \n          I~~[¤]~~I\n          I¨¨¨¨¨¨¨I\n          I       I\n         {I}     {I}")
                #print("  O\n /|\\\n  |\n / \\")
                print("(X.X)")

                while True:
                    try:
                        gaming = input("\nDo you want to countinue? 'yes' or 'no'\n")
                        if gaming == "no":
                            exit()
                        elif gaming == "yes":
                            hangman_game(check=False)
                    except ValueError as e:
                        print(e)

        if "_" not in random_word:
            print("You did it! The word was: ", ''.join(random_word))
            
            while True:
                try:
                    gaming = input("\nDo you want to countinue? 'yes' or 'no'\n")
                    if gaming == "no":
                        exit()
                    elif gaming == "yes":
                        hangman_game(check=False)
                except ValueError as e:
                    print(e)  

hangman_game()

