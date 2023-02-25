from guizero import App, Text, Picture, TextBox, PushButton, Box, ButtonGroup, error, Window

import random
from hangman_img import number_wrong, splash


def game():
    global display_box, display, correct, letters, false, correct, bob

    app = App(title='Hangman', width=550, height=300)
    app.icon = 'man.ico'

    # Splash Page
    def desfp():
        fp.destroy()
        options.show()

    fp = Box(app)
    Picture(fp, image=random.choice(splash))
    fp.after(1900, desfp)

    # Game Mode Select
    def mode_select():
        if choice1.value == 'Computer':
            options.destroy()
            computer.show()
        elif choice1.value == 'Player':
            options.destroy()
            player.show()

    options = Box(app)
    options.hide()

    Text(options, text='\nDo you want to play against the computer\n or have another player input a word?', size=15)
    Text(options, text='Computer Mode is in US English Only', size=11, color='red', font='Arial Italic')
    choice1 = ButtonGroup(options, options=["Computer", "Player"], selected="Computer")
    PushButton(options, command=mode_select, text="      Enter      ")

    def computer_select():
        global length, word

        try:
            length = int(choice2.value)
            fo = open("words.txt", "r")
            yo = fo.readlines()
            ranlist = []
            for y in range(len(yo) - 1):
                y = y + 1
                if len(yo[y]) == (length + 1):
                    ranlist.append(yo[y])

            rannum = (random.randint(0, (len(ranlist))))
            word = (ranlist[rannum])
            computer.destroy()
            tries.show()
        except ValueError:
            error('Error', 'Not a valid integer')
        except IndexError:
            error('Error', 'Not in the range, pick a number that is less than 12 letters')

    computer = Box(app)
    computer.hide()
    Text(computer, text='\nHow long do you want the word to be?', size=15)
    choice2 = TextBox(computer, width=20)
    button2 = PushButton(computer, command=computer_select, text="      Enter      ")

    def player_select():
        global length, word, word_reveal
        word = str(choice3.value)
        word = word.lower()
        x = str.isalpha(word)
        length = len(word)

        if x == False:
            error('Error', ' Input a Word, with no letters or symbol')
        else:
            player.destroy()
            theme_input.show()

    player = Box(app)
    player.hide()
    Text(player, text='\nInput a Word:', size=15)
    choice3 = TextBox(player, width=20)
    button3 = PushButton(player, command=player_select, text="      Enter      ")

    def theme_select():
        global theme_value
        theme_value = str(choice4.value)
        theme_input.destroy()
        tries.show()

    theme_input = Box(app)
    theme_input.hide()
    Text(theme_input, text='\nWhat is the theme of your word?', size=15)
    choice4 = TextBox(theme_input, width=20)
    button4 = PushButton(theme_input, command=theme_select, text="      Enter      ")

    display_info = Box(app)

    def continue_function():
        display_info.hide()
        main_game.show()

    def tries_select():
        global word_reveal, tries_num

        try:
            tries_num = int(choice5.value)
            tries.destroy()
        except ValueError:
            error('Error', 'This is not a number, Try again')
        else:
            try:
                theme_value
                display_info.show()
                Text(display_info, text='\nThe Theme is:', size=15)
                Text(display_info, text=theme_value, size=15)

                Text(display_info, text='\nThe length of the word is:', size=15)
                Text(display_info, text=length, size=15)
                Text(display_info, text='_ ' * length, size=13)
                word_reveal = ['_'] * length

            except NameError:
                display_info.show()
                Text(display_info, text='\nThe length of the word is:')
                Text(display_info, text=length, size=15)
                Text(display_info, text='_ ' * length, size=15)
                word_reveal = ['_'] * length
            display_info.after(1900, continue_function)

    tries = Box(app)
    tries.hide()
    Text(tries, text='\nHow many incorrect guesses do you want?', size=15)
    Text(tries, text='A Standard Game of Hangman ends after 8 incorrect guesses', size=13)
    choice5 = TextBox(tries, width=20)
    button5 = PushButton(tries, command=tries_select, text="      Enter      ")

    letters = []
    false = 0
    correct = 0

    def both():
        global display_box, display
        display_box.destroy()
        display_box = Box(display)
        game_comp()

    def exit_game():
        exit_select = app.yesno("Exit?", "Do you want to play again?")

        if exit_select == False:
            exit()
        elif exit_select == True:
            app.destroy()
            game()

    def game_comp():
        global correct, false, word_reveal, display

        guess = str(choice6.value)
        guess = guess.lower()
        choice6.clear()

        try:
            num_test = int(guess)
            error('Error', 'This is not a valid letter, Try again')

        except ValueError:

            if len(guess) == length and guess == word:
                # print("You have correctly guessed the word!") # Fix Formatting
                app.info("I'm proud of you!", text='You have correctly guessed the word!')
                exit_game()

            elif guess == ' ':
                error('Oh, no', "Space isn't a valid input")

            elif guess in letters:
                error('Oh, no', 'You have already used that letter')

            elif guess == '':
                error('Oh, no', 'You entered nothing')

            if guess in word and guess not in letters and guess != ' ' and guess != '':
                letters.append(guess)
                you_guessed = ("\nYou've guessed:  " + " ".join(letters))
                Text(display_box, text=you_guessed)

                Text(display_box, text='\nCorrect Guess\n')
                x = 0
                for i in range(len(word)):
                    new_word = word.replace(guess, "_", x)
                    new_result = new_word.find(guess)
                    int(new_result)

                    if new_result >= 0:
                        word_reveal[new_result] = guess
                        i = i + 1
                        x = x + 1
                        correct = correct + 1
                word_reveal_text = (' '.join(word_reveal))
                Text(display_box, text=word_reveal_text)

                display.show()

                if correct == length:
                    Text(display_box, text='Well Done! You guessed correctly')
                    exit_game()



            elif guess not in word and guess not in letters and guess != ' ' and guess != '':
                letters.append(guess)

                you_guessed = ("\nYou've guessed:  " + " ".join(letters))
                Text(display_box, text=you_guessed)

                Text(display_box, text='Incorrect Guess')
                if tries_num == 8:
                    Picture(display_box, image=number_wrong[false])

                word_reveal_text = (' '.join(word_reveal))
                Text(display_box, text=word_reveal_text)

                false = false + 1
                display.show()

                if false == tries_num:
                    display_box.destroy()
                    final_display_box.show()
                    Text(final_display_box, text='\nOut of Guesses!')  # Fix Formatting, make look pretty
                    Text(final_display_box, text=word_reveal_text)
                    Text(final_display_box, text='The Word was:')
                    Text(final_display_box, text=word)
                    display.show()
                    exit_game()

    main_game = Box(app)
    main_game.hide()

    Text(main_game, text='\nWhat letter or word do you want to input:')
    choice6 = TextBox(main_game, width=20)

    button6 = PushButton(main_game, command=both, text="      Enter      ")

    display = Window(app, title='Gamer Box', height=400, width=400)
    display.hide()

    display_box = Box(display)
    display_box.hide()

    final_display_box = Box(display)
    final_display_box.hide()

    app.display()


# Main Game Loop is game function

if __name__ == "__main__":
    game()
