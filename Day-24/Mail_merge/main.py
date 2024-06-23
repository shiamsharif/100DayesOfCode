#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp

#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

"""  firstTry """

# with open("../Mail_merge/Input/Names/invited_names.txt") as name:
#     each_name = name.readline()
#     # print(each_name)

# with open("../Mail_merge/Input/Letters/starting_letter.txt") as letter:
#     letter1 = letter.read()
#     x = letter1.replace("[name]", f"{each_name}")
#     print(x)


"""  second try and won """
with open("../Mail_merge/Input/Names/invited_names.txt") as invited_name:
    name_list = invited_name.readlines()
    names = [item.replace("\n", "") for item in name_list]

for name in names:
    with open("../Mail_merge/Input/Letters/starting_letter.txt") as letter:
        letter1 = letter.read()
        x = letter1.replace("[name]", f"{name}")
        
        filename = f"../Mail_merge/Output/ReadyToSend/Letter_for_{name}.txt"
        with open(filename, mode="w") as f:
            f.write(x)
        print(f"Created {filename}")


""" Angela's Solution with bug"""
# PLACEHOLDER = "[name]"

# with open("./Input/Names/invited_names.txt") as names_file:
#     names = names_file.readlines()

# with open("./Input/Letters/starting_letter.txt") as letter_file:
#     letter_contents = letter_file.read()
#     for name in names:
#         stripped_name = name.strip()
#         new_latter = letter_contents.replace(PLACEHOLDER, stripped_name)
#         with open(f"./Output/Angela/letterFor{name}.txt", mode="w") as completed_letter:
#             completed_letter.write(new_latter)