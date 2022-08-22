# -------------------------------- CHAPTER - 9 --------------------------------





# CREATING A DOG CLASS WHICH TELL PYTHON TO MAKE AN OBJECT REPRESENTING A DOG:

# class Dog():
#     '''A SIMPLE ATTEMPT TO MODEL A DOG.'''  # DOCTRING TELL WHAT CLASS DOES

#     def __init__(self,name,age):
#         '''INITIALIZE NAME AND AGE ATTRIBUTES''' # DOCSTRING
#         self.name = name
#         self.age = age

#     def sit(self):
#         '''SIMULATE A DOG TO SIT ON COMMAND'''  # DOCSTRING
#         print(self.name.title()+" is now sitting.")

#     def roll_over(self):
#         '''SIMULATE A DOG TO ROLL OVER ON COMMAND''' # DOCSTRING
#         print(self.name.title()+ " is rolled over!")

# my_dog = Dog('willie',6)  # CALLING CLASS 
# your_dog = Dog('tummy',4) # CALLING CLASS
# print("My dog's name is "+my_dog.name.title()+".")
# print("My dog is "+str(my_dog.age)+" years old.")
# print("My dog's name is "+your_dog.name.title()+".")
# print("My dog is "+str(your_dog.age)+" years old.")
# my_dog.sit()  # CALLING METHODS
# my_dog.roll_over()  # CALLING METHODS
# your_dog.sit()    # CALLING METHODS
# your_dog.roll_over()   # CALLING METHODS





# CREATING AN RESTAURANT CLASS WHICH TELLS PYTHON TO MAKE OBJECT REPRESENTING -
# - AN RESTAURANT

# class Restaurant():  # CLASS
#     '''SIMPLE ATTEMPT TO IMFORM ABOUT RESTAURANT''' # DOCSTRING

#     def __init__(self,restaurant_name,cuisine_type):  # DEFINING ATTRIBUTES
#         '''INITIALIZE RESTAURANT NAME AND CUISINE TYPE'''
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type

#     def describe_restaurant(self):  # DEFINING INSTATNCE METHODS
#         '''DESCRIBING ABOUT RESTAURANT'''
#         print(f"This restaurant named {self.restaurant_name.title()} is \
# famous for 'RasMalai'.\n")

#     def open_restaurant(self): # DEFININF INSTANCE METHODS
#         '''OPENING TIMING OF THE RESTAURANT'''
#         print(f"""THE OPENING AND CLOSING TIME OF THE RESTAURANT ARE FOLLOWS :
# OPEN : 9 AM TO 10 PM
# CLOSE : 10 PM TO 9 AM\n""")

# restaurant = Restaurant("gopal Maharaj","korean cuisine")
# print(f"""Our restaurant name is {restaurant.restaurant_name.title()} and we
# provide our guests the {restaurant.cuisine_type.title()}.\n""")
# restaurant.describe_restaurant() # CALLING METHODS
# restaurant.open_restaurant()   # CALLING METHODS





# class Users():

#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age

#     def describe_user(self):
#         print(f'''Full Name of the user is 
# {self.first_name.title() +" "+ self.last_name.title()} and the Age of the
# user is {self.age}.\n''')

#     def greet_user(self):
#         print(f"Nice to meet you {self.first_name.title()}. How's going!\n")

# user_info = Users('Radha','Krsna',20)
# user_info.describe_user()
# user_info.greet_user()
# print(f"{user_info.first_name.title()} is currently studing in GLA CS branch \
# .\n")




# class Car():
#     '''A simple attempt to represent a car.'''

#     def __init__(self,make,model,year):
#         """Initialize attributes to describe a car."""
#         self.make1 = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0   # WE CAN SET DEFAULT VALUES LIKE THIS EVEN
#                                     # - IF WE DON't HAVE ITS ATTRIBUTE
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + " " + self.make1 + " " + self.model
#         return long_name.title()

#     def read_odometer(self):
#         """Print's statement showing the car's mileage."""
#         print(f"The car has {str(self.odometer_reading)} miles on it.")

# my_new_car = Car("audi",'a4',2016)
# print(f"My car name is "+ "'" + my_new_car.get_descriptive_name() + "'.")
# # my_new_car.read_odometer()
# my_new_car.odometer_reading = 60
# my_new_car.read_odometer()





# class Car():
#     '''A simple attempt to represent a car.'''

#     def __init__(self,make,model,year):
#         """Initialize attributes to describe a car."""
#         self.make1 = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0   # WE CAN SET DEFAULT VALUES LIKE THIS EVEN-
#                                     # - IF WE DON't HAVE ITS ATTRIBUTE
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + " " + self.make1 + " " + self.model
#         return long_name.title()

#     def update_odometer(self,mileage):
#         """Set the odometer reading to the given value.
#         Set the odometer reading to a given value and,
#         restrict the change if someone tries to roll back the 
#         odometer reading."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
        
#     def read_odometer(self):
#         """Print's statement showing the car's mileage."""
#         print(f"The car has {str(self.odometer_reading)} miles on it.")
    
# my_new_car = Car("audi",'a4',2016)
# print(f"My car name is "+ "'" + my_new_car.get_descriptive_name() + "'.")
# # # my_new_car.read_odometer()
# # # my_new_car.odometer_reading = 60
# # # my_new_car.read_odometer()
# my_new_car.update_odometer(44)  # DEFINING CURRENT ODOMETER REAL READING.
# my_new_car.update_odometer(22)  # TRYING TO ROLL BACK i.e UPDATING THE -
#                                 # - ODOMETER READING LESS THAN CURRENT VALUE.
# # my_new_car.update_odometer(55)# AS CURRENT READING IS 44 HENCE 55 WILL BE-
#                                 # RIGHT.
# my_new_car.read_odometer()





# class Car():
#     '''A simple attempt to represent a car.'''

#     def __init__(self,make,model,year):
#         """Initialize attributes to describe a car."""
#         self.make1 = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0   # WE CAN SET DEFAULT VALUES LIKE THIS EVEN-
#                                     # - IF WE DON't HAVE ITS ATTRIBUTE
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + " " + self.make1 + " " + self.model
#         return long_name.title()

#     def update_odometer(self,mileage):
#         """Set the odometer reading to the given value.
#         Set the odometer reading to a given value and,
#         restrict the change if someone tries to roll back the 
#         odometer reading."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         if mileage < 0:
#             print('Could you tell me how you drove your car in (-)ve values!!')
#         else:
#             print("You can't roll back an odometer!")
        
#     def read_odometer(self):
#         """Print's statement showing the car's mileage."""
#         print(f"The car has {str(self.odometer_reading)} miles on it.")

#     def increment_odometer(self,miles):
#         self.odometer_reading += miles

# my_new_car = Car("audi",'a4',2016)
# print(f"My car name is "+ "'" + my_new_car.get_descriptive_name() + "' its my \
# new car.")
# my_new_car.read_odometer()         # READ THE DEFAULT ODOMETER READING i.e 0
# my_new_car.odometer_reading = 56   # CHANGING THE ODOMETER DEFAULT READING TO 56
# my_new_car.read_odometer()         # READING THE NEW ODOMETER VALUE

# print()

# my_used_car = Car("mercides",'B1600',2022)
# print(f"""Currently I am using the '{my_used_car.get_descriptive_name()}' 
#     model car.""")
# my_used_car.update_odometer(23500)  # UPDATING ODO. READING USING METHODS
# my_used_car.read_odometer()         # READING THE NEW ODOMETER VALUE
# my_used_car.increment_odometer(100) # INCREMENTING THE INITIAL VALUE BY PRESENT-
#                                    # - VALUE
# my_used_car.read_odometer()         # READING THE NEW ODOMETER VALUE





# """CREATING AN RESTAURANT CLASS WHICH TELLS PYTHON TO MAKE OBJECT REPRESENTING
# AN RESTAURANT
# """
# class Restaurant():  # CLASS
#     '''SIMPLE ATTEMPT TO IMFORM ABOUT RESTAURANT''' # DOCSTRING

#     def __init__(self,restaurant_name,cuisine_type):  # DEFINING ATTRIBUTES
#         '''INITIALIZE RESTAURANT NAME AND CUISINE TYPE'''
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):  # DEFINING INSTATNCE METHODS
#         '''DESCRIBING ABOUT RESTAURANT'''
#         print(f"This restaurant named {self.restaurant_name.title()} is \
# famous for 'RasMalai'.")

#     def open_restaurant(self): # DEFININF INSTANCE METHODS
#         '''OPENING TIMING OF THE RESTAURANT'''
#         print(f"""THE OPENING AND CLOSING TIME OF THE RESTAURANT ARE FOLLOWS :
# OPEN  : 9 AM TO 10 PM
# CLOSE : 10 PM TO 9 AM""")

#     def get_number_served(self):
#         """Processing the number of customers served."""
#         print(f"Total {str(self.number_served)} numbers of customers have been \
# served.")
    
#     def update_number_served(self,latest_people_served):
#         '''Updating number of peoples served.'''
#         self.number_served = latest_people_served

#     def increment_number_served(self,current_number_served):
#         '''Total number of peoples served.'''
#         self.number_served += current_number_served

# restaurant = Restaurant("gopal Maharaj","korean cuisine")
# print("--------------------------------------------------------------------")
# print(f"Our restaurant name is '{restaurant.restaurant_name.title()}' and we \
# provide our guests the '{restaurant.cuisine_type.title()}'.")

# restaurant.describe_restaurant()
# print("--------------------------------------------------------------------")
# restaurant.open_restaurant()   
# print("--------------------------------------------------------------------")
# restaurant.number_served
# restaurant.get_number_served()
# restaurant.update_number_served(4)
# restaurant.get_number_served()
# restaurant.increment_number_served(3)
# restaurant.get_number_served()




# class Users():

#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = 1

#     def describe_user(self):
#         print(f"Full Name of the user is \
# '{self.first_name.title()} {self.last_name.title()}' and the Age of the \
# user is '{self.age}'.\n")

#     def greet_user(self):
#         print(f"Nice to meet you {self.first_name.title()}. How's going!\n")

#     def read_attempts(self):
#         print(f"ATTEPT {self.login_attempts} OF USER:")

#     def increment_login_attempts(self):
#         '''Increments the number of logins as instance calls the method'''
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         '''Reset the number of login attempts to 0.'''
#         self.login_attempts = 0

# user_info = Users('Radha','Krsna',20)
# user_info.reset_login_attempts()
# user_info.read_attempts()
# print("---------------------------------------------------------------------")
# user_info.describe_user()
# user_info.greet_user()
# print(f"{user_info.first_name.title()} is currently studing in GLA CS branch \
# .\n")
# print("---------------------------------------------------------------------")

# user_info_1 = Users('krsna','gopal',20)
# user_info_1.increment_login_attempts()
# user_info_1.read_attempts()
# print("---------------------------------------------------------------------")
# user_info_1.describe_user()
# user_info_1.greet_user()
# print(f"{user_info_1.first_name.title()} is currently studing in GLA CS branch \
# .\n")





# class Car():
#     '''A simple attempt to represent a car.'''

#     def __init__(self,make,model,year):
#         """Initialize attributes to describe a car."""
#         self.make1 = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0   # WE CAN SET DEFAULT VALUES LIKE THIS EVEN-
#                                     # - IF WE DON't HAVE ITS ATTRIBUTE
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + " " + self.make1 + " " + self.model
#         return long_name.title()

#     def update_odometer(self,mileage):
#         """Set the odometer reading to the given value.
#         Set the odometer reading to a given value and,
#         restrict the change if someone tries to roll back the 
#         odometer reading."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         if mileage < 0:
#             print('Could you tell me how you drove your car in (-)ve values!!')
#         elif mileage < self.odometer_reading:
#             print("You can't roll back an odometer!")
        
#     def read_odometer(self):
#         """Print's statement showing the car's mileage."""
#         print(f"The car has {str(self.odometer_reading)} miles on it.")

#     def increment_odometer(self,miles):
#         self.odometer_reading += miles

#     def fill_gas_tank(self):
#         '''This vehicle contains a gas tank.'''
#         print("Your GasTank have been filled up.")

# my_new_car = Car("audi",'a4',2016)
# print(f"My car name is "+ "'" + my_new_car.get_descriptive_name() + "' its my \
# new car.")
# my_new_car.read_odometer()         # READ THE DEFAULT ODOMETER READING i.e 0
# my_new_car.odometer_reading = 56   # CHANGING THE ODOMETER DEFAULT READING TO 56
# my_new_car.read_odometer()         # READING THE NEW ODOMETER VALUE
# my_new_car.fill_gas_tank()

# print("-----------------------------------------------------------------------")

# my_used_car = Car("mercides",'B1600',2022)
# print(f"Currently I am using the '{my_used_car.get_descriptive_name()}' \
# model car.")
# my_used_car.update_odometer(23500)  # UPDATING ODO. READING USING METHODS
# my_used_car.read_odometer()         # READING THE NEW ODOMETER VALUE
# my_used_car.increment_odometer(100) # INCREMENTING THE INITIAL VALUE BY PRESENT-
#                                    # - VALUE
# my_used_car.read_odometer()         # READING THE NEW ODOMETER VALUE
# my_used_car.fill_gas_tank()

# print("-----------------------------------------------------------------------")

# class Electric_car(Car):
#     '''Represent aspects of a car, specific to electric vehicles.
#     and Initialize attribute of the child class.'''

#     def __init__(self,make,model,year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make,model,year)
#         self.battery_size = 70

#     def describe_battery(self):
#         '''Print a statement describing the battery size.'''
#         print(f"The battery of this car have a battery of {self.battery_size} KwH.")

#     def fill_gas_tank(self):
#         '''A electric vehicle not contains a gas tank.'''
#         print("This vehicle not having the GasTank!!")

# my_tesla = Electric_car('tesla','model s',2016)
# print(f"I just bought my new tesla car named '{my_tesla.get_descriptive_name()}'")
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()






# class Car():
#     '''A simple attempt to represent a car.'''

#     def __init__(self,make,model,year):
#         """Initialize attributes to describe a car."""
#         self.make1 = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0   # WE CAN SET DEFAULT VALUES LIKE THIS EVEN-
#                                     # - IF WE DON't HAVE ITS ATTRIBUTE
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + " " + self.make1 + " " + self.model
#         return long_name.title()

#     def update_odometer(self,mileage):
#         """Set the odometer reading to the given value.
#         Set the odometer reading to a given value and,
#         restrict the change if someone tries to roll back the 
#         odometer reading."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         if mileage < 0:
#             print('Could you tell me how you drove your car in (-)ve values!!')
#         elif mileage < self.odometer_reading:
#             print("You can't roll back an odometer!")
        
#     def read_odometer(self):
#         """Print's statement showing the car's mileage."""
#         print(f"The car has {str(self.odometer_reading)} miles on it.")

#     def increment_odometer(self,miles):
#         self.odometer_reading += miles

#     def fill_gas_tank(self):
#         '''This vehicle contains a gas tank.'''
#         print("Your GasTank have been filled up.")

# print("-----------------------------------------------------------------------")

# my_new_car = Car("audi",'a4',2016)
# print(f"My car name is "+ "'" + my_new_car.get_descriptive_name() + "' its my \
# new car.")
# my_new_car.read_odometer()         # READ THE DEFAULT ODOMETER READING i.e 0
# my_new_car.odometer_reading = 56   # CHANGING THE ODOMETER DEFAULT READING TO 56
# my_new_car.read_odometer()         # READING THE NEW ODOMETER VALUE
# my_new_car.fill_gas_tank()

# print("-----------------------------------------------------------------------")

# my_used_car = Car("mercides",'B1600',2022)
# print(f"Currently I am using the '{my_used_car.get_descriptive_name()}' \
# model car.")
# my_used_car.update_odometer(23500)  # UPDATING ODO. READING USING METHODS
# my_used_car.read_odometer()         # READING THE NEW ODOMETER VALUE
# my_used_car.increment_odometer(100) # INCREMENTING THE INITIAL VALUE BY PRESENT-
#                                     # - VALUE
# my_used_car.read_odometer()         # READING THE NEW ODOMETER VALUE
# my_used_car.fill_gas_tank()

# print("-----------------------------------------------------------------------")

# class Battery():
#     """Modeling a Battery for the Electric_car."""

#     def __init__(self,battery_size = 70):
#         '''Initializing the battery attributes.'''
#         self.battery_size = battery_size

#     def describe_battery(self):
#         '''Print a statement describing the battery size.'''
#         print(f"The battery of car have a battery of {self.battery_size} KwH.")

#     def get_range(self):
#         """Print a statement about the range the battery provides."""
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         print(f"This car can go approximatelt {str(range)} miles on full \
# charge.")

# class Electric_car(Car):
#     '''Represent aspects of a car, specific to electric vehicles.
#     and Initialize attribute of the child class.'''

#     def __init__(self,make,model,year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make,model,year)
#         self.battery = Battery()

#     def fill_gas_tank(self):
#         '''A electric vehicle not contains a gas tank.'''
#         print("This vehicle not having the GasTank!!")

# my_tesla = Electric_car('tesla','model s',2016)
# print(f"I just bought new tesla car named '{my_tesla.get_descriptive_name()}'.")
# my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
# my_tesla.battery.get_range()





# """CREATING AN RESTAURANT CLASS WHICH TELLS PYTHON TO MAKE OBJECT REPRESENTING
# AN RESTAURANT
# """
# class Restaurant():  # CLASS
#     '''SIMPLE ATTEMPT TO IMFORM ABOUT RESTAURANT''' # DOCSTRING

#     def __init__(self,restaurant_name,cuisine_type):  # DEFINING ATTRIBUTES
#         '''INITIALIZE RESTAURANT NAME AND CUISINE TYPE'''
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):  # DEFINING INSTATNCE METHODS
#         '''DESCRIBING ABOUT RESTAURANT'''
#         print(f"This restaurant named {self.restaurant_name.title()} is \
# famous for 'RasMalai'.")

#     def open_restaurant(self): # DEFININF INSTANCE METHODS
#         '''OPENING TIMING OF THE RESTAURANT'''
#         print(f"""THE OPENING AND CLOSING TIME OF THE RESTAURANT ARE FOLLOWS :
# OPEN  : 9 AM TO 10 PM
# CLOSE : 10 PM TO 9 AM""")

#     def get_number_served(self):
#         """Processing the number of customers served."""
#         print(f"Total {str(self.number_served)} numbers of customers have been \
# served.")
    
#     def update_number_served(self,latest_people_served):
#         '''Updating number of peoples served.'''
#         self.number_served = latest_people_served

#     def increment_number_served(self,current_number_served):
#         '''Total number of peoples served.'''
#         self.number_served += current_number_served

# restaurant = Restaurant("gopal Maharaj","korean cuisine")
# print("--------------------------------------------------------------------")
# print(f"Our restaurant name is '{restaurant.restaurant_name.title()}' and we \
# provide our guests the '{restaurant.cuisine_type.title()}'.")

# restaurant.describe_restaurant()
# print("--------------------------------------------------------------------")
# restaurant.open_restaurant()   
# print("--------------------------------------------------------------------")
# restaurant.number_served
# restaurant.get_number_served()
# restaurant.update_number_served(4)
# restaurant.get_number_served()
# restaurant.increment_number_served(3)
# restaurant.get_number_served()
# print("--------------------------------------------------------------------")
# class Ice_cream_stand():
#     '''Discribing a class telling flovours of icecream.'''

#     def __init__(self,flavours = ['chocolate','vanilla','mango','pineapple']):
#         """Initializing attributes of flavours of icecream."""
#         self.flavours = flavours

#     def ice_cream_flavours(self):
#         '''Telling icecream flavours.'''
#         print(f"""We have a icecream of following flavours:
# {tuple(flavour for flavour in self.flavours)}. What you like?""")

# icecream_stand = Ice_cream_stand()
# icecream_stand.ice_cream_flavours()





# """CREATING AN RESTAURANT CLASS WHICH TELLS PYTHON TO MAKE OBJECT REPRESENTING
# AN RESTAURANT
# """
# class Restaurant():  # CLASS
#     '''SIMPLE ATTEMPT TO IMFORM ABOUT RESTAURANT''' # DOCSTRING

#     def __init__(self,restaurant_name,cuisine_type):  # DEFINING ATTRIBUTES
#         '''INITIALIZE RESTAURANT NAME AND CUISINE TYPE'''
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0

#     def describe_restaurant(self):  # DEFINING INSTATNCE METHODS
#         '''DESCRIBING ABOUT RESTAURANT'''
#         print(f"This restaurant named {self.restaurant_name.title()} is \
# famous for 'RasMalai'.")

#     def open_restaurant(self): # DEFININF INSTANCE METHODS
#         '''OPENING TIMING OF THE RESTAURANT'''
#         print(f"""THE OPENING AND CLOSING TIME OF THE RESTAURANT ARE FOLLOWS :
# OPEN  : 9 AM TO 10 PM
# CLOSE : 10 PM TO 9 AM""")

#     def get_number_served(self):
#         """Processing the number of customers served."""
#         print(f"Total {str(self.number_served)} numbers of customers have been \
# served.")
    
#     def update_number_served(self,latest_people_served):
#         '''Updating number of peoples served.'''
#         self.number_served = latest_people_served

#     def increment_number_served(self,current_number_served):
#         '''Total number of peoples served.'''
#         self.number_served += current_number_served

# restaurant = Restaurant("gopal Maharaj","korean cuisine")
# print("--------------------------------------------------------------------")
# print(f"Our restaurant name is '{restaurant.restaurant_name.title()}' and we \
# provide our guests the '{restaurant.cuisine_type.title()}'.")

# restaurant.describe_restaurant()
# print("--------------------------------------------------------------------")
# restaurant.open_restaurant()   
# print("--------------------------------------------------------------------")
# restaurant.number_served
# restaurant.get_number_served()
# restaurant.update_number_served(4)
# restaurant.get_number_served()
# restaurant.increment_number_served(3)
# restaurant.get_number_served()
# print("--------------------------------------------------------------------")
# class Ice_cream_stand(Restaurant):
#     '''Discribing a class telling flovours of icecream.'''

    # def __init__(self,restaurant_name,cuisine_type):            # INHERIT FROM-
#         """Initializing attributes of flavours of icecream."""# -RES. CLASS
#         super().__init__(restaurant_name,cuisine_type)
#         self.flavours = ['chocolate','vanilla','mango','pineapple']

#     def ice_cream_flavours(self):
#         '''Telling icecream flavours.'''
#         print(f"""We have a icecream of following flavours:
# {[flavour for flavour in self.flavours]}. What you like?""")

# icecream_stand = Ice_cream_stand('KrsnaGopal','Maharaj Sofa')
# print(f"Our restaurant name is '{icecream_stand.restaurant_name.title()}' and we \
# provide our guests the '{icecream_stand.cuisine_type.title()}'.")
# icecream_stand.describe_restaurant()





# class Users():

#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = 1

#     def describe_user(self):
#         print(f"Full Name of the user is \
# '{self.first_name.title()} {self.last_name.title()}' and the Age of the \
# user is '{self.age}'.\n")

#     def greet_user(self):
#         print(f"Nice to meet you {self.first_name.title()}. How's going!\n")

#     def read_attempts(self):
#         print(f"ATTEPT {self.login_attempts} OF USER:")

#     def increment_login_attempts(self):
#         '''Increments the number of logins as instance calls the method'''
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         '''Reset the number of login attempts to 0.'''
#         self.login_attempts = 0

# user_info = Users('Radha','Krsna',20)
# user_info.reset_login_attempts()
# user_info.read_attempts()
# print("---------------------------------------------------------------------")
# user_info.describe_user()
# user_info.greet_user()
# print(f"{user_info.first_name.title()} is currently studing in GLA CS branch \
# .\n")
# print("---------------------------------------------------------------------")

# user_info_1 = Users('krsna','gopal',20)
# user_info_1.increment_login_attempts()
# user_info_1.read_attempts()
# print("---------------------------------------------------------------------")
# user_info_1.describe_user()
# user_info_1.greet_user()
# print(f"{user_info_1.first_name.title()} is currently studing in GLA CS branch \
# .\n")

# print("---------------------------------------------------------------------")

# class Admin(Users):
#     '''Describing privileges to the user.'''
#     def __init__(self,first_name,last_name,age):
#         """Initializing the attriibutes for the privileges."""
#         super().__init__(first_name,last_name,age)
#         self.privileges = ["can add post","can del post","can ban user"]
    
#     def show_privileges(self):
#         '''Showing list of privileges to the user.'''
#         print(f'''What you want to do out of the following:
# {self.privileges} ?''')

# admin = Admin('Radha','Krsna',20)
# admin.show_privileges()






# class Users():

#     def __init__(self,first_name,last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.login_attempts = 1

#     def describe_user(self):
#         print(f"Full Name of the user is \
# '{self.first_name.title()} {self.last_name.title()}' and the Age of the \
# user is '{self.age}'.\n")

#     def greet_user(self):
#         print(f"Nice to meet you {self.first_name.title()}. How's going!\n")

#     def read_attempts(self):
#         print(f"ATTEPT {self.login_attempts} OF USER:")

#     def increment_login_attempts(self):
#         '''Increments the number of logins as instance calls the method'''
#         self.login_attempts += 1

#     def reset_login_attempts(self):
#         '''Reset the number of login attempts to 0.'''
#         self.login_attempts = 1

# user_info = Users('Radha','Krsna',20)
# user_info.reset_login_attempts()
# user_info.read_attempts()
# print("---------------------------------------------------------------------")
# user_info.describe_user()
# user_info.greet_user()
# print(f"{user_info.first_name.title()} is currently studing in GLA CS branch \
# .\n")
# print("---------------------------------------------------------------------")

# user_info_1 = Users('krsna','gopal',20)
# user_info_1.increment_login_attempts()
# user_info_1.read_attempts()
# print("---------------------------------------------------------------------")
# user_info_1.describe_user()
# user_info_1.greet_user()
# print(f"{user_info_1.first_name.title()} is currently studing in GLA CS branch \
# .\n")

# print("---------------------------------------------------------------------")
# class Privileges():
#     '''Describing the privileges to the user.'''
#     def __init__(self,privileges = ['can add post','can delete post',\
# 'can ban user']):
#         '''Initializing the attribute of privileges.'''
#         self.privileges = privileges

#     def show_privileges(self):
#         '''Showing privileges one by one.'''
#         print(f"What you wnat to choose among the follwing privileges :")
#         for privilege in self.privileges:
#             print(f"{self.privileges.index(privilege)+1}){privilege}")

# class Admin(Users):
#     '''Describing privileges to the user.'''
#     def __init__(self,first_name,last_name,age):
#         """Initializing the attriibutes for the privileges."""
#         super().__init__(first_name,last_name,age)
#         self.get_privileges = Privileges()
    
# admin = Admin('Radha','Krsna',20)
# admin.describe_user()
# admin.get_privileges.show_privileges()




# class Car():
#     '''A simple attempt to represent a car.'''

#     def __init__(self,make,model,year):
#         """Initialize attributes to describe a car."""
#         self.make1 = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 0   # WE CAN SET DEFAULT VALUES LIKE THIS EVEN-
#                                     # - IF WE DON't HAVE ITS ATTRIBUTE
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + " " + self.make1 + " " + self.model
#         return long_name.title()

#     def update_odometer(self,mileage):
#         """Set the odometer reading to the given value.
#         Set the odometer reading to a given value and,
#         restrict the change if someone tries to roll back the 
#         odometer reading."""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         if mileage < 0:
#             print('Could you tell me how you drove your car in (-)ve values!!')
#         elif mileage < self.odometer_reading:
#             print("You can't roll back an odometer!")
        
#     def read_odometer(self):
#         """Print's statement showing the car's mileage."""
#         print(f"The car has {str(self.odometer_reading)} miles on it.")

#     def increment_odometer(self,miles):
#         self.odometer_reading += miles

#     def fill_gas_tank(self):
#         '''This vehicle contains a gas tank.'''
#         print("Your GasTank have been filled up.")

# print("-----------------------------------------------------------------------")

# my_new_car = Car("audi",'a4',2016)
# print(f"My car name is "+ "'" + my_new_car.get_descriptive_name() + "' its my \
# new car.")
# my_new_car.read_odometer()         # READ THE DEFAULT ODOMETER READING i.e 0
# my_new_car.odometer_reading = 56   # CHANGING THE ODOMETER DEFAULT READING TO 56
# my_new_car.read_odometer()         # READING THE NEW ODOMETER VALUE
# my_new_car.fill_gas_tank()

# print("-----------------------------------------------------------------------")

# my_used_car = Car("mercides",'B1600',2022)
# print(f"Currently I am using the '{my_used_car.get_descriptive_name()}' \
# model car.")
# my_used_car.update_odometer(23500)  # UPDATING ODO. READING USING METHODS
# my_used_car.read_odometer()         # READING THE NEW ODOMETER VALUE
# my_used_car.increment_odometer(100) # INCREMENTING THE INITIAL VALUE BY PRESENT-
#                                     # - VALUE
# my_used_car.read_odometer()         # READING THE NEW ODOMETER VALUE
# my_used_car.fill_gas_tank()

# print("-----------------------------------------------------------------------")

# class Battery():
#     """Modeling a Battery for the Electric_car."""

#     def __init__(self,battery_size = 70):
#         '''Initializing the battery attributes.'''
#         self.battery_size = battery_size

#     def describe_battery(self):
#         '''Print a statement describing the battery size.'''
#         print(f"The battery of car have a battery of {self.battery_size} KwH.")

#     def get_range(self):
#         """Print a statement about the range the battery provides."""
#         if self.battery_size == 70:
#             range = 240
#         elif self.battery_size == 85:
#             range = 270
#         print(f"This car can go approximatelt {str(range)} miles on full \
# charge.")

#     def update_battery(self):
#         '''Updating battery power.'''
#         if self.battery_size == 70:
#             self.battery_size = 85
#         else:
#             self.battery_size = 70

# class Electric_car(Car):
#     '''Represent aspects of a car, specific to electric vehicles.
#     and Initialize attribute of the child class.'''

#     def __init__(self,make,model,year):
#         """Initialize attributes of the parent class."""
#         super().__init__(make,model,year)
#         self.battery = Battery()

#     def fill_gas_tank(self):
#         '''A electric vehicle not contains a gas tank.'''
#         print("This vehicle not having the GasTank!!")

# my_tesla = Electric_car('tesla','model s',2016)
# print(f"I just bought new tesla car named '{my_tesla.get_descriptive_name()}'.")
# my_tesla.battery.describe_battery()
# my_tesla.fill_gas_tank()
# my_tesla.battery.get_range()

# my_tesla.battery.describe_battery()
# my_tesla.battery.update_battery()
# my_tesla.battery.get_range()



# from car import Car
# car1 = Car('audi','a4',2016)
# print(car1.get_descriptive_name())
# car1.odometer_reading = 22
# car1.read_odometer()



# from car1 import Electric_car
# my_tesla = Electric_car('tesla','model-s',2016)
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()
# my_tesla.battery.get_range()



# from car1 import Car,Electric_car
# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
# my_tesla = Electric_car('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())



# import car1
# my_beetle = car1.Car('volkswagen', 'beetle', 2016)
# my_tesla = car1.Electric_car('tesla', 'roadster', 2016)
# print(my_beetle.get_descriptive_name())
# print(my_tesla.get_descriptive_name())




# from car import Car 
# from electric_car import Electric_car
# my_beetle = Car('volkswagen', 'beetle', 2016)
# print(my_beetle.get_descriptive_name())
# my_tesla = Electric_car('tesla', 'roadster', 2016)
# print(my_tesla.get_descriptive_name())




# from collections import OrderedDict

# favorite_languages = OrderedDict() # Notice there are no curly
# # -brackets; the call to OrderedDict() creates an empty ordered dictionary
# # -for us and stores it in favorite_languages.
# favorite_languages['jen'] = 'python'
# favorite_languages['sarah'] = 'c'
# favorite_languages['edward'] = 'ruby'
# favorite_languages['phil'] = 'python'

# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is " + language.title() + ".")




# from random import randint

# class Dice():
#     """Describing the outputs of a dice."""
#     sides_of_dice = 6

#     def roll_dice(self): # Instance method
#         '''Returning the value on the dice.'''
#         choose_random  = randint(1,self.sides_of_dice)
#         return (f"The number you got on the dice is : {choose_random}")

# dice_roll = Dice() # Instance
# # dice_roll.sides_of_dice = 2 # We can further change here if we want
# print(f"----------You are using a dice of {dice_roll.sides_of_dice} \
# sides.---------- ")
# print(dice_roll.roll_dice()) # Calling class




# -------------------------------- CHAPTER - 10 --------------------------------




# with open("/Users'RadhaKrsna/Python/Python_work_from_PDF/\
# Python_crash_course_resources/chapter_10/pi_digits.txt") as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())



# path_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/\
# Python_crash_course_resources/chapter_10/pi_digits.txt"
# with open(path_name) as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())  
#     print(object) 



# path_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/\
# Python_crash_course_resources/chapter_10/pi_digits.txt"
# with open(path_name) as file_object:
#     # contents = file_object.read()  
#     # print(contents.rstrip())  
#     print(type(file_object)) 



# path_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/\
# Python_crash_course_resources/chapter_10/pi_digits.txt"
# with open(path_name) as file_object:
#     for lines in file_object:
#         print(lines.rstrip())    



# path_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/\
# Python_crash_course_resources/chapter_10/pi_digits.txt"
# with open(path_name) as file_object:
#     # content = file_object.read()
#     lines = file_object.readlines()
# for line in lines:
#     print(line.rstrip())
# print(lines)



# path_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/\
# Python_crash_course_resources/chapter_10/pi_digits.txt"
# with open(path_name) as file_object:
#     lines = file_object.readlines()
# print(lines)  # In form of list
# pi_string = ""
# for line in lines:
#     pi_string += line.rstrip()
# print(pi_string)
# new_pi_string = pi_string.replace(' ' , "")
# print(new_pi_string) # In form of string
# print(len(new_pi_string))
# print(type(new_pi_string))



# path_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/\
# Python_crash_course_resources/chapter_10/pi_million_digits.txt"
# with open(path_name) as file_object:
#     lines = file_object.readlines()
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
# print(pi_string[:55] + "..." + pi_string[-5:] + f"""
# And,length of the 'pi_string' is {len(pi_string)} Digits.""")

# birthdate = input("Enter your BirthDate in the format ddmmyyyy :")
# if birthdate in pi_string:
#     print("Your birthday appears in the first million digits of pi!")
# else:
#     print("Your birthday not appears in the first million digits of pi.")



# path_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/Python_Learning.txt"
# with open(path_name) as file_object:
#     contents = file_object.read()
#     print(contents)



# path_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/Python_Learning.txt"
# with open(path_name) as file_object:
#     for line in file_object:
#         print(line.strip())



# path_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/Python_Learning.txt"
# with open(path_name) as file_object:
#     file_string = ''
#     for line in file_object:
#         file_string += line
#     print(file_string)



# path_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/Python_Learning.txt"
# with open(path_name) as file_object:
#     lines = file_object.readlines()
#     print(lines)
# file_string = ''
# for line in lines:
#     file_string += line
# print(file_string)



# path_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/MyCreatedFiles/Python_Learning.txt"
# with open(path_name) as file_object:
#     lines = file_object.readlines()
#     print(lines)
# file_string = ''
# for line in lines:
#     file_string += line
# replace_python_to_C = file_string.replace('Python','C')
# print(replace_python_to_C)


# path_name = 'programming.txt'
# with open(path_name,'w') as file_object:
#     file_object.write("I love programming.")



# path_name = 'programming.txt'
# with open(path_name,'w') as file_object:
#     file_object.write("I love programming.\n")
#     file_object.write("I love creating new games.\n")



# path_name = 'programming.txt' # Some data is already there in this file.
# with open(path_name,'a') as file_object: 
#     file_object.write("Bythe way I am currently working on python.\n")



# i = 0
# maximum_inputs = int(input("Set the limit of names you want to enter : "))
# while i < maximum_inputs:
#     guest_names = input("Enter your name : ")
#     with open('guest_book.txt','a') as file_object:
#         file_object.write(f"{i + 1}. Name of the person :\
# {guest_names.title()}\n")
#         file_object.write(input(f"Hello {guest_names.title()}, Nice to talk you! \
# Enter your response on experience with programming : ")+ "\n")
#     print()
#     i += 1



# i = 0
# maximum_inputs = int(input("Set the limit of names you want to enter : "))
# while i<maximum_inputs:
#     person_name = input("Enter your name : ")
#     person_response = input(f"Hello {person_name}, Enter your response : ")
#     file_name_1,file_name_2 = '/Users'RadhaKrsna/Python/Python_work_from_PDF/person_name.txt','/Users'RadhaKrsna/Python/Python_work_from_PDF/person_response.txt'
#     with open(file_name_1,"a") as file_object_1:
#         file_object_1.write(f"The name of the person is :{person_name}"+"\n")
#     with open(file_name_2,"a") as file_object_2:
#         file_object_2.write(f"The response from the user named {person_name} is :{person_response}"+"\n")
#     i += 1



# first_number = input("Enter the first number : ")
# second_number = input("Enter the second number : ")
# try:
#     divide = int(first_number)/int(second_number)
# except ZeroDivisionError:
#     print("0 Can't be divided with any number !! Try again.")
# print(f"The division of two numbers are : {divide}")



# first_number = input("Enter the first number : ")
# second_number = input("Enter the second number : ")
# try:
#     divide = int(first_number)/int(second_number)
# except ZeroDivisionError:
#     print("0 Can't be divided with any number !! Try again.")
# else:
#     print(f"The division of two numbers are : {divide}")



# print("---To quit press 'Q'---")
# while True:
#     first_number = input("Enter the first number : ").upper()
#     if first_number == "Q":
#         break
#     second_number = input("Enter the second number : ").upper()
#     if second_number == "Q":
#         break
#     try:
#         answer = int(first_number)/int(second_number)
#     except ZeroDivisionError:
#         print("0 Can't be divided with any number !! Try again.")
#     else:
#         print(f"The division of two numbers are : {answer}")



# file_name = 'spam.txt'
# try:
#     with open(file_name) as file_object:
#         content = file_object.read()
#         print(content)
# except FileNotFoundError:
#     print(f"Sorry, But file named '{file_name}' does not exist. Check and try again!!")



# file_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/MyCreatedFiles/Alice_In_Wonderland.txt"
# with open(file_name) as file_object:
#     lines = file_object.readlines()
# string_file = ''
# for line in lines:
#     string_file += line.strip()
# list_of_words = string_file.split()
# print(len(list_of_words))



# file_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/MyCreatedFiles/Alice_In_Wonderland.txt"
# try:
#     with open(file_name) as file_object:
#         contents = file_object.read() # A string of what in .txt file.
# except FileNotFoundError:
#     print(f"Sorry, But file named 'Alice_In_Wonderland.txt' does not exist. Check and try again!!")
# list_of_words = contents.split()
# print(f"The file 'Alice_In_Wonderland.txt' is having about {len(list_of_words)} words.")



# def word_count(file_name):
#     '''Count the approximate number of words in the file.'''

#     try:
#         with open(file_name) as file_object:
#             contents = file_object.read() # A string of what in .txt file.
#     except FileNotFoundError:
#         print(f"Sorry, But file named 'Alice_In_Wonderland.txt' does not exist. Check and try again!!")
#     else:
#         list_of_words = contents.split()
#         print(f"The file {file_name} is having about {len(list_of_words)} words.")
    
# list_of_books = ["Alice_In_Wonderland.txt","book2.txt","book3.txt","book4.txt"]
# for books in list_of_books:
#     word_count(books)



# def word_count(file_name):
#     '''Count the approximate number of words in the file.'''

#     try:
#         with open(file_name) as file_object:
#             contents = file_object.read() # A string of what in .txt file.
#     except FileNotFoundError:
#         # print(f"Sorry, But file named '{file_name}' does not exist. Check and try again!!")
#         pass
#     else:
#         list_of_words = contents.split()
#         print(f"The file {file_name} is having about {len(list_of_words)} words.")
    
# list_of_books = ["Alice_In_Wonderland.txt","book9.txt","book3.txt","book4.txt"]
# for books in list_of_books:
#     word_count(books)


# while True:
#     first_number = input("Enter first number : ").upper()
#     if first_number == 'Q':
#         break
#     second_number = input("Enter second number : ")
#     try:
#         add_numbers = int(first_number) + int(second_number)
#     except ValueError:
#         print("Try to use integers instead of alphabets.")
#     else:
#         print(f"The sum of the numbers are : {add_numbers}")



# file_path_1 = "/Users'RadhaKrsna/Python/Python_work_from_PDF/MyCreatedFiles/cat.txt"
# file_path_2 = "/Users'RadhaKrsna/Python/Python_work_from_PDF/MyCreatedFiles/dog.txt"

# while True:
#     name_of_cats = input("Enter the name of cats : ")
#     if name_of_cats == "QUIT":
#         break
#     with open(file_path_1,"a") as file_object_1:
#         file_object_1.write(f"{name_of_cats}\n")

# print("-----Reading 'cat.txt' file-----")
# try:
#     with open(file_path_1) as file_1:
#         print(file_1.read().strip())
# except FileNotFoundError:
#     print(f"File 'cat.txt' does not exist. Try again!")

# while True:
#     name_of_dogs = input("Enter the name of dogs : ")
#     if name_of_dogs == "QUIT":
#         break
#     with open(file_path_2,"a") as file_object_2:
#         file_object_2.write(f"{name_of_dogs}\n")

# print("-----Reading 'dog.txt' file-----")
# try:
#     with open(file_path_2) as file_2:
#         print(file_2.read().strip())
# except FileNotFoundError:
#     print(f"File 'dog.txt' does not exist. Try again!")



# file_path_1 = "/Users'RadhaKrsna/Python/Python_work_from_PDF/MyCreatedFiles/cat.txt"
# file_path_2 = "/Users'RadhaKrsna/Python/Python_work_from_PDF/MyCreatedFiles/dog.txt"

# while True:
#     name_of_cats = input("Enter the name of cats : ")
#     if name_of_cats == "QUIT":
#         break
#     with open(file_path_1,"a") as file_object_1:
#         file_object_1.write(f"{name_of_cats}\n")

# while True:
#     name_of_dogs = input("Enter the name of dogs : ")
#     if name_of_dogs == "QUIT":
#         break
#     with open(file_path_2,"a") as file_object_2:
#         file_object_2.write(f"{name_of_dogs}\n")

# print("-----Reading 'cat.txt' file-----")
# try:
#     with open(file_path_1) as file_1:
#         print(file_1.read().strip())
# except FileNotFoundError:
#     pass
# print("-----Reading 'dog.txt' file-----")
# try:
#     with open(file_path_2) as file_2:
#         print(file_2.read().strip())
# except FileNotFoundError:
#     pass



# file_path = "/Users'RadhaKrsna/Python/Python_work_from_PDF/MyCreatedFiles/test.txt"
# with open(file_path) as file_object:
#     contents = file_object.read()
# print(f"The number of 'the' in the file are : {contents.lower().count('the')}")



# import json
# numbers = [1,2,3,4,5]
# file_name = 'numbers.json'
# with open (file_name,'w') as file_object:
#     json.dump(numbers,file_object)

# with open(file_name) as file_object_:
#     numbers = json.load(file_object_)
#     print(numbers)
#     print(type(numbers))

# print("""Its the difference between when using Json and not using json.
# When we use json to read and write the file.
# We can store any data_structure to the file but the same thing we can't do in 
# writing and reading the file,Normally.""")

# numbers_1 = [1,2,3,4,5]
# file_name_1 = 'numbers_1.txt'
# with open(file_name_1,"w") as file_object_1:
#     file_object_1.write(str(numbers_1))

# with open(file_name_1) as file_object_1_:
#     numbers_1 = file_object_1_.read()
#     print(numbers_1)
#     print(type(numbers_1))



# import json
# user_name = input("Enter your name : ")
# file_name = 'username.json'
# with open(file_name,"w") as file_object:
#     json.dump(user_name,file_object)
#     print(f"Waiting for you {user_name}. Hope you come soon!!")
# with open(file_name) as file_object_1:
#     user_name = json.load(file_object_1)
#     print(f"Welcome back, {user_name}")



# import json,sys
# # Load for the user name if already stored in the file, Otherwise
# # Prompt the user name, store it and then call it.

# # Program to store the entry entered by the user to the spefied file.
# file_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/MyCreatedFiles/\
# user_name.json"
# user_name = input("Enter your name : ")
# with open(file_name,"w") as file_object:
#     json.dump(user_name,file_object)
#     print(f"Waiting for you {user_name}. Hope you come soon!!")
#     print("Your entry has been saved in the file.")
# print()
# # Program asking the user whether to read the saved file or not.
# while True:
#     while True:
#         temp_1 = input("""To read the entry from the file
# Press (Y for Yes) and (N for No) : """)
#         print()
#         if temp_1 == "Y":
#             break
#         elif temp_1 == "N":
#             print("Thank you, Have a nice day.")
#             sys.exit()
#         else:
#             print("You have not entered a valid input, Try again!!")
#             continue
# # program which open the saved file for the user and if somehow file got 
# # - deleted it created the desired file for the user with the neccessery entry 
# # - and then show this file to the user.
#     try:
# # trying to call the saved file.
#         with open(file_name) as file_object_0:
#             user_name = json.load(file_object_0)
#     except FileNotFoundError:
# # Creating a new file if the desired file got deleted.
#         print(f"""Sorry but file named 'user_name.json' does not exist.
#     We are trying to save a new file for you with the name and location:\
#  '{file_name}'.
#     Kindly enter the data for the file.""")
#         print()
#         user_name_1 = input("Enter your name : ")
#         file_name_1 = "/Users'RadhaKrsna/Python/Python_work_from_PDF/\
# MyCreatedFiles/user_name.json"
#         with open(file_name_1,"w") as file_object_1:
#             json.dump(user_name_1,file_object_1)
#             print(f"Waiting for you {user_name_1}. Hope you come soon!!\
# Your entry have been saved in the file.")
#             print()
#             continue
#     else:
# # Greeting the user as per he entered data in the file.
#         print("----Reading your file----")
#         print(f"Welcome back, {user_name}")
#         break



# import json,sys
# def greet_user(file_name):
#     """Load for the user name if already stored in the file, Otherwise
#     Prompt the user name, store it and then call it."""
#     # Program to store the entry entered by the user to the spefied file.
#     user_name = input("Enter your name : ")
#     with open(file_name,"w") as file_object:
#         json.dump(user_name,file_object)
#         print(f"Waiting for you {user_name}. Hope you come soon!!")
#         print("Your entry has been saved in the file.")
#     print()
#     # Program asking the user whether to read the saved file or not.
#     while True:
#         while True:
#             temp_1 = input("""To read the entry from the file
#     Press (Y for Yes) and (N for No) : """)
#             print()
#             if temp_1 == "Y":
#                 break
#             elif temp_1 == "N":
#                 print("Thank you, Have a nice day.")
#                 sys.exit()
#             else:
#                 print("You have not entered a valid input, Try again!!")
#                 continue
#     # program which open the saved file for the user and if somehow file got 
#     # - deleted it created the desired file for the user with the neccessery entry 
#     # - and then show this file to the user.
#         try:
#     # trying to call the saved file.
#             with open(file_name) as file_object_0:
#                 user_name = json.load(file_object_0)
#         except FileNotFoundError:
#     # Creating a new file if the desired file got deleted.
#             print(f"""Sorry but file named 'user_name.json' does not exist.
# We are trying to save a new file for you with the name and location:'{file_name}'.
# Kindly enter the data for the file.""")
#             print()
#             user_name_1 = input("Enter your name : ")
#             file_name_1 = "/Users'RadhaKrsna/Python/Python_work_from_PDF/\
# MyCreatedFiles/user_name.json"
#             with open(file_name_1,"w") as file_object_1:
#                 json.dump(user_name_1,file_object_1)
#                 print(f"Waiting for you {user_name_1}. Hope you come soon!!\
# Your entry have been saved in the file.")
#                 print()
#                 continue
#         else:
#     # Greeting the user as per he entered data in the file.
#             print("----Reading your file----")
#             print(f"Welcome back, {user_name}")
#             break
# file_name = "/Users'RadhaKrsna/Python/Python_work_from_PDF/MyCreatedFiles/\
# user_name.json"
# greet_user(file_name)



# import json
# def get_username():
#     """Get stored username if available."""
#     file_name = "user_name.json"
#     try:
#         with open(file_name) as file_object:
#             user_data = json.load(file_object)
#     except FileNotFoundError:
#         return None
#     else:
#         return user_data

# def create_n_store_if_not():
#     """Prompt for the file"""
#     user_data = input("Enter your name : ")
#     file_name = "user_name.json"
#     with open(file_name,"w") as file_object:
#         json.dump(user_data,file_object)
#     return user_data

# def greet_user():
#     """Gretting the user."""
#     user_data = get_username()
#     if user_data:
#         print(f"Welcome back, {user_data}")
#     else:
#         user_data = create_n_store_if_not()
#         print(f"Your file with the data '{user_data}' have been saved in the file.")
#         print(f"""----Opening the file with the greeting.----
# Welcome back, {get_username()}!""")
# greet_user()



# import json
# def get_username():
#     """Getting the data if the file already exist."""
#     file_name = "user_name.json"
#     try:
#         with open(file_name) as file_object:
#             user_name = json.load(file_object)
#     except FileNotFoundError:
#         return None
#     else:
#         return user_name

# def greet_user():
#     """Gretting the user."""
#     user_name = get_username()
#     if user_name:
#         print (f"Welcome back, {user_name}")
#     else:
#         user_name = input("Enter your name : ")
#         file_name = "user_name.json"
#         with open(file_name,"w") as file_object:
#             json.dump(user_name,file_object)
#             print(f"Your file with the data '{user_name}' have been saved in \
# the file.")

# greet_user()


# import sys
# from function_1 import get_formatted_name
# print("----To quit press Q----")
# user_first_name = input("Enter your first name : ").lower()
# if user_first_name == "q":
#     sys.exit()
# user_last_name = input("Enter your last name : ").lower()
# print(get_formatted_name(user_first_name.strip(),user_last_name.strip()))


# # MAKING A PASSED TEST...
# # Importing unitest module.
# import unittest
# # Importing function to print fullname
# # -also it's the function we want to testfor.
# from function_1 import get_formatted_name
# # Defining a class to inherit from testcase so that the python know how to 
# # -run the test we write.
# class Name_test_case(unittest.TestCase): 
# # Docstring 
#     """Testing for 'function_1.py'."""
# # Creating a test method to test.
#     def test_first_last_name(self): 
# # Docstring 
#         "Do name like 'Radha Krsna' works?"  
# # Make a variable and store the argument in the function we want to test.
#         formatted_name = get_formatted_name("Radha","Krsna")
# # Within this test method, we call the function 
# # -we want to test and store a return value that we’re interested in testing.

# # we use one of unittest’s most useful features: an assert method.
# # -Assert methods verify that a result you received matches the result you
# # -expected to receive.

# # we use unittest’s assertEqual() method and pass it formatted_name 
# # -and 'Radha Krsna'.
#         self.assertEqual(formatted_name,"Radha Krsna")
# # The line unittest.main() tells Python to run the tests in this file.
# unittest.main()
# # Any method that starts with test_ will be run automatically when we 
# # -run "Python_crash_course_PART_2.py".




# # MAKING A FAIL TEST...
# # Importing unitest module.
# import unittest
# # Importing function to print fullname
# # -also it's the function we want to testfor.
# from function_2_MIDDLE_NAME import get_formatted_name
# # Defining a class to inherit from testcase so that the python know how to 
# # -run the test we write.
# class Name_test_case(unittest.TestCase): 
# # Docstring 
#     """Testing for 'function_1.py'."""
# # Creating a test method to test.
#     def test_first_last_name(self): 
# # Docstring 
#         "Do name like 'Radha Krsna' works?"  
# # Make a variable and store the argument in the function we want to test.
#         formatted_name = get_formatted_name("Radha","Krsna")
# # Within this test method, we call the function 
# # -we want to test and store a return value that we’re interested in testing.

# # we use one of unittest’s most useful features: an assert method.
# # -Assert methods verify that a result you received matches the result you
# # -expected to receive.

# # we use unittest’s assertEqual() method and pass it formatted_name 
# # -and 'Radha Krsna'.
#         self.assertEqual(formatted_name,"Radha Krsna")
# # The line unittest.main() tells Python to run the tests in this file.
# unittest.main()
# # Any method that starts with test_ will be run automatically when we 
# # -run "Python_crash_course_PART_2.py".




# # MAKING A PASSED TEST BY MODIFYING THE FUNCTION SUCH SUCH IT's OPTiONAL TO TAKE MIDDLE NAMES...
# # Importing unitest module.
# import unittest
# # Importing function to print fullname
# # -also it's the function we want to testfor.
# from function_3_MIDDLE_NAME_OPTIONAL import get_formatted_name
# # Defining a class to inherit from testcase so that the python know how to 
# # -run the test we write.
# class Name_test_case(unittest.TestCase): 
# # Docstring 
#     """Testing for 'function_1.py'."""
# # Creating a test method to test.
#     def test_first_last_name(self): 
# # Docstring 
#         "Do name like 'Radha Krsna' works?"  
# # Make a variable and store the argument in the function we want to test.
#         formatted_name = get_formatted_name("Radha","Krsna")
# # Within this test method, we call the function 
# # -we want to test and store a return value that we’re interested in testing.

# # we use one of unittest’s most useful features: an assert method.
# # -Assert methods verify that a result you received matches the result you
# # -expected to receive.

# # we use unittest’s assertEqual() method and pass it formatted_name 
# # -and 'Radha Krsna'.
#         self.assertEqual(formatted_name,"Radha Krsna")
# # The line unittest.main() tells Python to run the tests in this file.
# unittest.main()
# # Any method that starts with test_ will be run automatically when we 
# # -run "Python_crash_course_PART_2.py".



# import unittest
# from function_3_MIDDLE_NAME_OPTIONAL import get_formatted_name
# class Name_test_case(unittest.TestCase):
#     """Tests for function_3_MIDDLE_NAME_OPTIONAL."""

#     def test_first_last_name(self):  # FIRST TEST
#         """Testing the function for first and last name.
#         Do name like 'Radha Krsna' Works?"""
#         formatted_name = get_formatted_name("Radha","Krsna")
#         self.assertEqual(formatted_name,"Radha Krsna")
    
#     def test_first_middle_last_name(self):  # SECOND TEST
#         """Testing the function for first, middle and last name.
#         Do name like 'Radha Gopal Krsna' Works?"""
#         formatted_name = get_formatted_name("Radha","Krsna","Gopal")
#         self.assertEqual(formatted_name,"Radha Gopal Krsna")

# unittest.main()



# import unittest
# from city_country import city_country_name
# class Name_test_case(unittest.TestCase):
#     '''Defining a class to test for function we have written.'''
#     def test_city_country(self):
#         """Testing the function for City,Country."""
#         area = city_country_name("Jaipur","India")
#         self.assertEqual(area,"Jaipur,India")
# unittest.main()




# import unittest
# from city_country_population import city_country_name
# class Name_test_case(unittest.TestCase):
#     '''Defining a class to test for function we have written.'''
#     def test_city_country(self):
#         """Testing the function for City,Country."""
#         area = city_country_name("Jaipur","India")
#         self.assertEqual(area,"Jaipur,India")
# unittest.main()




# import unittest
# from city_country_population_optional import city_country_name
# class Name_test_case(unittest.TestCase):
#     '''Defining a class to test for function we have written.'''

#     def test_city_country(self):
#         """Testing the function for City,Country."""
#         area = city_country_name("Jaipur","India")
#         self.assertEqual(area,"Jaipur,India")

#     def test_city_country_population(self):
#         "Testing the function for City,Country,Population."
#         area = city_country_name("Jaipur","India","20000000")
#         self.assertEqual(area,"Jaipur,20000000,India")

# unittest.main()


# from Anonymous_Survey import Anonymous_survey
# questions = input("Type your question : ")
# my_survey = Anonymous_survey(questions)
# print()
# while True:
#     enter_response = input("Enter your response for the question : ")
#     if enter_response == "Q":
#         break
#     else:
#         my_survey.store_response(enter_response)
# print()
# print("Thanks to each and eveyone who participated in the survey.\n")
# my_survey.show_results()


# Testing class for single response.
# import unittest
# from Anonymous_Survey import Anonymous_survey

# class Test_anonymous_survey(unittest.TestCase):
#     """Test for the class Anonymous_survey."""

#     def test_store_single_response(self):
#         """Test that a single response is stored properly."""
#         my_survey = Anonymous_survey("Which programming language you learnt first ?")
#         my_survey.store_response("Python")
#         self.assertIn("Python",my_survey.responses)
# unittest.main()



# # Testing class for single and multiple response.
# import unittest
# from Anonymous_Survey import Anonymous_survey
# class Test_anonymous_survey(unittest.TestCase):
#     """Test for the class anonymous survey."""
#     def test_single_response(self):
#         """Testing single response."""
#         my_survey = Anonymous_survey("Which programming language you learnt first ?")
#         my_survey.store_response("Python")
#         self.assertIn("Python",my_survey.responses)

#     def test_multiple_responses(self):
#         """Testing multiple responses."""
#         my_survey = Anonymous_survey("Which programming language you learnt first ?")
#         responses = ["Python","C","Java"]
#         for response in responses:
#             my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response,my_survey.responses)
# unittest.main()





# # Testing class for single and multiple response and also using setUp() method.
# import unittest
# from Anonymous_Survey import Anonymous_survey
# class Test_anonymous_survey(unittest.TestCase):
#     """Test for the class anonymous survey."""

#     def setUp(self):
#         """Create a survey and a set of responses for use in all test methods."""
#         question = "Which programming language you learnt first ?"
#         self.my_survey = Anonymous_survey(question)
#         self.responses = ["Python","C","Java"]

#     def test_single_response(self):
#         """Testing single response."""
#         self.my_survey.store_response(self.responses[0])
#         self.assertIn("Python",self.my_survey.responses)

#     def test_multiple_responses(self):
#         """Testing multiple responses."""
#         responses = ["Python","C","Java"]
#         for response in responses:
#             self.my_survey.store_response(response)
#         for response in responses:
#             self.assertIn(response,self.my_survey.responses)
# unittest.main()


















