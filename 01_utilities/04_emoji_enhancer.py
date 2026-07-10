
emoji = {"happy": "😊", "love": "❤️", "okay": "👍" , "sad": "😢", "code": "💻"}

message = input("Enter a message: ")

updated_message = []
for word in message.split():
    cleaned_word = word.strip(".,!?;:()\"'").lower()
    emoji_symbol = emoji.get(cleaned_word, "")
    if emoji_symbol:
        updated_message.append(f"{word} {emoji_symbol} ")
    else:
        updated_message.append(word)

final_message = " ".join(updated_message)
print("\nEnhanced message with emojis:")
print(final_message)    