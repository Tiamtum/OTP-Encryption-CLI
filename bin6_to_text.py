import base64dict

"""
bin6_to_text(bin_msg) parses bin_msg into segments of length 6, then
consults the binary-character dictionary to translate the segment into a letter
or symbol charater
Note: Can possibly be scaled to any bit width at a latter date
"""

def bin6_to_text(bin_msg):
    text_msg = ""
    segment = 0
    n=0
    while segment < len(bin_msg)/6: 
        sub_string = ""
        for x in range(6*n,6*n+6): 
            sub_string = sub_string + bin_msg[x] 
        text_msg = text_msg + base64dict.base64_dict_BC[sub_string]
        segment += 1
        n += 1
    return text_msg
