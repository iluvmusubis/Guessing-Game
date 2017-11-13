import random
def main():
    print("\nWelcome to the Guessing Game!\n"
          "\nPlease choose your difficulty level:\n"
          "\n1. Easy\n"
          "\n2. Medium\n"
          "\n3. Hard\n")
    x = int(input())
    if x == 1:
        easy()
    elif x == 2:
        medium()
    elif x == 3:
        hard()


def easy():
    print("\nFirst to 10 guesses loses\n"
          "\nPlayer 1, try and guess the random number between 1 and 10")
    random_num = random.randrange(1, 11)
    x = int(input())
    count = 0
    while random_num != x:
        if x < random_num:
            print("The number you entered is too low")
            x = int(input())
            count = count + 1
        elif x > random_num:
            print("The number you entered is too high")
            x = int(input())
            count = count + 1
    while random_num == x:
        print("Congratulations you guessed the correct number!")
        count = count + 1
        count = str(count)
        print("It took you " + count + " tries to guess the number")
        break
    print("\nPlayer 2, try and guess a number between 1 and 10")
    random_num2 = random.randrange(1, 11)
    y = int(input())
    count2 = 0
    while random_num2 != y:
        if y < random_num2:
            print("The number you entered is too low")
            y = int(input())
            count2 = count2 + 1
        elif y > random_num2:
            print("The number you entered is too high")
            y = int(input())
            count2 = count2 + 1
    while random_num2 == y:
        print("Congratulations you guessed the correct number!")
        count2 = count2 + 1
        count2 = str(count2)
        print("It took you " + count2 + " tries to guess the number")
        break
    count = int(count)
    count2 = int(count2)

    while count < 10 and count2 < 10:
        print("\nPlayer 1, try and guess the random number between 1 and 10")
        random_num = random.randrange(1, 11)
        user_num = int(input())
        while random_num != user_num:
            if user_num < random_num:
                print("The number you entered is too low")
                user_num = int(input())
                count = count + 1
            elif user_num > random_num:
                print("The number you entered is too high")
                user_num = int(input())
                count = count + 1
        while random_num == user_num:
            print("Congratulations you guessed the correct number!")
            count = count + 1
            count = str(count)
            print("It took you " + count + " tries to guess the number")
            break

        print("\nPlayer 2, try and guess the random number between 1 and 10")
        random_num2 = random.randrange(1, 11)
        user_num = int(input())
        while random_num2 != user_num:
            if user_num < random_num:
                print("The number you entered is too low")
                user_num = int(input())
                count2 = count2 + 1
            elif user_num > random_num2:
                print("The number you entered is too high")
                user_num = int(input())
                count2 = count2 + 1
        while random_num2 == user_num:
            print("Congratulations you guessed the correct number!")
            count2 = count2 + 1
            count2 = str(count2)
            print("It took you " + count + " tries to guess the number")
        break

    if count > count2:
        print("\nPlayer 2 wins!\n"
              "\nPlayer 1 loses\n")
    elif count < count2:
        print("\nPlayer 1 wins!\n"
              "\nPlayer 2 loses\n")
    elif count == count2:
        print("There is tie. Play again.")
    replay()


def medium():
    print("First to 15 guesses loses. Good Luck!\n"
          "\nPlayer 1, try and guess the random number between 1 and 20")
    random_num = random.randrange(1, 21)
    x = int(input())
    count = 0
    while random_num != x:
        if x < random_num:
            print("The number you entered is too low")
            x = int(input())
            count = count + 1
        elif x > random_num:
            print("The number you entered is too high")
            x = int(input())
            count = count + 1
    while random_num == x:
        print("Congratulations you guessed the correct number!")
        count = count + 1
        count = str(count)
        print("It took you " + count + " tries to guess the number")
        break
    print("\nPlayer 2, try and guess a number between 1 and 20")
    random_num2 = random.randrange(1, 21)
    y = int(input())
    count2 = 0
    while random_num2 != y:
        if y < random_num2:
            print("The number you entered is too low")
            y = int(input())
            count2 = count2 + 1
        elif y > random_num2:
            print("The number you entered is too high")
            y = int(input())
            count2 = count2 + 1
    while random_num2 == y:
        print("Congratulations you guessed the correct number!")
        count2 = count2 + 1
        count2 = str(count2)
        print("It took you " + count2 + " tries to guess the number")
        break
    while count < 15 and count2 < 15:
        print("\nPlayer 1, try and guess the random number between 1 and 20")
        random_num = random.randrange(1, 21)
        user_num = int(input())
        while random_num != user_num:
            if user_num < random_num:
                print("The number you entered is too low")
                user_num = int(input())
                count = count + 1
            elif user_num > random_num:
                print("The number you entered is too high")
                user_num = int(input())
                count = count + 1
        while random_num == user_num:
            print("Congratulations you guessed the correct number!")
            count = count + 1
            count = str(count)
            print("It took you " + count + " tries to guess the number")
            break

        print("\nPlayer 2, try and guess the random number between 1 and 20")
        random_num2 = random.randrange(1, 21)
        user_num = int(input())
        while random_num2 != user_num:
            if user_num < random_num:
                print("The number you entered is too low")
                user_num = int(input())
                count2 = count2 + 1
            elif user_num > random_num2:
                print("The number you entered is too high")
                user_num = int(input())
                count2 = count2 + 1
        while random_num2 == user_num:
            print("Congratulations you guessed the correct number!")
            count2 = count2 + 1
            count2 = str(count2)
            print("It took you " + count + " tries to guess the number")
        break

    if count > count2:
        print("\nPlayer 2 wins!\n"
              "\nPlayer 1 loses\n")
    elif count < count2:
        print("\nPlayer 1 wins!\n"
              "\nPlayer 2 loses\n")
    elif count == count2:
        print("There is tie. Play again.")
    replay()

def hard():
    print("First to 30 guesses loses. Good Luck!\n"
          "\nPlayer 1, try and guess the random number between 1 and 100")
    random_num = random.randrange(1, 101)
    user_num = int(input())
    count = 0
    while random_num != user_num:
        if user_num < random_num:
            print("The number you entered is too low")
            user_num = int(input())
            count = count + 1
        elif user_num > random_num:
            print("The number you entered is too high")
            user_num = int(input())
            count = count + 1
    while random_num == user_num:
        print("Congratulations you guessed the correct number!")
        count = count + 1
        count = str(count)
        print("It took you " + count + " tries to guess the number")
        break
    print("\nPlayer 2, try and guess a number between 1 and 100")
    random_num2 = random.randrange(1, 101)
    y = int(input())
    count2 = 0
    while random_num2 != y:
        if y < random_num2:
            print("The number you entered is too low")
            y = int(input())
            count2 = count2 + 1
        elif y > random_num2:
            print("The number you entered is too high")
            y = int(input())
            count2 = count2 + 1
    while random_num2 == y:
        print("Congratulations you guessed the correct number!")
        count2 = count2 + 1
        count2 = str(count2)
        print("It took you " + count2 + " tries to guess the number")
        break
    if count > count2:
        print("\nPlayer 2 wins!\n"
              "\nPlayer 1 loses\n")
    elif count < count2:
        print("\nPlayer 1 wins!\n"
              "\nPlayer 2 loses\n")
    elif count == count2:
        print("There is tie. Play again.")
    replay()
    replay()


def replay():
    print("\nWould you like to play again?\n"
          "\n1. Yes\n"
          "\n2. No\n "
          "\nPlease choose a number\n")
    choice = int(input())
    if choice == 1:
        main()
    else:
        print("Game Over")


def easy1():
    print("\nPlayer 1, try and guess the random number between 1 and 10")
    random_num = random.randrange(1, 11)
    user_num = int(input())
    while random_num != user_num:
        if user_num < random_num:
            print("The number you entered is too low")
            user_num = int(input())
            count = count + 1
        elif user_num > random_num:
            print("The number you entered is too high")
            user_num = int(input())
            count = count + 1
    while random_num == user_num:
        print("Congratulations you guessed the correct number!")
        count = count + 1
        count = str(count)
        print("It took you " + count + " tries to guess the number")
        break


def easy2():
    print("\nPlayer 2, try and guess a number between 1 and 10 ")
    random_num2 = random.randrange(1, 11)
    user_num2 = int(input())
    count2 = 0
    while random_num2 != user_num2:
        if user_num2 < random_num2:
            print("The number you entered is too low")
            user_num2 = int(input())
            count2 = count2 + 1
        elif user_num2 > random_num2:
            print("The number you entered is too high")
            user_num2 = int(input())
            count2 = count2 + 1
    while random_num2 == user_num2:
        print("Congratulations you got the number!")
        count2 = count2 + 1
        count2 = str(count2)
        print("It took you " + count2 + " tries to guess the number")
        break

def medium1():
    print("\nPlayer 1, try and guess the random number between 1 and 20")
    random_num = random.randrange(1, 21)
    user_num = int(input())
    while random_num != user_num:
        if user_num < random_num:
            print("The number you entered is too low")
            user_num = int(input())
            count = count + 1
        elif user_num > random_num:
            print("The number you entered is too high")
            user_num = int(input())
            count = count + 1
    while random_num == user_num:
        print("Congratulations you guessed the correct number!")
        count = count + 1
        count = str(count)
        print("It took you " + count + " tries to guess the number")
        break

def medium2():
    print("\nPlayer 2, try and guess a number between 1 and 20 ")
    random_num2 = random.randrange(1, 21)
    user_num2 = int(input())
    count2 = 0
    while random_num2 != user_num2:
        if user_num2 < random_num2:
            print("The number you entered is too low")
            user_num2 = int(input())
            count2 = count2 + 1
        elif user_num2 > random_num2:
            print("The number you entered is too high")
            user_num2 = int(input())
            count2 = count2 + 1
    while random_num2 == user_num2:
        print("Congratulations you got the number!")
        count2 = count2 + 1
        count2 = str(count2)
        print("It took you " + count2 + " tries to guess the number")
        break

def hard1():
    print("\nPlayer 2, try and guess a number between 1 and 100 ")
    random_num2 = random.randrange(1, 101)
    user_num2 = int(input())
    count2 = 0
    while random_num2 != user_num2:
        if user_num2 < random_num2:
            print("The number you entered is too low")
            user_num2 = int(input())
            count2 = count2 + 1
        elif user_num2 > random_num2:
            print("The number you entered is too high")
            user_num2 = int(input())
            count2 = count2 + 1
    while random_num2 == user_num2:
        print("Congratulations you got the number!")
        count2 = count2 + 1
        count2 = str(count2)
        print("It took you " + count2 + " tries to guess the number")
        break

def hard2():
    print("\nPlayer 2, try and guess a number between 1 and 100 ")
    random_num2 = random.randrange(1, 101)
    user_num2 = int(input())
    count2 = 0
    while random_num2 != user_num2:
        if user_num2 < random_num2:
            print("The number you entered is too low")
            user_num2 = int(input())
            count2 = count2 + 1
        elif user_num2 > random_num2:
            print("The number you entered is too high")
            user_num2 = int(input())
            count2 = count2 + 1
    while random_num2 == user_num2:
        print("Congratulations you got the number!")
        count2 = count2 + 1
        count2 = str(count2)
        print("It took you " + count2 + " tries to guess the number")
        break

main()