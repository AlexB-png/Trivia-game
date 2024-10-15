import json
import getpass
import time
from os import system
import os
import random
user = [1]

def play():
    print("\n==========START QUIZ==========")
    score = 0
    with open("questions.json", 'r+') as f:
        j = json.load(f)
        for i in range(10):
            no_of_questions = len(j)
            check = random.randint(0, no_of_questions - 1)
            print(f'\nQ{i + 1} {j[check]["question"]}')
            for option in j[check]["options"]:
                print(option)
            answer = input("\nEnter your answer: ")
            if j[check]["answer"][0] == answer[0].upper():
                print("\nYou are correct")
                score += 1
            else:
                print("\nYou are incorrect")
                break
            del j[check]
        print("Score :",score)
        quit()


def quizQuestions():

    print('\n==========ADD QUESTIONS==========\n')
    ques = input("Enter the question that you want to add:\n")
    opt = []
    print("Enter the 4 options with character initials (A, B, C, D)")
    for _ in range(4):
        opt.append(input())
    ans = input("Enter the answer:\n")
    with open("questions.json", 'r+') as f:
        questions = json.load(f)
        dic = {"question": ques, "options": opt, "answer": ans}
        questions.append(dic)
        f.seek(0)
        json.dump(questions, f)
        f.truncate()
        print("Question successfully added.")
    

def addAccount():
    print("\n==========CREATE ACCOUNT==========")
    username = print("Enter your USERNAME: ")
    password = getpass.getpass(prompt='Enter your PASSWORD: ')
    with open('user_accounts.json', 'r+') as user_accounts:
        users = json.load(user_accounts)
        if username in users.keys():
            print("An account of this Username already exists.\nPlease enter the login panel.")
        else:
            users[username] = [password, "PLAYER"]
            user_accounts.seek(1)
            json.dump(users, user_accounts)
            user_accounts.truncate()
            print("Account created successfully!")


def loginAccount():
    print('\n==========LOGIN PANEL==========')
    variable1 = input("USERNAME: ")
    password = getpass.getpass(prompt='PASSWORD: ')
    with open('user_accounts.json', 'r') as user_accounts:
        users = json.load(user_accounts)
    if variable1 in users.keys():
        print("An account of that name doesn't exist.\nPlease create an account first.")
    elif variable1 in users.keys():
        if users[variable1][0]!= password:
            print("Your password is incorrect.\nPlease enter the correct password and try again.")
        elif users[variable1][0] == password:
            print("You have successfully logged in.\n")
            user.append(variable1)
            user.append(users[variable1][1])





def rules():
    print('''\n==========HOW TO PLAY==========
1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.
	''')


def about():
    print('''\n==========ABOUT US==========
This project has been created by ACC Ltd.''')

anotherVariable = 1

correct = 0
if anotherVariable != 5:
    print('\n=========ACC: QUIZ MASTER==========')
    print('-----------------------------------------')
    print('1. PLAY QUIZ')
    print('2. ADD QUIZ QUESTIONS')
    print('3. LOGIN')
    print('4. HOW TO PLAY')
    print('5. EXIT')
    print('6. ABOUT US')
    correct=0
    while correct != 1:
        
        anotherVariable = input('ENTER YOUR CHOICE: ')
        y=1
        while y == 1:
            try:
                anotherVariable = int(anotherVariable)
                y=0
                break
            except:
                print("There is an error with the Choice")
                anotherVariable = input("Try again \n")

        if anotherVariable == 1:
            play()
        elif anotherVariable == 2:
            print("Please log in before doing that")
            
        elif anotherVariable == 3:
            username = input("What is the username?")
            print("Password has been hidden for your safety")
            password = getpass.getpass(prompt='PASSWORD: ')
            if username == "Roger2909":
                if password == "ADMIN":
                    quizQuestions()
                    play()
            elif username == "RogerRoger2":
                if password == "PLAYER":
                    print("You have been logged in")
            elif username == "test":
                if password == "PLAYER":
                    print("You have been logged in")
            else:
                print("Not a valid username and password")
            break
        elif anotherVariable == 4:
            rules()
            correct=1
        elif anotherVariable == 5:
            os.system('CLS')
            print("Exiting software. . .")
            time.sleep(5)
            os.system('CLS')
            print("See you again soon!")
            correct=1
        elif anotherVariable == 6:
            about()
            correct=1
        else:
            print('WRONG INPUT. ENTER THE CHOICE AGAIN')
            anotherVariable = int(input('ENTER YOUR CHOICE: '))






