# # Variable for hometown name
# hometown_name = "Springfield"

# # Variable for hometown statistics
# hometown_statistics = {
#     "Population": 100000,
#     "Area": 50.2,
#     "Average Temperature": 20.5
# }

# # Printing the variables
# print(hometown_name)
# print(hometown_statistics)


# # Hometown statistics
# hometown_statistics = {
#     "Population": 100000,
#     "Area": 50.2
# }

# # Function to calculate population density
# def calculate_population_density(population, area):
#     density = population / area
#     return density

# # Calling the function with hometown statistics
# density = calculate_population_density(hometown_statistics["Population"], hometown_statistics["Area"])

# # Printing the population density
# print("Population Density:", density)

# # Hometown statistics
# hometown_statistics = {
#     "Population": 100000,
#     "Area": 50.2
# }

# # Function to generate the sentence about population density
# def get_population_density_sentence(population, area):
#     density = population / area
#     sentence = "The population density of my hometown is {:.2f} people per square kilometer.".format(density)
#     return sentence

# # Calling the function with hometown statistics
# density_sentence = get_population_density_sentence(hometown_statistics["Population"], hometown_statistics["Area"])

# # Printing the population density sentence
# print(density_sentence)



# Hometown statistics
# hometown_statistics = {
#     "Population": 100000,
#     "Area": 50.2
# }

# Function to generate the sentence about population density
# def get_population_density_sentence(population, area):
#     density = population / area
#     sentence = "The population density of my hometown is {:.2f} people per square kilometer.".format(density)
#     return sentence

# # Checking if hometown statistics are available
# if "Population" in hometown_statistics and "Area" in hometown_statistics:
#     # Calling the function with hometown statistics
#     density_sentence = get_population_density_sentence(hometown_statistics["Population"], hometown_statistics["Area"])
# else:
#     # Using default values
#     default_population = 100000
#     default_area = 50.2
#     density_sentence = get_population_density_sentence(default_population, default_area)

# # Printing the population density sentence
# print(density_sentence)


# hometown_statistics = {
#     "Population": 100000,
#     "Area": 50.2
# }

# # Function to generate the sentence about population density
# def get_population_density_sentence(population, area):
#     density = population / area
#     sentence = "The population density of my hometown is {:.2f} people per square kilometer.".format(density)
#     return sentence

# # Using the hometown statistics if available, otherwise using default values
# population = hometown_statistics.get("Population", 100000)
# area = hometown_statistics.get("Area", 50.2)

# # Calling the function with the population and area values
# density_sentence = get_population_density_sentence(population, area)

# # Printing the population density sentence
# print(density_sentence)

# Procedural Python challenges

# Make a program that counts down from 10 to 0 but instead of 0 it says Boom
# import time

# def countdown():
#     for num in range(10, 0, -1): #iterate from 10 down to 1 (exclusive), with a step of -1. 
#         print(num)
#         time.sleep(1)  # Wait for 1 second before printing the next number

#     print("Boom!")

# countdown()

# def find_repeated_names(list1, list2):
#     # Convert the lists to sets to eliminate duplicates
#     set1 = set(list1)
#     set2 = set(list2)

#     # Find the intersection of the two sets
#     common_names = set1.intersection(set2) #The intersection() method returns a set that contains the similarity between two or more sets.

#     if common_names:
#         print("Repeated names found:", common_names)
#     else:
#         print("No repeated names found")

# # Example lists of names
# names_list1 = ["John", "Emma", "Oliver", "Sophia", "Liam"]
# names_list2 = ["Sophia", "Emma", "Ava", "Oliver", "Noah"]

# # Calling the function with the lists
# find_repeated_names(names_list1, names_list2)

# import  from file import class 
from name_generator import NameGenerator

# Example usage
name = "John"
month_of_birth = "april"

name_generator = NameGenerator()

dragon_name = name_generator.dragon_name(name, month_of_birth)
penguin_name = name_generator.penguin_name(name, month_of_birth)

print("Dragon Name:", dragon_name)
print("Penguin Name:", penguin_name)