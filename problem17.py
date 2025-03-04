# Problem 17 : Number Letter Counts

def letter_counts():
    dictionary = {
        1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten",
        11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
        16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen",
        20: "twenty", 30: "thirty", 40: "forty", 50: "fifty",
        60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety",
        100: "hundred", 1000: "thousand"
    }
    
    total_letters = 0
    
    letter_counts_dict = {
        num: len(word.replace(" ", "").replace("-", ""))
        for num, word in dictionary.items()
    }

    for num in range(1, 1001):
        
        if num == 100:
            total_letters += letter_counts_dict[1] + letter_counts_dict[100]
        
        elif num == 1000:
            total_letters += letter_counts_dict[1] + letter_counts_dict[1000]
                
        elif num in letter_counts_dict:
            total_letters += letter_counts_dict[num]
        
        elif num < 100:
            tens, ones = divmod(num, 10)
            total_letters += letter_counts_dict[tens * 10]
            if ones:
                total_letters += letter_counts_dict[ones]
        
        elif num < 1000:
            hundreds, remainder = divmod(num, 100)
            total_letters += letter_counts_dict[hundreds]
            total_letters += letter_counts_dict[100] 
            if remainder:
                total_letters += 3
                if remainder in letter_counts_dict:
                    total_letters += letter_counts_dict[remainder]
                else:
                    tens, ones = divmod(remainder, 10)
                    total_letters += letter_counts_dict[tens * 10]
                    if ones:
                        total_letters += letter_counts_dict[ones]
        else:
            pass
    
    return total_letters

print(letter_counts())
