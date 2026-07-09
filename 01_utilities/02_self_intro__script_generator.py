from datetime import date, datetime

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
proffession = input("Enter your profession: ")
hobby = input("Enter your hobby: ")

script = f"Hi everyone, my name is {name}. I am {age} years old and I live in {city}. I work as a {proffession}. In my free time, I love {hobby}. It is great to meet you all."

date = datetime.today().strftime("%d-%m-%Y")
script += f"\n\nThis script was generated on {date}."

print("\nGenerated Script:\n")
print(script)