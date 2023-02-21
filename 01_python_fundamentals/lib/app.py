#!/usr/bin/env python3

# 📚 Review:
    # Python environment set up
	# Python debugging tools 
	# Python datatypes 

# 🚨 To enable ipdb debugging, first import "ipdb"
import ipdb

# 1. ✅ Create a condition to check a pet's mood
    # If "pet_mood" is "Hungry!", "Rose needs to be fed."
    # If "pet_mood" is "Rowdy!", "Rose needs a walk."
    # In all other cases, "Rose is all good."

    # Note => Feel free to set your own values for "pet_mood" to view various outputs.

pet_mood = "Rowdy!"
pet_name = "Rose"

# ipdb.set_trace()

# if pet_mood == "Hungry!":
#     print(f"{pet_name} needs to be fed.")
# elif pet_mood == "Rowdy!":
#     print(f"{pet_name} needs a walk.")
# else:
#     print(f"{pet_name} is all good.")

# 2. ✅ Create a ternary operator using "pet_mood" as a condition:
    # If pet_mood is "Hungry!" => "Rose needs to be fed."
    # In all other cases => "Rose is all good."

print(f"{pet_name} needs to be fed.") if pet_mood == "Hungry!" else print(f"{pet_name} is all good.")

# 3. ✅ Create a function (say_hello) that returns the string "Hello, world!"
    # Test invocation of "say_hello" in ipdb using "say_hello()"
    # say_hello() => "Hello, world!"

def say_hello():
    print("Hello, world!")

say_hello()

# 4. ✅ Create a function (pet_greeting) that will return a string with interpolated pet's name
    # Test invocation of "pet_greeting" in ipdb using "pet_greeting()"
    # pet_greeting("Rose") => "Rose says hello!"
    # pet_greeting("Spot") => "Spot says hello!"

def pet_greeting(name = "Pet"):
    print(f"{name} says hello!")

pet_greeting(pet_name)

# 5. ✅ Move conditional logic from Deliverable 1 into a function (pet_status) so that we may use it with different pets / moods
    # Test invocation of "pet_status" in ipdb using "pet_status(pet_name, pet_mood)"
    # pet_status("Rose", "Hungry!") => "Rose needs to be fed."
    # pet_greeting("Spot", "Rowdy!") => "Spot needs a walk."
    # pet_greeting("Bud", "Relaxed") => "Bud is all good."
    
    # Take a moment to note that "pet_name" and "pet_mood" parameters are within Local Scope and take priority over "pet_name" and "pet_mood"
    # in Global Scope.

def pet_status(pet_name, pet_mood):
    if pet_mood == "Hungry!":
        print(f"{pet_name} needs to be fed.")
    elif pet_mood == "Rowdy!":
        print(f"{pet_name} needs a walk.")
    else:
        print(f"{pet_name} is all good.")

pet_status("Bingbong", "Rowdy!")


# 6. ✅ Create a function (pet_birthday) that will increment a pet's age up by 1. Use try / except to handle errors. 
    # If our function is given an incorrect datatype, it should handle the TypeError exception and alert the user
    # pet_birthday(10) => "Happy Birthday! Your pet is now 11."
    # pet_birthday("oops") => "Type Error Occurred"

    # Note => To view more common Python exceptions, visit https://docs.python.org/3/library/exceptions.html

def pet_birthday(age):
    try:
        print(f"Happy Birthday! Your pet is now {age+1}.")
    except TypeError:
        print("Type Error Occurred")
    except NameError:
        print("Name Error Occurred")

pet_birthday(10)
pet_birthday("10")
pet_birthday(ten)

# 🚨 To create an ipdb breakpoint, comment / uncomment line below:
# ipdb.set_trace()


