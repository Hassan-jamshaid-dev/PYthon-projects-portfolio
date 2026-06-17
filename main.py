#            THESE ARE ALL MY PYTHON PROJECTS

# 1.QUIZ GAME
questions = ("What is the colour of the sky: ",
             "How many meters are in a kilometer: ",
             "Who is the G.O.A.T: ",
             "Who will win the world cup: ",
             "What is the best programming language: : ")
options = (("A: Blue","B: Pink","C: Black","D: Brown"),
           ("A: 123","B: 456","C: 719","D: 1000"),
           ("A: messi","B: pele","C: ronaldo","D: zidane"),
           ("A: portugal","B: brazil","C: spain","D: rance"),
           ("A: SQl","B: python","C: java","D: CSS"))
answers = ("A","D","C","A","B")
guesses = []
score = 0
qn = 0

for question in questions:
    print("^^^^^^^^^^^^^^^^^^^^^")
    print(question)
    for option in options[qn]:
        print(option)
    guess = input("Enter the correct option (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[qn]:
        score = score +1
        print("CORRECT!")
    else :
        print("INCORRECT!")
    qn+=1
print("-------------------------------------")
print("              RESULT                 ")
print("-------------------------------------")

print("answers ",end ="")
for answer in answers:
    print(answer,end=" ")
print()
print("guesses ",end ="")
for guess in guesses:
    print(guess,end=" ")
print()
score = int(score / len(questions)*100)
print(f"Your score is: {score}")


# CAPITAL DATABASE PROGRAM

capitals = {"Afghanistan": "Kabul",
    "Albania": "Tirana",
    "Algeria": "Algiers",
    "Andorra": "Andorra la Vella",
    "Angola": "Luanda",
    "Antigua and Barbuda": "Saint John's",
    "Argentina": "Buenos Aires",
    "Armenia": "Yerevan",
    "Australia": "Canberra",
    "Austria": "Vienna",
    "Azerbaijan": "Baku",
    "Bahamas": "Nassau",
    "Bahrain": "Manama",
    "Bangladesh": "Dhaka",
    "Barbados": "Bridgetown",
    "Belarus": "Minsk",
    "Belgium": "Brussels",
    "Belize": "Belmopan",
    "Benin": "Porto-Novo",
    "Bhutan": "Thimphu",
    "Bolivia": "Sucre",
    "Bosnia and Herzegovina": "Sarajevo",
    "Botswana": "Gaborone",
    "Brazil": "Brasília",
    "Brunei": "Bandar Seri Begawan",
    "Bulgaria": "Sofia",
    "Burkina Faso": "Ouagadougou",
    "Burundi": "Gitega",
    "Cambodia": "Phnom Penh",
    "Cameroon": "Yaoundé",
    "Canada": "Ottawa",
    "Cape Verde": "Praia",
    "Central African Republic": "Bangui",
    "Chad": "N'Djamena",
    "Chile": "Santiago",
    "China": "Beijing",
    "Colombia": "Bogotá",
    "Comoros": "Moroni",
    "Congo": "Brazzaville",
    "Costa Rica": "San José",
    "Croatia": "Zagreb",
    "Cuba": "Havana",
    "Cyprus": "Nicosia",
    "Czech Republic": "Prague",
    "Denmark": "Copenhagen",
    "Djibouti": "Djibouti",
    "Dominica": "Roseau",
    "Dominican Republic": "Santo Domingo",
    "East Timor": "Dili",
    "Ecuador": "Quito",
    "Egypt": "Cairo",
    "El Salvador": "San Salvador",
    "Equatorial Guinea": "Malabo",
    "Eritrea": "Asmara",
    "Estonia": "Tallinn",
    "Eswatini": "Mbabane",
    "Ethiopia": "Addis Ababa",
    "Fiji": "Suva",
    "Finland": "Helsinki",
    "France": "Paris",
    "Gabon": "Libreville",
    "Gambia": "Banjul",
    "Georgia": "Tbilisi",
    "Germany": "Berlin",
    "Ghana": "Accra",
    "Greece": "Athens",
    "Grenada": "Saint George's",
    "Guatemala": "Guatemala City",
    "Guinea": "Conakry",
    "Guinea-Bissau": "Bissau",
    "Guyana": "Georgetown",
    "Haiti": "Port-au-Prince",
    "Honduras": "Tegucigalpa",
    "Hungary": "Budapest",
    "Iceland": "Reykjavik",
    "India": "New Delhi",
    "Indonesia": "Jakarta",
    "Iran": "Tehran",
    "Iraq": "Baghdad",
    "Ireland": "Dublin",
    "Israel": "Jerusalem",
    "Italy": "Rome",
    "Jamaica": "Kingston",
    "Japan": "Tokyo",
    "Jordan": "Amman",
    "Kazakhstan": "Astana",
    "Kenya": "Nairobi",
    "Kiribati": "South Tarawa",
    "Kuwait": "Kuwait City",
    "Kyrgyzstan": "Bishkek",
    "Laos": "Vientiane",
    "Latvia": "Riga",
    "Lebanon": "Beirut",
    "Lesotho": "Maseru",
    "Liberia": "Monrovia",
    "Libya": "Tripoli",
    "Liechtenstein": "Vaduz",
    "Lithuania": "Vilnius",
    "Luxembourg": "Luxembourg",
    "Madagascar": "Antananarivo",
    "Malawi": "Lilongwe",
    "Malaysia": "Kuala Lumpur",
    "Maldives": "Malé",
    "Mali": "Bamako",
    "Malta": "Valletta",
    "Marshall Islands": "Majuro",
    "Mauritania": "Nouakchott",
    "Mauritius": "Port Louis",
    "Mexico": "Mexico City",
    "Micronesia": "Palikir",
    "Moldova": "Chișinău",
    "Monaco": "Monaco",
    "Mongolia": "Ulaanbaatar",
    "Montenegro": "Podgorica",
    "Morocco": "Rabat",
    "Mozambique": "Maputo",
    "Myanmar": "Naypyidaw",
    "Namibia": "Windhoek",
    "Nauru": "Yaren",
    "Nepal": "Kathmandu",
    "Netherlands": "Amsterdam",
    "New Zealand": "Wellington",
    "Nicaragua": "Managua",
    "Niger": "Niamey",
    "Nigeria": "Abuja",
    "North Korea": "Pyongyang",
    "North Macedonia": "Skopje",
    "Norway": "Oslo",
    "Oman": "Muscat",
    "Pakistan": "Islamabad",
    "Palau": "Ngerulmud",
    "Panama": "Panama City",
    "Papua New Guinea": "Port Moresby",
    "Paraguay": "Asunción",
    "Peru": "Lima",
    "Philippines": "Manila",
    "Poland": "Warsaw",
    "Portugal": "Lisbon",
    "Qatar": "Doha",
    "Romania": "Bucharest",
    "Russia": "Moscow",
    "Rwanda": "Kigali",
    "Saint Kitts and Nevis": "Basseterre",
    "Saint Lucia": "Castries",
    "Saint Vincent and the Grenadines": "Kingstown",
    "Samoa": "Apia",
    "San Marino": "San Marino",
    "Sao Tome and Principe": "São Tomé",
    "Saudi Arabia": "Riyadh",
    "Senegal": "Dakar",
    "Serbia": "Belgrade",
    "Seychelles": "Victoria",
    "Sierra Leone": "Freetown",
    "Singapore": "Singapore",
    "Slovakia": "Bratislava",
    "Slovenia": "Ljubljana",
    "Solomon Islands": "Honiara",
    "Somalia": "Mogadishu",
    "South Africa": "Pretoria",
    "South Korea": "Seoul",
    "South Sudan": "Juba",
    "Spain": "Madrid",
    "Sri Lanka": "Sri Jayawardenepura Kotte",
    "Sudan": "Khartoum",
    "Suriname": "Paramaribo",
    "Sweden": "Stockholm",
    "Switzerland": "Bern",
    "Syria": "Damascus",
    "Taiwan": "Taipei",
    "Tajikistan": "Dushanbe",
    "Tanzania": "Dodoma",
    "Thailand": "Bangkok",
    "Togo": "Lomé",
    "Tonga": "Nuku'alofa",
    "Trinidad and Tobago": "Port of Spain",
    "Tunisia": "Tunis",
    "Turkey": "Ankara",
    "Turkmenistan": "Ashgabat",
    "Tuvalu": "Funafuti",
    "Uganda": "Kampala",
    "Ukraine": "Kyiv",
    "United Arab Emirates": "Abu Dhabi",
    "United Kingdom": "London",
    "United States": "Washington, D.C.",
    "Uruguay": "Montevideo",
    "Uzbekistan": "Tashkent",
    "Vanuatu": "Port Vila",
    "Vatican City": "Vatican City",
    "Venezuela": "Caracas",
    "Vietnam": "Hanoi",
    "Yemen": "Sana'a",
    "Zambia": "Lusaka",
    "Zimbabwe": "Harare"}

capital = input("Enter the city for which you would like to know the capital of: ").title()
print(capitals.get(capital))

# CONCESSION STAND PROGRAM
menu = {"pizza": 12.60,
        "burger": 5.99,
        "soda": 2.00,
        "milkshake": 3.00,
        "nuggets(10 pc)":7.99,
        "pretzel":3.50,
        "noodles":1.50}
cart=[]
total = 0
print("-----------MENU-----------")
for key,value in menu.items():
    print(f"{key:10}:{value:.2f}")
print("--------------------------")

while True:
    food = input("Enter a food from the menu (press q to esc): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)
print("-----YOUR CART-----")
print()
for food in cart:
    total = total + menu.get(food)
    print(food)
print()
print(f"Your total is: {total:.2f}")



#NUMBER GUESSING PROGRAM




import random
lowest_num = 1
highest_num = 100
num_guess = random.randint(lowest_num,highest_num)
guesses = 0
is_running = True
print("---------- WELCOME TO THE NUMBER GUESSING GAME ----------")
while is_running:
       guess = input("Enter your guess (1-100): ")
       if guess.isdigit():
          guess = int(guess)
          guesses +=1
          if guess < lowest_num or guess> highest_num:
                 print("Please enter a guess within the specified range")
          elif guess > num_guess:
                 print("Too high!")
          elif guess < num_guess:
                 print("Too low!")
          elif guess == num_guess:
                 print("CORRECT!")
                 print(f"It took you {guesses} guesses")
                 is_running = False
       else:
              print("Invalid response")


# ROCK<PAPER<SCISSOR GAME





import random
options = ("rock","paper","scissor")
player =None
computer = random.choice(options)

while player not in options:
       player = input("Enter either of the three (rock,paper or scissor): ").lower()

print(f"Computer: {computer}")
print(f"Player: {player}")

if computer == player:
       print("TIE!")
elif computer == "rock" and player == "paper":
       print("YOU WIN!")
elif computer == "scissor" and player == "rock":
       print("YOU WIN!")
elif computer == "paper " and player == "scissor":
       print("YOU WIN!")
else:
       print("YOU LOSE!")





# ADD AS MANY NUMBERS AS YOU LIKE




def add(*args):
    total = 0
    for arg in args:
        total = total + arg
    return total
number =[]
while True:
    num = input("Enter your number (press q to esc): ").lower()
    if num == "q":
        break
    number.append(int(num))
total = add(*number)

for n in number:
    print(n, end =" + ")
print("=",total)











# DAYS OF THE WEEK PROGRAM







def which_day(day):
    match day:
        case "monday":
            print("It is the first day of the week")
        case "tuesday":
            print("It is the second day of the week")
        case "wednesday":
            print("It is the third day of the week")
        case "thursday":
            print("It is the fourth day of the week")
        case "friday":
            print("It is the first day of the week")
        case "saturday":
            print("It is the sixth day of the week")
        case "sunday":
            print("It is the seventh day of the week")
        case _:
            print("NONE!")

day = input("Enter the day: ").lower()

which_day(day)






# BANKING PROGRAM



def show_balance():
    pass
def deposit():
    pass
def withdrawal():
    pass

balance = int(input("enter your balance: "))

while True:
    print("----------BANKING PROGRAM----------")
    print("1. Show balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Exit")
    print()

    choice = input("Enter (1,2,3,4): ")

    if choice.isdigit():
        if choice == "1":
            print(f"Your balance is {balance}")
        elif choice == "2":
            deposit = input("How much would you like to deposit: ")
            print()
            balance += int(deposit)
            print(f"Your deposit was {deposit} hence your balance is now {balance}")
        elif choice == "3" and int(choice)> 0:
            withdraw = input("How much would you like to withdraw: ")
            balance = balance - int(withdraw)
            print(f"The amount you withdrew is {withdraw} hence your balance is {balance}")
        elif choice == "4":
            print("THANK YOU FOR YOUR PATIENCE!")
            break
        else:
            print("INVALID RESPONSE")



# SLOT MACHINE PROGRAM


import random

def row_spinning():
    spins = ["🍇","🍈","🍉","🍊","🍌"]
    results =[]
    for spin in range(3):
        results.append(random.choice(spins))
    return results

def print_rows(rows):
    print("- - - - - - - - - - -")
    print("|".join(rows))
    print("- - - - - - - - - - -")

def pay_out(rows,bet):
    if rows[0] == rows[1]== rows[2]:
        if rows[0] == "🍇":
             return int(bet)*6
        elif rows[0] == "🍈":
            return int(bet) * 3
        elif rows[0] == "🍉":
            return int(bet) * 10
        elif rows[0] == "🍊":
            return int(bet) * 5
        elif rows[0] == "🍌":
            return int(bet) * 12

    return 0


def main_():
    balance = input("Enter your balance: ")
    print("-----------PYTHON SLOT MACHINE-----------")
    print("🍇,🍈,🍉,🍊,🍌")
    print()
    print(f"Your balance is {balance}")
    while int(balance) > 0:
        bet = input("How much would you like to bet: ")
        if not bet.isdigit():
            print("please enter a valid number")
            continue
        if int(bet) > int(balance):
            print("You cannot bet more than your balance")
            continue
        if int(bet)<=0:
            print("Bet must be a positive number")
            continue

        balance = int(balance) - int(bet)
        rows  = row_spinning()
        print("spinning... \n")
        print_rows(rows)
        payout = pay_out(rows,bet)
        if payout > 0:
            print(f"You won {payout}")
        else:
            print(f"Your balance is {balance}")
            print("You lost")

        balance += payout
        play_again = input("Do you want to play again (Y/N): ").upper()
        if play_again != "Y":
            break
if __name__ == "__main__":
    main_()





# ENCRYPTION PROGRAM

import string
import random
chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
keys = chars.copy()

random.shuffle(keys)
print(chars)
print(keys)

plain = input("Enter a message to be encrypted: ")
cipher = ""

for l in plain:
    index = chars.index(l)
    cipher = cipher +keys[index]


print(f"Your original message was {plain}")
print(f"Your encrypted message is {cipher}")


cipher = input("Enter a message to be decrypted: ")
plain = ""

for l in cipher:
    index = keys.index(l)
    plain = plain +chars[index]


print(f"Your encrypted message is {cipher}")
print(f"Your original message was {plain}")


# HANGMAN PROGRAM


import  random
from operator import index

words = ("apple", "nigger","man","portugal","apricot")
art_a = {0:("   ",
            "    ",
            "    "),
         1:(" o ",
            "   ",
            "   "),
        2: (" o ",
            " | "),
        3: (" o ",
            "|\\",
            "   "),
         4: (" o ",
             "/|\\",
             "   "),
        5: (" o ",
           "/|\\",
           "/   ") ,
       6 : (" o ",
            "/|\\ ",
            "/ \\")}

def hint_man(hint):
    print(" ".join(hint))


def display_man(wrong_guesses):
    for line in art_a[wrong_guesses]:
        print(line)
    print("--------------------------")
    print()


def answer_man(answer):
    print(" ".join(answer))


def main():
   answer = random.choice(words)
   hint = ["_"] * len(answer)
   wrong_guesses = 0
   guessed_letters = set()
   is_running = True


   while is_running:
       print("--------HANGMAN GAME--------")
       display_man(wrong_guesses)
       hint_man(hint)
       guess = input("Enter a letter to guess the word: ").lower()

       if len(guess) != 1:
           print("Your guess cannot be more than 1 letter!")
           continue
       if  not   guess.isalpha():
           print("You can only choose letters")
           continue
       if guess in guessed_letters:
           print("You cannot guess a letter more than once")
           continue


       guessed_letters.add(guess)



       if guess in answer:
           for index in range(len(answer)):
               if answer[index] == guess:
                   hint[index] = guess

       else:
           wrong_guesses+=1

       if "_" not in hint:
           display_man(wrong_guesses)
           answer_man(answer)
           print("YOU WIN!")
           is_running = False

       elif wrong_guesses >= len(art_a) - 1:
           display_man(wrong_guesses)
           answer_man(answer)
           print("YOU LOSE!!")
           is_running = False









if __name__ == "__main__":
    main()




# FIRST OOP PROGRAM



class car:
    def __init__(self,model,year,seller_num,colour):
        self.model = model
        self.year = year
        self.seller_num = seller_num
        self.colour = colour

    def drive(self):
        print(f"you can now drive your very own:{self.colour} {self.model}")


car1 = car("mustang",2024,123_45678, "blue")
car2 = car("BMW",2012,543234,"black")
while True:
    choice = input("Which car would you like car1 or car2: ")
    if choice == "car1":
        print("Great choice!")
        print(f"Your car is {car1.model}")
        print(f"Your model is {car1.year}")
        print(f"Your seller_ number is {car1.seller_num}")
        print(f"cars colour: {car1.colour}")
        car1.drive()
    elif choice == "car2":
        print("Great choice!")
        print(f"Your car is {car2.model}")
        print(f"Your model is {car2.year}")
        print(f"Your seller_ number is {car2.seller_num}")
        print(f"cars colour: {car2.colour}")
        car2.drive()
    elif " " in choice:
        print("There can be no spaces in your input")
        continue
    else:
        print("Car not available")
        continue
    break



# INHERITANCE AND CLASS FIRST PROGRAM

class inheritance:
    def __init__(self,name,eyes,mouth):
        self.name = name
        self.eyes = eyes
        self.mouth = mouth


    def eat(self):
        print(f"{self.name} can eat")
    def sleep(self):
        print(f"{self.name} can sleep")

class dog(inheritance):
   def sound(self):
       print("WOOF")
class cat(inheritance):
    def sound(self):
        print("MEOW")



Dog = dog("scoobie","blue","big")
Cat = cat("Crookshanks","red","small")
print(f"the name of the dog is {Dog.name},his eyes are {Dog.eyes} and his mouth is {Dog.eyes} ")
print(f"the name of the cat is {Cat.name},his eyes are {Cat.eyes} and his mouth is {Cat.eyes} ")
Dog.eat()
Dog.sleep()
Dog.sound()
Cat.eat()
Cat.sleep()
Cat.sound()



# FIRST MULTIPLE INHERITANCEPROGRAM

class animal():
    def __init__(self,name):
        self.name = name
    def eat(self):
        print(f"can eat")
    def sleep(self):
        print(" can sleep")



class predetor(animal):
    def hunt(self):
        print(f" can hunt   ")
        print(f" higher than its prey in the food chain")

class prey(animal):
    def flee(self):
        print(f" it can run")
        print(f" it has defense mechanisms  ")

class cat(predetor):
   def sound(self):
       print(f" makes the sound MEOW")
class bird(predetor):
    def sound(self):
        print(f" makes the sound CHIRP")
class mouse(predetor,prey):
    def sound(self):
        print(f" makes the sound SQUEEK")
class worm(predetor,prey):
    def sound(self):
        print(f" makes the sound SLITHER..")


cat1 = cat("Crookshanks")
bird1 = bird("Hedwig")
mouse1 = mouse("Scabbers")
worm1 = worm("Trevor")
while True:
    choice = input("Wha animal would you like information about (cat,bird,mouse or worm)? ").lower()
    if  choice.isalpha():

        if choice == "cat":
            print(f"His name is {cat1.name} ")
            cat1.sleep()
            cat1.eat()
            cat1.hunt()
            cat1.sound()
            break
        elif choice == "bird":
            print(f"His name is {bird1.name} ")
            bird1.sleep()
            bird1.eat()
            bird1.hunt()
            bird1.sound()
            break
        elif choice == "mouse":
            print(f"His name is {mouse1.name} ")
            mouse1.sleep()
            mouse1.eat()
            mouse1.hunt()
            mouse1.sound()
            break
        elif choice == "worm":
            print(f"His name is {worm1.name} ")
            worm1.sleep()
            worm1.eat()
            worm1.hunt()
            worm1.sound()
            break
        else:
            print("Animal not available")
            continue


# BASIC DUCK TYPEING


class animals():
    alive = True

class dog(animals):
    def speak(self):
        print("Woof")

class cat(animals):
    def speak(self):
        print("MEOW")

class car(animals):
    alive = False
    def speak(self):
        print("HONK")

animals =  [dog(),cat(),car()]
for animal in animals:
    animal.speak()
    print(animal.alive)



#BASIC FILE READING PROGRAM


file_path = "C:/Users/Solar Turbines User/OneDrive/Desktop/hogwarts.csv"

try:
    with open(file_path, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("this file does not exist")
except PermissionError:
    print("Permission error")



# ALARM CLOCK PROGRAM


import time
import datetime
import winsound

def alarm(alarm_time):
    print(f"Your alarm time is {alarm_time} ")

    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        time.sleep(1)
        if alarm_time == current_time:
            print("WAKE UP!")
            for i in range(5):
                winsound.Beep(1000, 1000)

            is_running= False


if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    alarm(alarm_time)



# POKEMON API PROGRAM NOT A PROJECT!!!!

import requests
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)
    if response.status_code  ==  200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print("FAHHHHHH")


pokemon_name = input("Enter the name of the pokemon: ")
pokemon_info = get_pokemon_info(pokemon_name)

try :
    if pokemon_info:
        what = input(f"What would you like to know about {pokemon_name}: ")
        print(f"{pokemon_info[what]}")

except KeyError:
    print("INVALID KEY INPUT")



# PyQt5 Concepts program

import sys
from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,
                             QWidget,QHBoxLayout,QVBoxLayout,
                             QGridLayout,QPushButton,QCheckBox,
                             QRadioButton,QButtonGroup,QLineEdit)
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("relearning PyQt5")
        self.setGeometry(0,0,1800,1500)
        self.setWindowIcon(QIcon("Top_5_digital_marketing_trends_in_2024_12Grids.webp"))


        self.initUI()
    def initUI(self):

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        color1 = QLabel("#1",self)
        color2 = QLabel("#2", self)
        color3 = QLabel("#3", self)
        color4 = QLabel("#4", self)
        color5 = QLabel("#5", self)

        color1.setStyleSheet("background-color:black;")
        color2.setStyleSheet("background-color:white;")
        color3.setStyleSheet("background-color:black;")
        color4.setStyleSheet("background-color:white;")
        color5.setStyleSheet("background-color:black;")

        Qbox = QGridLayout()

        Qbox.addWidget(color1,0,0)
        Qbox.addWidget(color2,0,1)
        Qbox.addWidget(color3,0,0)
        Qbox.addWidget(color4,0,1)
        Qbox.addWidget(color5,1,1)

        central_widget.setLayout(Qbox)

        self.checkbox1 = QCheckBox("IS AOT SAD ", self)
        self.checkbox2 = QCheckBox("is levi the goat ", self)
        self.checkbox3 = QCheckBox("ervin over armin? ", self)

        self.checkbox1.setGeometry(270, 630, 200, 200)
        self.checkbox2.setGeometry(270, 670, 400, 200)
        self.checkbox3.setGeometry(270, 710, 400, 200)

        self.checkbox1.setStyleSheet("color:#0053d9;"
                                     "font-size: 30px")
        self.checkbox2.setStyleSheet("color:#0053d9;"
                                     "font-size: 30px")
        self.checkbox3.setStyleSheet("color:#0053d9;"
                                     "font-size: 30px")

        self.checkbox1.stateChanged.connect(self.check_box_checked)


        image = QLabel(self)
        image.setGeometry(270, 300, 500, 300)
        image.setScaledContents(True)
        pixmap = QPixmap("Top_5_digital_marketing_trends_in_2024_12Grids.webp")
        image.setPixmap(pixmap)

        label = QLabel("PYQT5", self)
        label.setFont(QFont("italic", 30))
        label.setGeometry(0, 0, 1900, 1800)
        label.setStyleSheet(
            "color:blue;"
            "font-weight:bold;"
            "font-style:italic;"
            "text-decoration:underline;"
        )
        label.setAlignment(Qt.AlignHCenter)

        self.button = QPushButton("click me ",self)
        self.button.setGeometry(270,600,500,100)
        self.button.clicked.connect(self.click_button)


        self.radio1 = QRadioButton("Mikasa",self)
        self.radio2 = QRadioButton("Armin", self)
        self.radio3 = QRadioButton("Eren", self)
        self.radio4 = QRadioButton("Erwin", self)
        self.radio5 = QRadioButton("Levi", self)

        self.radio1.setGeometry(1000,100,200,50)
        self.radio2.setGeometry(1000, 200, 200, 50)
        self.radio3.setGeometry(1000, 300, 200, 50)
        self.radio4.setGeometry(1000, 400, 200, 50)
        self.radio5.setGeometry(1000, 490, 200, 50)

        self.radio1.setStyleSheet("font-size:20px")
        self.radio2.setStyleSheet("font-size:20px")
        self.radio3.setStyleSheet("font-size:20px")
        self.radio4.setStyleSheet("font-size:20px")
        self.radio5.setStyleSheet("font-size:20px")

        self.radio1.raise_()
        self.radio2.raise_()
        self.radio3.raise_()
        self.radio4.raise_()
        self.radio5.raise_()

        self.button_group1 = QButtonGroup(self)
        self.button_group2 = QButtonGroup(self)

        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radio_button_clicked)
        self.radio2.toggled.connect(self.radio_button_clicked)
        self.radio3.toggled.connect(self.radio_button_clicked)
        self.radio4.toggled.connect(self.radio_button_clicked)
        self.radio5.toggled.connect(self.radio_button_clicked)


        self.textbox1 = QLineEdit(self)
        self.textbox2 = QLineEdit(self)
        self.textbox3 = QLineEdit(self)
        self.textbox4 = QLineEdit(self)
        self.textbox5 = QLineEdit(self)

        self.textbox1.setGeometry(1100,500,200,50)
        self.textbox1.setStyleSheet("font-size: 20px")

        self.textbox2.setGeometry(1100, 600, 200, 50)
        self.textbox2.setStyleSheet("font-size: 20px")

        self.textbox3.setGeometry(1100, 700, 200, 50)
        self.textbox3.setStyleSheet("font-size: 20px")

        self.textbox4.setGeometry(1100, 800, 200, 50)
        self.textbox4.setStyleSheet("font-size: 20px")

        self.textbox5.setGeometry(1100, 900, 200, 50)
        self.textbox5.setStyleSheet("font-size: 20px")

        self.textbox1.setPlaceholderText("Enter an AOT charecter")
        self.textbox2.setPlaceholderText("Enter an AOT charecter")
        self.textbox3.setPlaceholderText("Enter an AOT charecter")
        self.textbox4.setPlaceholderText("Enter an AOT charecter")
        self.textbox5.setPlaceholderText("Enter an AOT charecter")

        self.button_for_textbox1 = QPushButton("Submit",self)
        self.button_for_textbox2 = QPushButton("Submit", self)
        self.button_for_textbox3 = QPushButton("Submit", self)
        self.button_for_textbox4 = QPushButton("Submit", self)
        self.button_for_textbox5 = QPushButton("Submit", self)

        self.button_for_textbox1.setGeometry(1300,500,200,50)
        self.button_for_textbox2.setGeometry(1300, 600, 200, 50)
        self.button_for_textbox3.setGeometry(1300, 700, 200, 50)
        self.button_for_textbox4.setGeometry(1300, 800, 200, 50)
        self.button_for_textbox5.setGeometry(1300, 900, 200, 50)

        self.button_for_textbox1.clicked.connect(self.textbox_button_clicked)
        self.button_for_textbox2.clicked.connect(self.textbox_button_clicked)
        self.button_for_textbox3.clicked.connect(self.textbox_button_clicked)
        self.button_for_textbox4.clicked.connect(self.textbox_button_clicked)
        self.button_for_textbox5.clicked.connect(self.textbox_button_clicked)











    def textbox_button_clicked(self):
            button = self.sender()

            if button == self.button_for_textbox1:
                print(self.textbox1.text())

            elif button == self.button_for_textbox2:
                print(self.textbox2.text())

            elif button == self.button_for_textbox3:
                print(self.textbox3.text())

            elif button == self.button_for_textbox4:
                print(self.textbox4.text())

            elif button == self.button_for_textbox5:
                print(self.textbox5.text())


    def radio_button_clicked(self):
        button_pressed = self.sender()
        if button_pressed.isChecked():
            print(f"{button_pressed.text()} was pressed")

    def check_box_checked(self,state):
        print("CRYING EMOJI")

    def click_button(self):
        print("THE HOGWARTS CHAMPION")
        self.button.setText("Welcome")
        self.button.setDisabled(True)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


# DIGITAL CLOCK PROGRAM


import sys
from wsgiref.util import application_uri

from PyQt5.QtWidgets import (QApplication,QMainWindow,QLabel,
                             QWidget,QHBoxLayout,QVBoxLayout,
                             QGridLayout,QPushButton,QCheckBox,
                             QRadioButton,QButtonGroup,QLineEdit,
                             QHBoxLayout)
from PyQt5.QtGui import QIcon,QFont,QPixmap
from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtGui import QFont,QFontDatabase

class Digitalclock(QWidget):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        self.label_time = QLabel(self)
        self.initUI()


    def initUI(self):
        self.setWindowTitle("Digital clock")
        self.setGeometry(320,300,700,500)
        vbox = QVBoxLayout()
        vbox.addWidget(self.label_time)
        self.setLayout(vbox)
        self.label_time.setAlignment(Qt.AlignCenter)
        self.label_time.setStyleSheet("color:#bfab75")
        self.setStyleSheet("background-color:black")

        font_id = QFontDatabase.addApplicationFont("DS-DIGI.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font_choice = QFont(font_family,150)
        self.label_time.setFont(font_choice)


        self.update_time()

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)



    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.label_time.setText(current_time)






def main():
    app = QApplication(sys.argv)
    clock = Digitalclock()
    clock.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()



# STOPWATCH PROGRAM


import sys
from wsgiref.util import application_uri

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QGridLayout, QPushButton, QCheckBox,
                             QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, )
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase


class stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00:00")
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.setGeometry(600, 300, 800, 500)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Stop watch")
        self.setWindowIcon(QIcon("william-warby-VwqMTcsb0Tg-unsplash.jpg"))

        vbox = QVBoxLayout()

        vbox.addWidget(self.time_label)

        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("""
        QPushButton{
        font-size:50px;
        font-style:italic;
        padding:20px;
        color:#03ff24; 
        background-color:black;
        }
        QLabel{
        font-size:150px;
        color:hsl(128, 100%, 51%);
        font-style:italic;
        background-color:hsl(128, 3%, 5%);
        }
         QPushButton:hover{
        font-size:50px;
        font-style:italic;
        color:#03ff24; 
        background-color:hsl(120, 4%, 80%)

        }



        """)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)

        vbox.addLayout(hbox)

        self.start_button.clicked.connect(self.start_stopwatch)
        self.stop_button.clicked.connect(self.Stop_stopwatch)
        self.reset_button.clicked.connect(self.reset_stopwatch)
        self.timer.timeout.connect(self.update_dsplay)

    def start_stopwatch(self):
        self.timer.start(10)

    def Stop_stopwatch(self):
        self.timer.stop()

    def reset_stopwatch(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_stopwatch_time(self.time))

    def format_stopwatch_time(self, time):
        hours = time.hour()
        min = time.minute()
        sec = time.second()
        milisec = time.msec() // 10

        return f"{hours:02}:{min:02}:{sec:02}:{milisec:02}"

    def update_dsplay(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_stopwatch_time(self.time))


def main():
    app = QApplication(sys.argv)
    clock = stopwatch()
    clock.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()




# WEATHER API PROGRAM   (LAST ONE FROM BRO CODE)


import sys
from wsgiref.util import application_uri
import requests

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QGridLayout, QPushButton, QCheckBox,
                             QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, )
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase


# 5fe60d5f637dd307eb03dc293c117a82

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.title_label = QLabel("Weather app", self)
        self.weather_label = QLabel("Enter your city name ", self)
        self.weather_textbox = QLineEdit(self)
        self.weather_button = QPushButton("Get weather", self)
        self.temp_label = QLabel(self)
        self.description_weather = QLabel(self)
        self.emoji_label = QLabel(self)

        self.init()

    def init(self):
        self.setWindowIcon(QIcon("william-warby-VwqMTcsb0Tg-unsplash.jpg"))
        self.setWindowTitle("Weather app")
        self.setGeometry(570, 300, 800, 500)

        vbox = QVBoxLayout()

        vbox.addWidget(self.title_label)
        vbox.addWidget(self.weather_label)
        vbox.addWidget(self.weather_textbox)
        vbox.addWidget(self.weather_button)
        vbox.addWidget(self.description_weather)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)

        self.setLayout(vbox)

        self.title_label.setAlignment(Qt.AlignCenter)
        self.weather_label.setAlignment(Qt.AlignCenter)
        self.weather_textbox.setAlignment(Qt.AlignCenter)
        self.description_weather.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)

        self.title_label.setObjectName("title_label")
        self.weather_label.setObjectName("weather_label")
        self.weather_textbox.setObjectName("weather_textbox")
        self.weather_button.setObjectName("weather_button")
        self.description_weather.setObjectName("description_weather")
        self.temp_label.setObjectName("temp_label")
        self.emoji_label.setObjectName("emoji_label")

        self.setStyleSheet("""
        QLabel,QPushButton{
        font-family:calibri;
        font-style:italic;
        }
        QLabel#title_label{
        font-size:70px;
        font-weight:bold;
        }
        QLabel#weather_label{
        font-size:35px;
        }
        QLineEdit#weather_textbox{
        font-size:30px;
        padding:15px;  
        }
        QPushButton#weather_button{
        font-size:25px;
        padding:15px;
        }
        QLabel#description_weather{
        font-size:50px;
        }
        QLabel#temp_label{
         font-size:50px;
        }
        QLabel#emoji_label{
        font-size:100px;
        }

                """)

        self.weather_button.clicked.connect(self.get_weather)

    def get_weather(self):

        try:
            api = "5fe60d5f637dd307eb03dc293c117a82"
            city = self.weather_textbox.text()
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            if data["cod"] == 200:
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:

            match response.status_code:
                case 400:
                    self.display_error("Bad request\nPlease check your input")
                case 401:
                    self.display_error("Unauthorized\nInvalid API key")
                case 403:
                    self.display_error("Forbidden\nAccess is denied")
                case 404:
                    self.display_error("Not found\nCity not found")
                case 500:
                    self.display_error("Internal server error\nPlease try again later")
                case 502:
                    self.display_error("Bad gateway\nInvalid response frm the server")
                case 503:
                    self.display_error("Server unavailable\nServer is down")
                case 504:
                    self.display_error("Gateway timeout\npNo response from server")
                case _:
                    self.display_error(f"HTTP error occured\n{http_error}")


        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error\nConnection is lost")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects\nCheck the url")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request error\n{req_error}")

    def display_error(self, message):

        self.description_weather.setText(message)
        self.emoji_label.clear()
        self.temp_label.clear()

    def display_weather(self, data):
        temp_value = data["main"]["temp"]
        self.description_weather.setText(f"{temp_value:.0f} Degrees Celsius ")

        temp_description = data["weather"][0]["description"]
        self.temp_label.setText(f"{temp_description}")

        weather_id = data["weather"][0]["id"]
        self.emoji_label.setText(self.emoji_weatherapp(weather_id))

    @staticmethod
    def emoji_weatherapp(weather_id):

        if weather_id >= 200 and weather_id <= 232:
            return "⛈️"
        elif weather_id >= 100 and weather_id <= 321:
            return "⛅"
        elif weather_id >= 500 and weather_id <= 531:
            return "🌧️"
        elif weather_id >= 600 and weather_id <= 622:
            return "🌨️"
        elif weather_id >= 701 and weather_id <= 741:
            return "🌫️"
        elif weather_id == 762:
            return "🌋"
        elif weather_id == 771:
            return "💨"
        elif weather_id == 781:
            return "🌪️"
        elif weather_id == 800:
            return "☀️"
        elif weather_id >= 801 and weather_id <= 804:
            return "☁️"
        else:
            return ""


def main():
    app = QApplication(sys.argv)
    weathapp = WeatherApp()
    weathapp.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()




# Calculator app


import sys
import requests

from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
                             QWidget, QHBoxLayout, QVBoxLayout,
                             QGridLayout, QPushButton, QCheckBox,
                             QRadioButton, QButtonGroup, QLineEdit,
                             QHBoxLayout, )
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator app")
        self.setWindowIcon(QIcon("charlesdeluvio-GlavtG-umzE-unsplash.jpg"))
        self.setGeometry(700, 50, 600, 1000)
        self.expression = ""
        self.initUI()



    def initUI(self):
        #display box
        self.display = QLineEdit(self)
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setGeometry(0,0,600,100)


        # number buttons

        self.button1 = QPushButton("1",self)
        self.button2 = QPushButton("2", self)
        self.button3 = QPushButton("3", self)
        self.button4 = QPushButton("4", self)
        self.button5 = QPushButton("5", self)
        self.button6 = QPushButton("6", self)
        self.button7 = QPushButton("7", self)
        self.button8 = QPushButton("8", self)
        self.button9 = QPushButton("9", self)
        self.button0 = QPushButton("0", self)

        # operators buttons
        self.equals_to = QPushButton("=",self)
        self.decimal = QPushButton(".",self)
        self.backspace = QPushButton("⌫",self)
        self.clear = QPushButton("C",self)
        self.add = QPushButton("+",self)
        self.subtract = QPushButton("-",self)
        self.multiply = QPushButton("x",self)
        self.divide = QPushButton("÷",self)
        self.remainder = QPushButton("%",self)
        self.square = QPushButton("x²",self)



        grid = QGridLayout()

        grid.addWidget(self.clear,0,0)
        grid.addWidget(self.backspace,0,1)
        grid.addWidget(self.remainder,0,2)
        grid.addWidget(self.divide,0,3)
        grid.addWidget(self.button1,1,0)
        grid.addWidget(self.button2,1,1)
        grid.addWidget(self.button3,1,2)
        grid.addWidget(self.add,1,3)
        grid.addWidget(self.button4,2,0)
        grid.addWidget(self.button5,2,1)
        grid.addWidget(self.button6,2,2)
        grid.addWidget(self.subtract,2,3)
        grid.addWidget(self.button7,3,0)
        grid.addWidget(self.button8,3,1)
        grid.addWidget(self.button9,3,2)
        grid.addWidget(self.multiply,3,3)
        grid.addWidget(self.square,4,0)
        grid.addWidget(self.decimal,4, 1)
        grid.addWidget(self.button0,4,2)
        grid.addWidget(self.equals_to,4,3)

        self.setLayout(grid)
        grid.setSpacing(0)


        #display box continue

        vbox = QVBoxLayout()
        vbox.setSpacing(0)
        vbox.setContentsMargins(0,0,0,0)

        vbox.addWidget(self.display)

        self.setLayout(vbox)

        self.setStyleSheet("""
        QWidget{
        background-color:black;
        }
        QPushButton{
        padding:25px;
        font-size:25px;
        background-color:#568896;
        color:#b0cad1;
        }
        QLineEdit{
        background-color:#568896;
        font-size:25px;
        color:#b0cad1;
        }
        """)



        self.button1.clicked.connect(lambda: self.pressed("1"))
        self.button2.clicked.connect(lambda: self.pressed("2"))
        self.button3.clicked.connect(lambda :self.pressed("3"))
        self.button4.clicked.connect(lambda: self.pressed("4"))
        self.button5.clicked.connect(lambda :self.pressed("5"))
        self.button6.clicked.connect(lambda: self.pressed("6"))
        self.button7.clicked.connect(lambda: self.pressed("7"))
        self.button8.clicked.connect(lambda: self.pressed("8"))
        self.button9.clicked.connect(lambda: self.pressed("9"))
        self.button0.clicked.connect(lambda: self.pressed("0"))

        #Operators

        self.add.clicked.connect(lambda :self.pressed("+"))
        self.subtract.clicked.connect(lambda: self.pressed("-"))
        self.multiply.clicked.connect(lambda: self.pressed("*"))
        self.divide.clicked.connect(lambda: self.pressed("/"))
        self.square.clicked.connect(lambda : self.pressed ("**2"))
        self.remainder.clicked.connect(lambda: self.pressed("%"))
        self.decimal.clicked.connect(lambda: self.pressed("."))

        #Other operators

        self.equals_to.clicked.connect(lambda : self.calculate())
        self.backspace.clicked.connect(lambda: self.do_backspace())
        self.clear.clicked.connect(lambda: self.clear_space())



    def pressed(self, value):
        self.expression += value
        self.display.setText(self.expression)



    def calculate(self):
        try:
            result = eval(self.expression)
            self.display.setText(str(result))
            self.expression = str(result)

        except:
            self.display.setText("error")
            self.expression = ""


    def do_backspace(self):
        self.expression = self.expression[:-1]
        self.display.setText(self.expression)

    def clear_space(self):
        self.expression = ""
        self.display.setText(self.expression)


def main():
    app = QApplication(sys.argv)
    calculator = CalculatorApp()
    calculator.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


