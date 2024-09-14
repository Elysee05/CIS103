def main():...
print("Exercise 6: List Operations")

my_list = [10, 20, 30, 40, 50]

# Adding a new integer
my_list.append(60) # 10, 20, 30, 40, 50, 60
my_list.append(70) # 10, 20, 30, 40, 50, 60,70
# Removing the third element (index 2)
my_list.pop(2)     # 10, 20, 40, 50, 60

# Sort in descending order
my_list.sort(reverse=True) # 60, 50, 40, 20, 10

print(my_list)

print()
print()

if __name__=="__main__":
    main()