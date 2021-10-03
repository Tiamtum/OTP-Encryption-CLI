
"""
bitwise_xor(bin_msg,bin_otp) preforms a make-shift xor operation
on the strings bin_msg and bin_otp and appends the result to 
encrypted_bin_msg.
Note: Passing two parameters is redundent, consider passing the length of one message instead
"""

def bitwise_xor(bin_msg,bin_otp):
    encrypted_bin_msg = ""
    for byte in range(0,len(bin_msg)): #since binMsg and binotp are the same size, the one we iterate through does not matter
        if bin_msg[byte] == bin_otp[byte]:
            encrypted_bin_msg = encrypted_bin_msg + "0"
        else:
            encrypted_bin_msg = encrypted_bin_msg + "1"
    return encrypted_bin_msg 
