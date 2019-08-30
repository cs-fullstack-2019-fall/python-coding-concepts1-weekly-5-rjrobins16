# # python-coding_concepts1-weekly-5
#
# You must push BEFORE 2:30pm or your answers will not be graded.
# Once you finish, do not leave the property. You will be interviewed about your questions at 2:45pm.
#
# DON'T FORGET TO USE THE assessment_handout.txt FILE.
#
# Do NOT use any notes or previous projects on this test.
# Each individual question file has the same questions as the README.


# ### Problem 1:
# Ask a user for the year they were born by calculating their age.
# Assuming they already had their birthday and it’s 2019 print “You are [AGE] years old”
birthyear = int(input("Enter the year you were born."))
age = 2019 - birthyear
print(f"You are {age} years old.")


# ### Problem 2:
# Ask the user for a string. If they enter “Kenn”, “Kevin”, “Erin”, or
# “Autumn” print “Hello Teacher”. Otherwise print “Hello Student”

usersname = input("Enter your name")

if usersname == "Kenn" or usersname == "Autumn" or usersname == "Kevin" or usersname == "Erin":
    print ("Hello Teacher")
else:
    print ("Hello Student")


# ### Problem 3:
# Ask the user for a negative number. Print from 7 down to the user's
# negative number. You must include the user's number.

usersnumber= int(input("Enter a negative number."))
for x in range(7,usersnumber-1,-1):
    print (x)


# ### Problem 4:
# Ask the user to enter a number between -10 to -5. If their input is not
# between the two numbers ask them to do it again until they get it right.
# Afterward they print the correct number, print "Good job"

usersnumber2 = int(input("Enter a number between -10 to -5."))
while usersnumber2 <= -11 or usersnumber2 >= -4:
    usersnumber2 = int(input("Enter a number between -10 to -5."))

print ("Good Job!")


# ### Problem 5:
# Create the list: squad = ["One", "Two", "Three", "Four", "Five"].
# Print the list in reverse without using a list method.

squad = ["One", "Two", "Three", "Four", "Five"]
print(squad[6:0:-1])
#dont remember how to do this backwards

# ### Problem 6:
# Create a function that will have the string firstName as a parameter.
# In the function ask the user for their last name. Print "Hello [FIRST & LAST NAME]" in the function. Call that function

def prob6(first):
    userlastname = input("Enter your last name.")
    print(f"Hello {first} {userlastname}!")

prob6("Rachel")

# ### Problem 7:
# Create the class Books with  properties/attributes.
# Create a class method that will change the rating of the book. Outside of the class,
# create three objects of the class Book and put them in an array. Lastly, USING THE ARRAY print only the
# names of the books using any method we’ve learned in class.


class Books:
    def __init__(self, name, rating, genre, author):
        self.name = name
        self.rating = rating
        self.genre = genre
        self.author = author

    def changeRating(self,newrating):
        self.rating = newrating


book1 = Books("Cat in Hat", 4, "PG", "Suess")
book2 = Books("XXX", 5, "PG", "Sally")
book3 = Books("Tina", 4, "G", "Me")

bookarray = [book1,book2,book3]
#for loop prints each book name only!
for eachbook in bookarray:
    print(eachbook.name)

# ### Problem 8:
# Create a function that asks the user to enter a number. If the number is between and include
# -50 and 5, return "Funds too low". If the number is between 5 and 50, return “You should add more funds.”
# If the number is more than 50, return “Just enough.”
def problem8():
    usernumber8 = int(input("Enter a number."))
    if usernumber8 <-50 and usernumber8 > 5:
        return "Funds too low"
    if usernumber8 > 5 and usernumber8 > 50:
        return "You should add more funds"
    elif usernumber8 > 50:
        return "Just enough"

print(problem8())

#
# ### Problem 9:
# Ask the user for a positive number. Create an empty array and starting from zero, add each number
# by 1 into the array. Print EACH ELEMENT of the array.
usernum9 = int(input("Enter a number."))
emptyarray = []
for x in range(0,usernum9+1,1):
    emptyarray.append(x)

for eachElement9 in emptyarray:
    print (eachElement9)


#
# ### Problem 10:
# Create a new empty array called pet_list. Create a Pet class with a type and breed attribute/property.
# Include a method that will print each attribute/property. Add 3 pet objects to the pet_list array.
# Print the attributes/properties for each pet.
class Pet:
    def __init__(self,type,breed):
        self.type = type
        self.breed = breed
    def __str__(self):
        self.type = f"The dog is this {self.type} type."
        self.breed =f"The dog is this {self.breed} breed."
        string = self.type,


dog1 = Pet("puppy","pitbull")
dog2 = Pet("MOM", "YORKIE")
dog3 = Pet("old","lab")
pet_list = [dog1,dog2,dog3]

print(dog1.__str__())
print(dog2.__str__())
print(dog3.__str__())