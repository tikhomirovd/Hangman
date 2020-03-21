import random

print("H A N G M A N")
print()
# Write your code here



def check_letter(out):
    print(out)
    letterf = input("Input a letter: ")
    if len(letterf) != 1:
        print("You should print a single letter")
        print()
        return check_letter(out)
    if letterf.lower() != letterf or not letterf.isalpha():
        print("It is not an ASCII lowercase letter")
        print()
        return check_letter(out)

    return letterf

def check_status():
    status = input('Type "play" to play the game, "exit" to quit:')
    if status == 'play':
        game()
        return check_status()
    else:
        return 0

def game():
    mistakes = 8
    world_list = ['python', 'java', 'kotlin', 'javascript']
    answer = random.choice(world_list)
    out = '-' * len(answer)
    mistakes = 8
    ans_letters = ''
    used_letters = ''
    while mistakes != 0:
        flag = False
        letter = check_letter(out)
        if letter in used_letters:
            print("You already typed this letter")
            flag = True
        else:
            for index, let in enumerate(answer):

                if letter in let:
                    out = out[:index] + letter + out[index + 1:]
                    ans_letters += letter
                    flag = True
        if not flag:
            print("No such letter in the word")
            mistakes -= 1
        used_letters += letter
        if sorted(answer) == sorted(ans_letters):
            print("You guessed the word!")
            print("You survived!")
            break
        elif mistakes == 0:
            print("You are hanged!")
        print()

check_status()
