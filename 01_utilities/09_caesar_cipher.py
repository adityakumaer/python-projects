

def encrypt(message, key):
    final = ""
    for msg in message:
        if msg.isalpha():
            char_num = ord("A") if msg.isupper() else ord("a")
            shift = (ord(msg) - char_num + key) % 26 + char_num
            final += chr(shift)
        else:
            final += msg
    return final


def decrypt(message, key):
    return encrypt(message, -key)


print("\nWelcome to caesar chipher")

user = input("Enter encrypt(E) or decrypt(D): ").strip().lower()

if user == "e":
    message = input("Enter your message: ")
    try:
        key = int(input("Enter key value (1-25): "))
        result = encrypt(message, key)
        print("Here is your encrypt message:")
        print(result)
    except ValueError:
        raise ValueError("Invalid key!")

elif user == "d":
    message = input("Enter your message: ")
    try:
        key = int(input("Enter key value (1-25): "))
        result = decrypt(message, key)
        print("Here is your decrypt message:")
        print(result)
    except ValueError:
        raise ValueError("Invalid key!")

else:
    print("Invalid input!")