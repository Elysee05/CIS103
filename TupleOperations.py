def main():...
print("Exercise 7: Tuple Operations")

my_tuple = [4, 5, 6, 7, 8]

# Print first and last elements
print("First element:", my_tuple[0]) # 4
print("Second element:", my_tuple[1]) # 5
print("third element:", my_tuple[2]) # 6
print("4th element:", my_tuple[3]) # 7
print("Last element:", my_tuple[-1]) # 8

# Attempt to modify the second element
try:
    my_tuple[1] = 10
except TypeError as e:
    print("Error:", e)

print()
print()
if __name__=="__main__":
    main()