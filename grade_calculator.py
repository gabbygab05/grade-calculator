try:
    name = input("Enter student name: ").strip()

    if not name:
        print("Error: Student name cannot be empty.")
        exit()

    quiz = float(input("Enter quiz grade: "))
    assignment = float(input("Enter assignment grade: "))
    exam = float(input("Enter exam grade: "))

    if not all(0 <= grade <= 100 for grade in [quiz, assignment, exam]):
        print("Error: Grades must be between 0 and 100.")
        exit()

    final_grade = (quiz * 0.30) + (assignment * 0.30) + (exam * 0.40)

    print("\n=== Grade Result ===")
    print(f"Student: {name}")
    print(f"Final Grade: {final_grade:.2f}")

    if final_grade >= 90:
        letter_grade = "A"
    elif final_grade >= 80:
        letter_grade = "B"
    elif final_grade >= 75:
        letter_grade = "C"
    else:
        letter_grade = "F"

    print(f"Letter Grade: {letter_grade}")

    if final_grade >= 75:
        print("Status: PASSED")
    else:
        print("Status: FAILED")

except ValueError:
    print("Error: Please enter valid numbers for the grades.")