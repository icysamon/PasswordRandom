import random

# Configuration
num = True # Whether to use numbers
sign = True # Whether to use sign
letter_m = True # Whether to use majuscule
letter_l = True # Whether to use lowercase 
digit = 12 # Password digit

# Font list
list = []
num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
sign_list = ["#", "@", "!", "~", "$", "%", "^", "&", "*", "(", ")", "-", "=", "+"]
letter_m_list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letter_l_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

# List combination
if(num): list += num_list
if(sign): list += sign_list
if(letter_m): list += letter_m_list
if(letter_l): list += letter_l_list

# Output
while(1):

    for cnt in range(digit):
     print(random.choice(list), end="")

    print()
    input('Press any key to rebuild.')
