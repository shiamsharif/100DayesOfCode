#Function with output:


# def format_name(f_name, l_name):
#     print(f_name.title())
#     print(l_name.title())

# format_name("shiam","shariF") #output:Shiam \n Sharif



# def format_name(f_name, l_name):
#     temp1 = f_name.title()
#     temp2 = l_name.title()
#     return f"{temp1} {temp2}"

# print(format_name("shiam","shariF"))


def format_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Tou did not provide valid inputs."
    temp1 = f_name.title()
    temp2 = l_name.title()
    return f"Result : {f_name} {l_name}"

print(format_name(input("What is your first name? "),input("What is your last name? ")))