from search import search_function
from search_helper import search_helper

example_results = ["how to drink water", "popular video games", "visual studio download", "benefits of food", "how to eat food", "benefits of water"]

user_search = input("\nInput search: ")

output = search_function(example_results, search_helper(user_search))

print("")
i = 1
for list in output:
    print(str(i) + ") " + list[0])
    i+=1
print("")