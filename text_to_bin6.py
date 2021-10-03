import base64dict

"""
text_to_bin6(text_msg) consults the charater-binary dictionary to translate text_msg  
into a 6-bit binary string
"""


def text_to_bin6(text_msg):
    bin6_msg = "" 
    for char in text_msg:
        bin6_msg = bin6_msg + base64dict.base64_dict_CB[char]
    return bin6_msg 