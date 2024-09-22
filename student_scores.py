from traceback import print_last


def main():...
print("Exercise 3: Student Scores")

student_score = {"John": 85, "Emma": 92, "Sophia": 78, "James": 89}
print(student_score)
# Add `"Oliver"` to the set
student_score["Olivier"] = "95"
print(student_score)
# Update Score Sophia
student_score["Sophia"] = 82
print(student_score["Emma"])
# Remove `"Sophia"` from the set.
del student_score["Sophia"]


# Add `"John"` to the set


if __name__=="__main__":
    main()