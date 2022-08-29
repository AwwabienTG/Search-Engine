from search import search_function
from search_helper import search_helper

example_results = ["how to eat food", "how to drink water", "popular video games", "visual studio download", "benefits of food", "benefits of water"]

user_search = input("Input search: ")

print(search_function(example_results, search_helper(user_search)))