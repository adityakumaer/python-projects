

def friendship_calculator(name1, name2):
    combined_names = (name1 + name2).lower()
    
    keyword = "aeiou"
    
    count_sum = 0
    for letter in keyword:
        letter_count = combined_names.count(letter)
        count_sum += letter_count
        
    score = (count_sum * 13) % 101 
    
    return score

def run_friendship_calculator():
    name1 = input("Enter first friend name:")
    name2 = input("Enter second friend name:")
    score = friendship_calculator(name1, name2)

    print(score)


run_friendship_calculator()