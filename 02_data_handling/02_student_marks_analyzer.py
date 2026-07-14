
def collect_student_data():
    students = {}

    while True:
        name = input("Enter student name (or type 'done' to finish): ").strip()
        if name.lower() == 'done':
            break

        try:
            marks = float(input(f"Enter marks for {name}: "))
            students[name] = marks
        except ValueError:
            print("Invalid input. Please enter a valid number for marks.")

    return students

def display_student_data(students):
    if not students:
        print("No student data available.")
        return
    
    marks = list(students.values())
    average_marks = sum(marks) / len(marks)
    max_marks = max(marks)
    min_marks = min(marks)

    topper = [name for name, mark in students.items() if mark == max_marks]
    lowest_scorer = [name for name, mark in students.items() if mark == min_marks]

    print("\nStudent Data:")
    for name, mark in students.items():
        print(f"{name}: {mark}")

    print(f"\nAverage Marks: {average_marks:.2f}")
    print(f"Topper(s): {', '.join(topper)}")
    print(f"Lowest Scorer(s): {', '.join(lowest_scorer)}")
    print(f"Maximum Marks: {max_marks}")
    print(f"Minimum Marks: {min_marks}")

data = collect_student_data()
display_student_data(data)