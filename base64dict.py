chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
base64_dict_CB = {}
base64_dict_BC = {}

"""
#Fills base64_dict_CB with character keys and binary values 
and fills base64_dict_BC with binary keys and character values
"""
x = 0
while x < 64:
    char = chars[x]
    base64_dict_CB[char] = '{0:06b}'.format(x)
    base64_dict_BC['{0:06b}'.format(x)] = char
    x += 1 

"""
(remove later)
for x in base64_dict_CB: #prints key:value
    print(x + " : " + base64_dict_CB[x])
"""

