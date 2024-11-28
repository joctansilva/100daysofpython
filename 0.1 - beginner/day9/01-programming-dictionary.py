#Associating key to value

programing_dictionary = {
  "Bug": "An error in a program that prevents it from running correctly", 
  "Loop": "The action of doing something over and over again",
}

print(programing_dictionary["Loop"])

#Adding new key and value
programing_dictionary["Function"] = "A piece of code that you can easily call over and over again"
print(programing_dictionary)

#Create a empty list

empty_dictionary = {}

#Adding key and value to the empty list

empty_dictionary["Bug"] = "An error in a program that prevents it from running correctly"
empty_dictionary["Loop"] = "The action of doing something over and over again"

print(empty_dictionary)

#Loop through the dictionary

for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])