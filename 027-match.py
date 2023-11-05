name = input("What's your name? ")

# initial version
# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffidor")
# elif name == "Ron":
#     print ("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# optimized version
# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# initial version
# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffindor")
#     case "Draco":
#         print("Slytherin")
#     case _:
#         print("Who?")
        
# optimized version
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Harry" | "Draco":
        print("Slytherin")
    case _:
        print("Who?")