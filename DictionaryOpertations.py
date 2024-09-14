def main():...
print("Exercise 8: Dictionary Operations")

student_dict = {'name': 'Elysee', 'age': 37, 'major': 'Computer Science'}

# Add GPA
student_dict['GPA'] = 3.85 # GPA = 3.85

# Modify age
student_dict['age'] = 23 # age = 23

# Remove major
student_dict.pop('major') # no more comp sci

# Print all keys and values
for key, value in student_dict.items():
    print(f"{key}: {value}")

if __name__=="__main__":
    main()