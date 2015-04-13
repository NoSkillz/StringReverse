__author__ = 'VerDe'

string = input("Throw me a string: ")
reversed_string = ""
'''
We pass through each letter in the string starting from it's last index, making our way towards the first index (0)
We append each letter as we go through them to our blank string
When both string are of equal length, we print the result and break out of the loop
'''

if len(string) > 0:
    for letter in string[::-1]:
        reversed_string += letter
        if len(string) == len(reversed_string):
            print(reversed_string)
            break
else:
    print("Invalid input. Quitting")