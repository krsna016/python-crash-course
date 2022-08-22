# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # CHAPTER_1 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# print("HELLO WORLD")
# # print"HELLO_WORLD"
# print("IT's THE SENTENCE")
# print("Python's First Program")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # CHAPTER_2 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# var1 = "HELLO PYTHON WORLD"
# print(var1)
# simple_message = "Hello There"
# print(simple_message)
# simple_messages = "what happens"
# print(simple_messages)
# simple_messages = "Keep it up"
# print(simple_messages)

# string1 = "This is a string"
# string2 = "This is also a string."
# string3 = "I told my friend, 'Python is my favourite language!' "
# string4 = 'The language "Python" is named after Monty Python, not the snake.'
# string5 = "One of Python's strengths is its diverse and supportive community."
# print(string1)
# print(string2)
# print(string3)
# print(string4)
# print(string5)

# name = "anurag pareek"
# print(name.title())

# name_1 = "Its Ok"
# print(name_1.upper())
# print(name_1.lower())

# first_name = "anurag"
# last_name = "pareek"
# full_name = first_name +" "+last_name
# # print("Hello, "+ full_name.title() +"!")
# message = "Hello, "+ full_name.title() +"!"
# print(message)

# name_2 = "Anurag\tpareek\nWhat are you doing\t\nHello\n\tThere"
# print(name_2)

# name_3 = "   Anurag     "
# name_4 = "**"
# total_name = name_3+name_4
# total_name1 = name_3+name_4
# total_name1 = name_3.rstrip()+name_4
# total_name2 = name_3.lstrip()+name_4
# total_name3 = name_3.strip()+name_4
# print(total_name1)
# print(total_name1)
# print(total_name2)
# print(total_name3)

# name_5 = '   Anurag   '
# print(name_5)
# print(name_5.lstrip())
# print(name_5.rstrip())  # WE NEED TO STORE THE STRIP VALUE IN NEW VARIABLE AS SPACES ONLY REMOVES TEMPORARITY.
# print(name_5.strip())
# print(name_5)

# name_1 = "Hello There's"
# print(name_1)
# name_2 = 'Hello There's'
# print(name_2)

# name_person = "AnUrag"
# message_person = "Hello "+name_person+", would you like to learn some Python today?"
# print(message_person) 
# print(name_person.title())
# print(name_person.upper())
# print(name_person.lower())

# name_1 = 'Albert Einstein once said, "A person who never made a mistake never tried anything new.'
# print(name_1)
# name_2 = "Albert Einstein"
# message = 'once said, "A person who never made a mistake never tried anything new.'
# print(name_2+" "+message)

# name_1 = "       Anurag     "
# name_2 = ".."
# a=(name_1)
# b=(name_1.lstrip())
# c=(name_1.rstrip())
# d=(name_1.strip())
# print(a+name_2)
# print(b+name_2)
# print(c+name_2)
# print(d+name_2)

# print(2+3)
# print(2*3)
# print(2/3)
# print(2-3)
# print(2**3)
# print(0.1+0.1)
# print(1.1+0.1)
# print(2.1*2.1)
# print(0.1*0.2)

# name_1 = 23
# name_2 = "IS THE INTEGER"
# total_1 = str(name_1) +" "+ name_2
# print(total_1)
# # ALSO:
# name_1 = "23"
# name_2 = "IS THE INTEGER"
# total_1 = name_1 +" "+ name_2
# print(total_1)
# # BUT NOT:
# name_1 = 23
# name_2 = "IS THE INTEGER"
# total_1 = name_1 +" "+ name_2
# print(total_1)

# print(5+3)
# print(13-5)
# print(2*4)
# print(16/2)

# var1 = 29
# var2 = 'MY FAVOURITE NUMBERS IS : '+str(var1)
# print(var2)

# #ADD TWO NUMBERS:
# a = 1
# b = 2
# add_numbers = a + b
# print(add_numbers)
# # CONCATENATE THE STRINGS:
# first_name = "ANURAG"
# last_name = "PAREEK"
# full_name = first_name+" "+last_name
# print(full_name)

# import this # WHEN WE RUN THIS CODE IT WILL PRINT SOME LINES BY "TIM PETERS" ABOUT CODING SKILLS.

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # CHAPTER_3 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# list_1 = ['Anurag','krsna','radhe']
# print(list_1)
# print(list_1[0])
# print(list_1[1])
# print(list_1[2].title())
# print(list_1[-1])
# message = "My friend name is "+list_1[1].title()
# print(message)

# name_1 = ['anurag','Krsna']
# name_1[1]='Radhe'
# print(name_1)
# name_1.append('KRSNA')
# print(name_1)
# name_1.insert(1,'Hare')
# print(name_1)
# print(len(name_1)) # ANS: 4 I.E FOUR ITEMS IN THE LIST

# list_1 = []
# print("** LIST CAN ONLY CONTAIN 4 ELEMENTS **")
# while len(list_1) < 3:
#     n = input(f"{len(list_1)} : PLEASE APPEND THE DATA IN THE LIST : ")
#     list_1.append(n)
# print(f"YOUR LIST IS : {list_1}")
# print(len(list_1))

# list_1 = []
# print("** LIST CAN ONLY CONTAIN 4 ELEMENTS **")
# while len(list_1) < 3:
#     n = input(f"{(len(list_1))+1} : PLEASE APPEND THE DATA IN THE LIST : ")
#     i = int(input("ENTER THE INDEX WHERE YOU WANT TO INSERT THE ENTRY : "))
#     list_1.insert(i,n)
# print(f"YOUR LIST IS : {list_1}")
# print(len(list_1))

# list_1 = ['anurag','pareek',10]
# del(list_1[0])
# print(list_1)

# list_1 = ['anurag','pareek','krsna']
# list_1.pop() # IF WE DON'T PASS ANY VALUE TO THE POP() THEN IT WILL REMOVE THE ELEMENT FROM THE END
# print(list_1)
# print(list_1.pop())  # IN THIS WAY WE CAN GET THE POPPED DATA AND IF WE WANT WE CAN SAVE THIS TO OTHER VARIABLE AND ACCESS IT LATER

# list_1 = ['anurag','pareek','krsna']
# # list_1.pop(1)
# # print(list_1)
# list_1.remove('anurag')
# print(list_1)

# list_1 = ['anurag','pareek','krsna']
# temp = "krsna"
# list_1.remove(temp)
# print(list_1)
# print(f"{temp} is my best friend")

# # INVITING PEOPLE
# invite_people = []
# while len(invite_people)< 3:
#     input_name_people = input("ENTER THE NAMES OF THE PEOPLE TO INVITE : ")
#     invite_people.append(input_name_people)
# print(f"THE LIST OF THE PEOPLE TO INVITE IS {invite_people}")
# # ONE OF THE PERSON CAN'T COME
# removing_person = input("ENTER THE NAME OF THE PERSON WHO CAN'T COME FOR THE DINNER :  ")
# new_person = input("ENTER THE NAME FOR THE NEW MEMBER FOR THE DINNER : ")
# invite_people.remove(removing_person)
# invite_people.append(new_person)
# # HERE WE HAVE FOUND A BIGGER DINING TABLE 
# while len(invite_people)<6:
#     input_name_people = input("ENTER THE NAMES OF THE PEOPLE TO INVITE AS YOU GET A BIGGER DINING TABLE : ")
#     i = int(input("ENTER THE INDEX WHERE YOU WANT THAT PERSON TO BE PLACED IN THE LIST : "))
#     invite_people.insert(i,input_name_people)
# # SORRY I CAN INVITE ONLY TWO PEOPLE AS LARGE DINING TABLE NOT ARRIVE AT THIS TIME 
# popped_person = []
# for k in range(1,5):
#     popped_out = invite_people.pop()
#     popped_person.append(popped_out)
# # SAYING SORRY TO THE PERSON ABOUT THE MISTAKE
# for j in popped_person:
#     print(f"{j.upper()}, YOU'RE SORRY YOU ARE NOT INVITED TO THE DINNER !!!")
# # MESSAGES TO INVITED PEOPLE
# for i in invite_people:
#     print(f"{i.upper()}, YOU ARE HERE INVITED FOR THE DINNER AT 8:00 PM TONIGHT!")
# print(f"!! I HAVE ONLY INVITED {len(invite_people)} PEOPLE AT THE DINNER PARTY !!")

# list_1 = ['krsna','radha','anurag','pareek']
# list_1.sort() # WHEN WE STORE THIS VALUE IN A VARIABLE AND PRINT THAT VARIABLE IT PRINTS NONE MEANS IT PERMANENTLY CHANGES THE ORDER ALSO IT'S A METHOD
# print(list_1)
# list_1.sort(reverse=True)
# print(list_1)
# print(list_1)

# list_1 = ['krsna','radha','anurag','pareek']
# a =  sorted(list_1)  # # WHEN WE STORE THIS VALUE IN A VARIABLE AND PRINT THAT VARIABLE OTHERWISE NOT IT PRINTS THAT VARIABLE MEANS IT TEMPORARILY CHANGES THE ORDER ALSO IT'S A FUNCTION
# print(list_1)
# b = sorted(list_1,reverse = True)
# print(b)
# print(list_1)

# name = ['krsna','radha','anurag','pareek']
# name.reverse() # WHEN WE STORE THIS VALUE IN A VARIABLE AND PRINT THAT VARIABLE IT PRINTS NONE MEANS IT PERMANENTLY CHANGES THE ORDER ALSO IT'S A METHOD
# print(name)

# name = ['krsna','radha','anurag','pareek']
# print(name[1])
# print(name[4]) # HERE INDEX ERROR WILL COME

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # CHAPTER_4 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# list_1 = ['a','b','c','d','e']
# for alphas in list_1:
#     print("HELLO, "+alphas+"\nNice to meet you "+alphas)
# print("Ok bye, "+alphas) # IT PRINT e  AT LAST BECOUSE alphas VARIABLE AT LAST HAVE e STORED IN IT
# print("THANK YOU EVERY ONE !!")    

# for i in range(1,6):
#     print(i)

# number = list(range(-10,1))
# number_1 = list(range(1,10))
# print(number)
# print(number_1)

# numbers = list(range(2,11,2))
# print(numbers)

# numbers = list(range(1,11))
# for nums in numbers:
#     print(nums**2,end=" ")

# numbers = list(range(1,11))
# square_numbers = []
# for i in numbers:
#     square_numbers.append(i**2)
# print(square_numbers)

# list_1 = list(range(1,10000000))
# print(max(list_1))
# print(min(list_1))
# print(sum(list_1))

# square_no = [num**2 for num in range(1,11)]
# print(square_no)

# count = [num for num in range(1,21)]
# print(count)

# million_numbers = [num for num in range(1,1000000+1)]
# print(min(million_numbers))
# print(max(million_numbers))
# print(sum(million_numbers))

# odd_number = [num for num in range(1,21,2)]
# for i in odd_number:
#     print(i,end=" ")

# multiple_of_three = [num if num%3==0 else None for num in range(1,31)]
# print(multiple_of_three)

# multiple_of_three = [num for num in range(3,31,3)]
# print(multiple_of_three)

# cube_no = list(range(1,11))
# for i in cube_no:
#     print(i**3,end=" ")
# print()

# cube_number = [i**3 for i in range(1,11)]
# print(cube_number)

# list_1 = ['a','b','c','d','e','f','g']
# print(list_1[0:3])
# print(list_1[1:3])
# print(list_1[0:])
# print(list_1[2:]) 
# print(list_1[:3]) # FIRST THREE ITEMS
# print(list_1[-3:]) # LAST THREE ITEMS
# for i in list_1[2:5]:
#     print("Hello,"+i.title(),end=" ")

# my_foods = ['a','b','c','d','e','f']
# print(my_foods)
# friends_foods = my_foods[:]    # FIRST METHOD TO COPY A LIST
# print(friends_foods)
# my_foods.append("Hello")
# print(my_foods)
# print(friends_foods)

# my_foods = ['a','b','c','d','e','f','g']
# print("THE FIRST THREE ITEMS OF THE LIST ARE : ",end=" ")
# print(my_foods[:3])
# print("THE MIDDLE THREE ITEMS OF THE LIST ARE : ",end=" ")
# print(my_foods[2:5])
# print("THE LAST THREE ITEMS OF THE LIST ARE : ",end=" ")
# print(my_foods[-3:])

# dimension = (720 , 1080)
# print(dimension[0])
# print(dimension[1])
# # dimension[1] = 90
# # print(dimension)

# dimensions = (20,50)
# print("ORIGINAL DIMENTIONS : ",end= " ")
# for i in dimensions:
#     print(i, end= " ")
# print()
# dimensions = (30,60)
# print("MODIFIED DIMENTIONS : ",end= " ")
# for j in dimensions:
#     print(j, end= " ")
# print()

# food_items = ('pizza','burgur','dossa','sandwitch','cake')
# print("THE ITEMS OFFERED BY THE RESTAURANT : ")
# for i in food_items:
#     print(i.title())
# # food_items[1] = "Pastta"
# # print(food_items)
# a = list(food_items)
# a [1]= "DalFry"
# a [2]= "Rice"
# print(tuple(a))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # CHAPTER_5 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# for car in cars:
#     if car == "bmw":
#         print(car.upper()) # ALSO WE CAN WRITE : print("BMW")
#     else:
#         print(car.title())

# # CONDITIONAL TEST:
# car = "bmw"
# car_1 = "farari"
# print(car=="bmw")
# print(car_1=="alto")

# car = "Audi"
# print(car.lower()=="audi")
# print(car == "audi")

# requested_toppings = "Mushroom"
# if requested_toppings != "Anchovies":
#     print("Hold the Anchovies !")

# total = 56
# if total != 70:
#     print("YOUR COUNTING IS WRONG!")

# age = 18
# age_1 = 20
# print(age >10 and age_1<18)
# print(age >10 and age_1>18)

# age = 18
# age_1 = 20
# print(age >10 or age_1<18)
# print(age >10 and age_1>18)
# print(age <10 and age_1<18)

# cars = ['audi', 'bmw', 'subaru', 'toyota']
# print("audi" in cars)
# print("buffalo" in cars)
# print("buffalo" not in cars)
# print("audi" not in cars)

# banned_users = ['andrew', 'carolina', 'david']
# if "anurag" not in banned_users:
#     print("anurag "+",you can send your response")
# else:
#     print("you cannot send your response")

# name = "KRSNA"
# name_1 = "RADHA"
# name_2 = "SHIV"
# name_3 = "VISNU"
# name_4 = "BHRAMA"
# a = (name == "KRSNA" or name_1 == "RADHA" or name_2 == "SHIV" or name_3 == "VISNU" or name_4 == "BHRAMA")
# b = (name != "KRSNA" or name_1 != "RADHA" or name_2 != "SHIV" or name_3 != "VISNU" or name_4 != "BHRAMA")
# print(f"IS NAME == 'KRSNA'.I THINK TRUE?")
# print(a)
# print(f"IS NAME == 'RADHA'.I THINK TRUE?")
# print(a)
# print(f"IS NAME == 'SHIV'.I THINK TRUE?")
# print(a)
# print(f"IS NAME == 'VISNU'.I THINK TRUE?")
# print(a)
# print(f"IS NAME == 'BHRAMA'.I THINK TRUE?")
# print(a)
# print(f"IS NAME == 'ANKIT'.I THINK FALSE?")
# print(b)
# print(f"IS NAME == 'ANUJ'.I THINK FALSE?")
# print(b)
# print(f"IS NAME == 'AKILESH'.I THINK FALSE?")
# print(b)
# print(f"IS NAME == 'ROHIT'.I THINK FALSE?")
# print(b)
# print(f"IS NAME == 'PANKAJ'.I THINK FALSE?")
# print(b)

# name = "anurag"
# a = 10
# b = 20
# friends = ["anurag","krsna","radha","balram"]
# print("I THINK NAME IS 'anurag'.IS IT TRUE?")
# print(name == "anurag")
# print("I THINK NAME IS 'radha'.IS IT FALSE?")
# print(name != "anurag")
# print("I THINK NAME IS 'ANURAG'.IS IT FALSE?")
# print(name == "ANURAG")
# print("I THINK NAME IS 'anurag'.IS IT TRUE?")
# print(name == "ANURAG".lower())
# print("I THINK 'anurag' AND 'krsna' ARE FRINDS.I THINK TRUE?")
# print('anurag' in friends and "krsna" in friends)
# print("I THINK 'anurag' AND 'rohit' ARE FRINDS.I THINK FALSE?")
# print('anurag' in friends and "rohit" in friends)
# print("a>b.I THINK FALSE")
# print(a>b)
# print("a<b.I THINK FALSE")
# print(a<b)

# age = 19
# if age>18:
#     print("YOU CAN GIVE VOTE.")

# age = 19
# if age>18:
#     print("YOU CAN GIVE VOTE.")
# else:
#     print("YOU CANNOT GIVE VOTE.")

# age = int(input("ENTER YOUR AGE : "))
# if age==4:
#     print("YOUR ENTRY IS FREE")
# elif age>4 and age<=18:
#     print("YOU NEED TO PAY $5" )
# else:
#     print("YOU NEED TO PAY $10")

# age = int(input("ENTER YOUR AGE : "))
# if age==4:
#     price = "$0"
# elif age>4 and age<=18:
#     price = "$5"
# else:
#     price = "$10"
# print(f"you need to pay {price}.")


# age = int(input("ENTER YOUR AGE : "))
# if age==4:
#     price = "$0"
# elif age>4 and age<=18:
#     price = "$5"
# elif age>65:
#     price = "$5"
# else: # FOR AGE BETWEEN 18 TO 65 YEARS
#     price = "$10"
# print(f"you need to pay {price}.")

# age = int(input("ENTER YOUR AGE : "))
# if age==4:
#     price = "$0"
# elif age>4 and age<=18:
#     price = "$5"
# elif age>18 and age<=65:
#     price = "$10"
# elif age>65:
#     price = "$5"
# print(f"you need to pay {price}.")

# requested_toppings = ['mushrooms', 'extra cheese']
# if "mushrooms" in requested_toppings:
#     print("MUSHROOMS ADDED !")
# if "pepperoni" in requested_toppings:
#     print("PEPPERONI ADDED !")
# if "extra cheese" in requested_toppings:
#     print("EXTRA CHEESE ADDED !")
# print("\nYOUR PIZZA IS READY.\n")

# requested_toppings = ['mushrooms', 'extra cheese']
# if "mushrooms" in requested_toppings:
#     print("MUSHROOMS ADDED !")
# elif "pepperoni" in requested_toppings:
#     print("PEPPERONI ADDED !")
# elif "extra cheese" in requested_toppings:
#     print("EXTRA CHEESE ADDED !")
# print("\nYOUR PIZZA IS READY.")

# alien_color = ["GREEN","YELLOW"]
# if "GREEN" in alien_color:
#     print("YOU EARNED 5 POINTS.")
# if "YELLOW" in alien_color:
#     print("YOU EARNED 10 POINTS.")
# if "RED" in alien_color:
#     print("WHAT?")

# alien_color = ["RED","YELLOW"]
# if "GREEN" in alien_color:
#     print("YOU EARNED 5 POINTS.")
# else:
#     print("YOU EARNED 10 POINTS.")


# alien_color = ["RED"]
# if "GREEN" in alien_color:
#     print("YOU EARNED 5 POINTS.")
# elif "YELLOW" in alien_color:
#     print("YOU EARNED 10 POINTS.")
# else:
#     print("YOU EARNED 15 POINTS.")

# alien_color = ["RED"]
# if "GREEN" in alien_color:
#     points = 5
# elif "YELLOW" in alien_color:
#     points = 10
# else:
#     points = 15
# print("YOU EARNED "+str(points)+" POINTS.")

# age = int(input("ENTER YOUR AGE : "))
# if age<=2:
#     print("YOU ARE BABY")
# elif age>2 and age<=4:
#     print("YOU ARE TODDLER")
# elif age>4 and age<=13:
#     print("YOU ARE KID")
# elif age>13 and age<=20:
#     print("YOU ARE TEENAGER")
# elif age>20 and age<=65:
#     print("YOU ARE ADULT")
# elif age>65:
#     print("YOU ARE ELDER")

# favourite_fruits = ["BANANA","APPLE","GUAVA","KIWI","MANGO"]
# if "BANANA" in favourite_fruits:
#     print("YOU REALLY LIKE BANANAS!")

# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for i in requested_toppings:
#     if i == "green peppers":
#         print("SORRY, 'GREEN PEPPER' IS OUT OF STOCK.")
#     else:
#         print(f"ADDED {i.upper()}!")
# print("\nYOUR PIZZA IS READY")

# requested_toppings = []
# if requested_toppings:
#     for i in requested_toppings:
#         if i == "green peppers":
#             print("SORRY, 'GREEN PEPPER' IS OUT OF STOCK.")
#         else:
#             print(f"ADDED {i.upper()}!")
#     print("\nYOUR PIZZA IS READY")
# else:
#     print("ARE YOU SURE YOU WANT PLAIN PIZZA?")

# available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
# for i in requested_toppings:
#     if i in available_toppings:
#         print(f"{requested_toppings.index(i)+1}. ADDING {i.upper()}")
#     else:
#         print(f"{requested_toppings.index(i)+1}. {i.upper()} IS NOT AVAILABLE")
# print("\nYOUR PIZZA IS READY")

# i = 1
# available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni', 'pineapple', 'extra cheese']
# while i<7:
#     for j in available_toppings:
#         print(f"{i}:{j}")
#         i = i+1

# while True:
#     admin_name = input("PLEASE MAKE ADMIN : ").strip()
#     if not admin_name:
#         print("WE DON'T WANT A EMPTY INPUT.TRY AGAIN!!")
#     if admin_name:
#         break
# user_names = []
# i = 1
# while True:
#     input_1 = input("ENTER YOUR USERNAME: ").strip()
#     if input_1 in user_names:
#         print("TRY ENTERING NEW USER NAME. TYPED USER NAME ALREADY EXIST")
#         continue
#     user_names.append(input_1)
#     if not input_1:
#         print("WE DON'T WANT A EMPTY INPUT.TRY AGAIN!!")
#     elif input_1 == admin_name:
#         print(f"HELLO {input_1}, WOULD TO LIKE TO SEE A STATUS REPORT.")
#     elif input_1 != admin_name:
#         print(f"HELLO {input_1}, THANKYOU FOR LOGGING IN AGAIN!")
#     if input_1 == "QUIT":
#         print("THANKS FOR COMING")
#         break
# user_names.pop()
# k=1
# while k<len(user_names):
#     for names in user_names:
#         print(f"{k}. LIST OF USERS LOGGED IN :{names}")
#         k = k+1

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # CHAPTER_6 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# aliens = {'power level':5,"points":10}
# print(aliens["power level"])
# print(aliens["points"])

# aliens = {'color':'green','points':5}
# user_points = aliens['points']
# print("YOU HAVE JUST EARNED "+str(user_points)+ " POINTS.")

# aliens = {'color':'green','points':5}
# aliens['X-POSITION']=0
# aliens['Y-POSITION']=25
# print(aliens)

# aliens = {}
# aliens['color']='green'
# aliens['points']=20
# # print(aliens)
# # print(f"THE COLOR OF THE ALIEN IS {aliens['color'].upper()}.")
# # aliens['color'] = 'pink'
# # print(f"THE COLOR OF THE ALIEN IS {aliens['color'].upper()}.")
# aliens['x-position']=0
# aliens['y-position']=25
# # aliens['speed']='slow'
# # aliens['speed']='medium'
# aliens['speed']='fast'
# print(aliens)
# print(f"INITIAL POSITION OF THE ALIEN IS: {str(aliens['x-position'])}")
# if aliens['speed']=="slow":
#     x_increment = 1
# elif aliens['speed']=="medium":
#     x_increment = 2
# else:
#     x_increment = 3
# aliens['x-position']=aliens['x-position']+x_increment
# print(f"NEW POSITION OF THE ALIEN IS: {str(aliens['x-position'])}")

# aliens = {'color':'green','points':5}
# del aliens['color']
# print(aliens)

# user_info = {
#             'first_name':'anurag',
#             'last_name':'pareek',
#             'age':'20',
#             'city':'guwahati',
#             }
# for KEYS,VALUES in user_info.items():
# #     print(f"{KEYS}:{VALUES}")
# # print(user_info)
#     print(f"\nKEYS IS : {KEYS.upper().center(50)}")
#     print(f"VALUE FO KEY IS : {VALUES.upper().center(30)}")

# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }
# print(f"NAME OF THE PERSON PARTICPIPATED IN THE POLLS :")
# for i in sorted(favorite_languages.keys()):  # ALSO: for i in favourite_languages:
#     print(f"{i}")
# print(f"LIST OF THEIR PAVOURITE LANGUAGES CHOOSEN BY THE POLLS (RESPECTIVELY) IS:")
# for j in sorted(favorite_languages):
#     print(favorite_languages[j])

# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }
# for i in favorite_languages.values():
#     print(f"FAVORITE LANGUAGE CHOOSEN IS : {i}")


# favorite_languages = {
# 'jen': 'python',
# 'sarah': 'c',
# 'edward': 'ruby',
# 'phil': 'python',
# }
# print("LANGUAGE CHOSEN ARE : ")
# for j in set(favorite_languages.values()):
#     print(j)

# aliens = []
# new_alien = {'color':'green','points':20,'speed':'slow'}
# for alien_number in range(0,30):
#     aliens.append(new_alien)
# for alien in aliens[0:3]:
#     if alien['color']=="green":
#         alien['color']="blue"
#         alien['points']=30
#         alien['speed']='medium'
# for alien in aliens[0:5]:
#     print(alien)

# print()

# aliens = []
# for alien_number in range(0,30):
#     new_alien = {'color':'green','points':20,'speed':'slow'}
#     aliens.append(new_alien)
# for alien in aliens[0:3]:
#     if alien['color']=="green":
#         alien['color']="blue"
#         alien['points']=30
#         alien['speed']='medium'
# for alien in aliens[0:5]:
#     print(alien)

# pizza = {'crust':'thick',
#         'toppings':['mushroom','extra cheese'],
#         }
# print(f"YOUR PIZZA IS READY WITH CRUST:{pizza['crust']} INCLUDING THE FOLLOWING TOPPINGS:{pizza['toppings'][0].upper()}")
# print(f"YOUR PIZZA IS READY WITH CRUST:{pizza['crust']} INCLUDING THE FOLLOWING TOPPINGS:{pizza['toppings'][1].upper()}")
# print(f"YOUR PIZZA IS READY WITH CRUST:{pizza['crust']} INCLUDING THE FOLLOWING TOPPINGS:{pizza['toppings']}")

# pizza = {'crust':'thick',
#         'toppings':['mushroom','extra cheese'],
#         }
# print(f"YOUR PIZZA IS READY HAVING '{pizza['crust'].upper()}' CRUST, INCLUDING THE FOLLOWING TOPPING:")
# for i in pizza['toppings']:
#     print(f"{pizza['toppings'].index(i)+1}.{i.upper()}")

# favorite_languages = {
# 'jen': ['python', 'ruby'],
# 'sarah': ['c'],
# 'edward': ['ruby', 'go'],
# 'phil': ['python', 'haskell'],
# }
# for name,fav_lang in favorite_languages.items():
#     print(f'\n{name.upper()}\'s FAVOURITE LANGUAGES ARE/IS:')
#     for i in fav_lang:
#         print(f"{fav_lang.index(i)+1}.{i.upper()}")

# users = {
#         'aeinstein': {
#         'first': 'albert',
#         'last': 'einstein',
#         'location': 'princeton',
#         },
#         'mcurie': {
#         'first': 'marie',
#         'last': 'curie',
#         'location': 'paris',
#         },
#         }
# for i,j in users.items():
#     print(f"INFO ABOUT {i}:")
#     for k,l in j.items():
#         print(f"{k}:{l}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # CHAPTER_7 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# cars = ['audi','mercides','bmw']
# choose_car = input("WHICH CAR YOU WANT TO BUY-\n(audi,mercides,bmw)\n: ").lower()
# if choose_car in cars:
#     print("YES, CAR IS AVAILABLE!")
# else:
#     print("SORRY SIR, CAR IS NOT AVAILABLE YET!")

# # CHECK FOR MULTIPLICITY TEST OF 10:
# while True: 
#     input_num = input("ENTER A NUMBER (TO QUIT PRESS 0) : ")
#     input_num_1 = int(input_num)
#     if input_num_1 == 0:
#         break
#     if input_num_1%10==0:  # WE KNOW 0 IS MULTIPLE OF EVERY NUMBER
#         print(f"{input_num_1} IS MULTIPLE OF 10")
#     else:
#         print(f"{input_num_1} IS NOT MULTIPLE OF 10")
# # ALSO:
# input_num_1 = " "
# while input_num_1 != 0: 
#     input_num = input("ENTER A NUMBER (TO QUIT PRESS 0) : ")
#     input_num_1 = int(input_num)
#     if input_num_1%10==0:  # WE KNOW 0 IS MULTIPLE OF EVERY NUMBER
#         print(f"{input_num_1} IS MULTIPLE OF 10")
#     else:
#         print(f"{input_num_1} IS NOT MULTIPLE OF 10")

# flag = True
# while flag:
#     input_1 = input("ENTER ANYTHING :").upper()
#     if input_1 == "QUIT":
#         flag = False
#     else:
#         print(input_1)

# current_num = 0
# list_odd_num = []
# input_1 =int(input("ENTER THE NUMBER UPTO WHICH YOU WANT ODD NUMBERS :"))
# while current_num<input_1:
#     current_num+=1
#     if current_num % 2 == 0:
#         continue
#     list_odd_num.append(current_num)
# print(list_odd_num)

# spam = True
# while spam:
#     input_age = int(input("ENTER YOUR AGE : "))
#     if input_age<=3 and input_age>0:
#         print("TICKET FARE IS FREE")
#     if input_age>3 and input_age<10:
#         print("TICKET FARE IS $5")
#     if input_age>=10:
#         print("TICKET FARE IS $10")
#     if input_age == 0:
#         spam=False

# unconfirmed_users = ['anurag','radha','krsna','lalit']
# confirmed_users = []
# while unconfirmed_users:
#     confirm_user = unconfirmed_users.pop()
#     print(f"VERIFYING UNCONFIRMED USER : {confirm_user.upper()}\n")
#     confirmed_users.append(confirm_user)
# print("THIS USERS HAVE BEEN VERIFIED AS CONFIRM USERS : \n")
# for i in confirmed_users:
#     print(i.upper( ))

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:
#     pets.remove('cat')
# print(pets)

# response = {}
# polling_status = True
# while polling_status:
#     names = input("ENTER YOUR NAME : ").upper()
#     mountains = input("ENTER THE NAME OF THE MOUNTAIN YOU WANT TO CLIMB : ").upper()
#     response[names]=mountains
#     yes_no = input("WHAT YOU WANT TO DO. START AGAIN OR QUIT PRESS (Y) OR (PRESS ANY KEY) RESPECTIVELY : ").upper()
#     if yes_no == "N":
#         polling_status = False
#     if yes_no == "Y":
#         continue
# # print(response)
# print("--------RESULT--------")
# for i,j in response.items():
#     print(f"{i} WANT TO CLIMB {j}.")

# spam = 41
# print(id(spam))
# cheese = spam
# print(id(cheese))
# spam = 100
# print(spam)
# print(cheese)

# spam = [0,1,2,3,4,5]
# print(id(spam))
# cheese = spam
# print(id(cheese))
# spam[1]="HELLO"
# print(spam)
# print(cheese)

# print('A'>'B')
# print('B'>'A')
# print(ord('A'))
# print(ord('B'))

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # CHAPTER_8 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

# def hello_user():
#     """GRETTING USER"""
#     print("HELLO, USER")
# print(hello_user.__doc__)
# hello_user()

# def hello_user(username):
#     """GREETING USER"""
#     print("HELLO, "+username.upper())
# hello_user('anurag')

# def chapter_explain():
#     '''WHAT CHAPTER EXPLAIN US-'''
#     print("THIS CHAPTER TELL US ALL ABOUT FUNCTIONS")
# print(chapter_explain.__doc__)
# chapter_explain()

# def favourite_book(bookname):
#     print("I LIKE THE BOOK "+bookname.upper())
# favourite_book('alice in wonder land')

# def favourite_animal(wild_animal,pet_animal):
#     print("MY FAVOURITE WILD ANIMAL IS "+wild_animal.upper())
#     print("MY FAVOURITE PET ANIMAL IS "+pet_animal.upper())
# favourite_animal('lion','cow')

# def favourite_animal(wild_animal,pet_animal):
#     print("MY FAVOURITE WILD ANIMAL IS "+wild_animal.upper())
#     print("MY FAVOURITE PET ANIMAL IS "+pet_animal.upper())
# favourite_animal(wild_animal='lion',pet_animal='cow')

# def favourite_animal(wild_animal,pet_animal="dog"):
#     print("MY FAVOURITE WILD ANIMAL IS "+wild_animal.upper())
#     print("MY FAVOURITE PET ANIMAL IS "+pet_animal.upper())
# favourite_animal('lion')

# def favourite_animal(wild_animal="lion",pet_animal="dog"):
#     print("MY FAVOURITE WILD ANIMAL IS "+wild_animal.upper())
#     print("MY FAVOURITE PET ANIMAL IS "+pet_animal.upper())
# favourite_animal()

# def favourite_animal(wild_animal="lion",pet_animal="dog"):
#     print("MY FAVOURITE WILD ANIMAL IS "+wild_animal.upper())
#     print("MY FAVOURITE PET ANIMAL IS "+pet_animal.upper())
# favourite_animal("bull",'cat')

# def favourite_animal(wild_animal="lion",pet_animal):
#     print("MY FAVOURITE WILD ANIMAL IS "+wild_animal.upper()) # WILL GET ERROR
#     print("MY FAVOURITE PET ANIMAL IS "+pet_animal.upper())
# favourite_animal('tiger')

# def make_tshirt(tshirt_size,print_name):
#     print(f"PRINT TEXT '{print_name}' IN T-SHIRT WITH THE SIZE '{tshirt_size}'.")
# make_tshirt(42,'ANURAG')

# def make_tshirt(tshirt_size,print_name):
#     print(f"PRINT TEXT '{print_name}' IN T-SHIRT WITH THE SIZE '{tshirt_size}'.")
# make_tshirt(print_name='ANURAG',tshirt_size=50)

# def make_tshirt(tshirt_size = "LARGE SIZE",print_name = "I LOVE PYTHON"):
#     print(f"PRINT TEXT '{print_name}' IN T-SHIRT WITH THE SIZE '{tshirt_size}'.")
# make_tshirt(print_name="ANURAG",tshirt_size='SMALL SIZE')
# make_tshirt(tshirt_size='MEDIUM SIZE')
# make_tshirt(tshirt_size='LARGE SIZE')

# def make_tshirt(tshirt_size = "LARGE SIZE",print_name = "I LOVE PYTHON"):
#     print(f"PRINT TEXT '{print_name}' IN T-SHIRT WITH THE SIZE '{tshirt_size}'.")
# make_tshirt()

# def city_in_country(city,country):
#     print(f"{city.upper()} IS IN {country.upper()}.")
# city_in_country('GUWAHATI',"INDIA")

# def city_in_country(city,country = "INDIA"):
#     print(f"{city.upper()} IS IN {country.upper()}.")
# city_in_country('GUWAHATI')
# city_in_country('TOKYO')  # WELL ITS NOT IN INDIA
# city_in_country('UTTAR-PRADESH')

# def user_fullname(first_name,last_name):
#     # full_name = first_name.title() + " " + last_name.title()
#     full_name = first_name + " " + last_name
#     return full_name.title()
# # print(user_fullname("anurag","pareek"))
# full_user_name = user_fullname("anurag","pareek")
# print(full_user_name)

# def user_fullname(first_name,last_name,middle_name = ""):
#     if middle_name:
#         full_name = first_name + " " + middle_name + " " + last_name
#     else:
#         full_name = first_name + " " + last_name
#     full_name = full_name.title()
#     return(full_name)
# print(user_fullname("shree",'krsna',"yasodanandan"))
# print(user_fullname('anurag',"pareek"))

# def name_in_dict(first_name,last_name):
#     dict_info = {'first':first_name.title(),"last":last_name.title()}
#     return dict_info
# print(name_in_dict('anurag',"pareek"))

# def name_in_dict(first_name,last_name,age = ""):
#     dict_info = {'first name':first_name.title(),"last name":last_name.title()}
#     if age:
#         dict_info['age'] = age
#     return dict_info
# print(name_in_dict('anurag',"pareek"))
# print(name_in_dict('anurag',"pareek",20))

# def full_name(first_name,last_name,middle_name = ""):
#     if middle_name:
#         full__user_name = first_name + " " + middle_name + " " + last_name
#     else:
#         full__user_name = first_name + " " + last_name
#     return full__user_name.title()
# while True:
#     f_name = input("ENTER YOUR FIRST NAME(TO QUIT TYPE : QUIT) : ").upper()
#     if f_name == "QUIT":
#         break
#     else:
#         l_name = input("ENTER YOUR LAST NAME : ").upper()
#         m_name = input("ENTER YOUR MIDDLE NAME(OPTIONAL(ELSE LEFT EMPTY)) : ").upper()
#         full_name_format =full_name(f_name,l_name,m_name)
#         print(f"HELLO, {full_name_format}!! \n")
# print("THANKS FOR TRYING !! HOPE YOU COME AGAIN")

# user_names = ['anurag','krsna','radha','ganesh']
# def greet_users(list_of_names):
#     for i in list_of_names:
#         greetings = f"HELLO, {i.upper()}. NICE TO MEET YOU!"
#         print(greetings)
# greet_users(user_names)

# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# print("LIST OF UNPRINTED DESIGNS:")
# for i in unprinted_designs:
#     print(f"{unprinted_designs.index(i)+1}) {i}")
# print()
# while unprinted_designs:
#     current_designs = unprinted_designs.pop()
#     print("DESIGNS UNDER PROCESS : "+current_designs)
#     completed_models.append(current_designs)
# print()
# print("THE FOLLOWING MODELS HAVE BEEN PRINTED : ")
# for i in completed_models:
#     print(f"{completed_models.index(i)+1}) {i}")
# # ALSO:
# def print_models(uncompleted_designs,completed_designs):
#     """
#     Simulate printing each design, until none are left.
#     Move each design to completed_models after printing.
#     """
#     while uncompleted_designs:
#         processing_designs = uncompleted_designs.pop()
#         print(f"{processing_designs.upper()} IS UNDER PROCESS.\n")
#         completed_designs.append(processing_designs)
# def show_completed_designs(completed_designs):
#     print("THE FOLLOWING DESIGNS HAVE BEEN COMPLETED :")
#     for completed_design in completed_designs:
#         print(f"{completed_designs.index(completed_design)+1}) {completed_design}\n")
# un_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# c_designs = []
# print_models(un_designs,c_designs)
# show_completed_designs(c_designs)

# def make_pizza(*args):
#     print(args)
# make_pizza('extra cheese','pepperoni','mushrooms')
# make_pizza('extra cheese')

# def make_pizza(*args):
#     print("THE LIST OF THE TOPPINGS CHOOSEN BY YOU : ")
#     for i in args:
#         print(f"- {i}")
# make_pizza('extra cheese','pepperoni','mushrooms')
# make_pizza('extra cheese')

# def make_pizza(size,*args):
#     print(f"MAKE A PIZZA OF {size} INCH AND ADD THE FOLLOWING TOPPINGS INTO PIZZA : ")
#     for i in args:
#         print(f"- {i.upper()}")
# make_pizza(20,"extra cheese",'mushroom','pepperoni')

# def user_info(first_name,last_name,**kwargs):
#     profile = {}
#     profile["first_name"] = first_name
#     profile["last_name"] = last_name
#     for i,j in kwargs.items():
#         profile[i]=j
#     print(profile)
# user_info('anurag','pareek',age=20,state='assam')

# def user_info(**kwargs):
#     print(kwargs)
# user_info(name='anurag',surname='pareek')

# def make_car(first_car,second_car,**kwargs):
#     car_data = {}
#     car_data['car_name1']= first_car
#     car_data['car_name2']= second_car
#     for i, j in kwargs.items():
#         car_data[i]=j
#     return car_data
# print(make_car("audi","bulero",color='blue',tow_package = 'True'))
# # ALSO:
# def make_car(*args,**kwargs):
#     car_data = {}
#     if list(args):
#         car_data['car_name']= args[0]
#         car_data['car_name_1']= args[1]
#     for i, j in kwargs.items():
#         car_data[i]=j
#     return car_data
# print(make_car("audi","bulero",color='blue',tow_package = 'True'))

# import pizza
# pizza.make_pizza(12,'mushroom')
# pizza.make_pizza(12,'mushroom','pepperoni','extra cheese')

# from pizza import make_pizza
# make_pizza(12,'mushroom','pepperoni',"extra cheese")

# from models import print_models
# un_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# c_designs = []
# print_models(un_designs,c_designs)
# from models import show_completed_designs
# show_completed_designs(c_designs)

# from models import print_models as mp
# un_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# c_designs = []
# mp(un_designs,c_designs)
# from models import show_completed_designs as scd
# scd(c_designs)

# import pizza as p
# p.make_pizza(12,'mushroom','pepperoni',"extra cheese")






























