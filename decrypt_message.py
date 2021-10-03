import base64dict
import bitwise_xor
import bin6_to_text
import text_to_bin6

"""
decrypt_message(msg,otp) handles the method calls required for decrypting the message
"""

def decrypt_message(msg,otp):
        
        #Translating message text into 6-bit binary 
        bin_msg = text_to_bin6.text_to_bin6(msg)
        bin_otp = text_to_bin6.text_to_bin6(otp)

        #Preforming bitwise xor on the two binary strings
        decrypted_bin_msg = bitwise_xor.bitwise_xor(bin_msg,bin_otp)
        
        #Translating 6-bit binary into message text
        decrypted_msg = bin6_to_text.bin6_to_text(decrypted_bin_msg)
        
        #Return encrypted message to user 
        return decrypted_msg


