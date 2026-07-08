
num_people = int(input("Enter the number of people: "))
total_bill = float(input("Enter the total bill amount: "))

name = []
for i in range(num_people):
    person_name = input(f"Enter the name of person {i + 1}: ").strip()
    name.append(person_name)

bill_per_person = round(total_bill / num_people, 2)


print("\nBill split:\n")

for i in range(num_people):
    print(f"{name[i]} should pay: {bill_per_person}")