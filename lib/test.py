def divide(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")

# # divide("five","more")
# # divide(5,10)
# # divide(0,5)
# # divide(5,below)

# dog = "cuddly"

# dict_map = {
#      "hungry": "Refilling food bowl.",
#     "thirsty": "Refilling water bowl.",
#     "playful": "Playing tug-of-war.",
#     "cuddly": "Snuggling.",
# }

# # Remember that a dictionary's .get() method lets us set a default value!
# owner = dict_map.get(dog, "Reading newspaper.")