from traceback import print_last


def main():...
print("Exercise 3: Student Name")

student_names = {"John", "Emma", "Sophia","James"}
print(student_names)
# Add `"Oliver"` to the set
student_names.add("Oliver")
print(student_names)
# Remove `"Sophia"` from the set.
student_names.remove("Sophia")

print(student_names)
# Add `"John"` to the set
student_names.add("John")
print(student_names)
if __name__=="__main__":
    main()