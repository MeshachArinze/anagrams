# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagrams(string1,string2):  
    # [assignment] Add your code here
    list1 = list(string1)  
    list2 = list(string2)  
    # Sort the list value  
    list1.sort()  
    list2.sort()  
  
    initial = 0  
    check = True  
  
    while initial < len(string1) and check:  
        if list1[initial]==list2[initial]:  
            initial = initial + 1  
        else:  
            check = False  
  
    return check  
  
print(find_anagrams('word','orwd'))  