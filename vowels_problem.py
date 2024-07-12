def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count

string= str(input("Enter word/sentence :")) 
print("Number of vowels:", count_vowels(string))
