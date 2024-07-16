
# try:
#     file = open("a_file.txt")
# except FileNotFoundError as error_message:
#     open("a_file.txt", "w")
#     print(f"The file {error_message} does not exist")
# except KeyError as error_message:
#     print("That key does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise KeyError("I made this up")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Height is too tall.")
bmi = weight / height**2
print(bmi)

#KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["WOW"]

#IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

#TypeError
# text = "abc"
# print(text+5)

# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there were no exceptions
# finally: do this no matter what happens