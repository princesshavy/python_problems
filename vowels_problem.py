def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count

string= str(input("Enter word/sentence :")) 
print("Number of vowels:", count_vowels(string))

#                        OR
# def getCount(s):
#   num_vowels = 0
 #   return sum(c in 'aeiou' for c in s)
  #  return num_vowels

   #                             OR
#   def getCount(inputStr):
#     num_vowels = 0
#     for char in inputStr:
#         if char in "aeiouAEIOU":
#            num_vowels = num_vowels + 1
#     return num_vowels