def main():...
print("Exercise 1: List fruits")

my_list = ["apple", "banana", "orange", "grape"]

# Adding a new string
my_list.append("Straberies") # "apple", "banana", "orange", "grape"
print(my_list)
my_list.append("mango") # "apple", "banana", "orange", "grape" "mango"
print(my_list)
# Removing the third element (index 2)
del my_list[1]  # "apple", "orange", "grape" "mango"
print(my_list)
# Sort in descending order
my_list.sort(reverse=True) # mango, grape, orange, apple

print(my_list)

print()
print()

if __name__=="__main__":
    main()