p_dictionary = {
    "Bug" : "This is an Error.",
    "Function" : "A place of code that you can easily call over and again",            

}
#Retrieving items from dictionary.
print(p_dictionary["Function"])

#Adding new ittems to dictionary.
p_dictionary["Loop"] = "The action of doing something over and over again."
# print(p_dictionary)

#empty dictionary
empty_dictionary = {}
print(empty_dictionary)


#edit an item in a dictionary
p_dictionary["Bug"] = "A bug is every thing of a programmer."
# print(p_dictionary)

#Loop through a dictionary.
for key in p_dictionary:
    print(key)
    print(p_dictionary[key])