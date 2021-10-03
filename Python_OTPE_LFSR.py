import encrypt_message
import decrypt_message

def encrypt_decyrpt(msg,otp, encrypt, decrypt):
    if(encrypt):
        print("Message encrypted as: " + encrypt_message.encrypt_message(msg,otp))
    if(decrypt):
        print("Message decrypted as: " + decrypt_message.decrypt_message(msg,otp))

def printMenu():
    print(" ------------------------------ ")
    print("|  What would you like to do?  |")
    print("| 1 - Encrypt a message.       |")
    print("| 2 - Decrypt a message.       |")
    print("| 3 - Generate a key.          |")
    print("| 4 - Quit.                    |")
    print(" ------------------------------ ")

loop = True
while(loop): #program loop 
    
    printMenu()
    selection = int(input())

    if selection==1:
        user_message = input("Enter message to be encrypted: ")
        one_time_pad = input("Enter one-time pad: ") #generate with LFSR later 
        if len(user_message) == len(one_time_pad):
            encrypt_decyrpt(user_message,one_time_pad,encrypt=True,decrypt=False)
        else:
            print("Error: Message and pad must be of the same length.")

    elif selection==2:
        user_message = input("Enter message to be decrypted: ")
        one_time_pad = input("Enter one-time pad: ") #generate with LFSR later 
        if len(user_message) == len(one_time_pad):
            encrypt_decyrpt(user_message,one_time_pad,encrypt=False,decrypt=True)
        else:
            print("Error: Message and pad must be of the same length.")

    elif selection==3:
        print("Not implemented yet!")

    elif selection==4:
        loop = False
        print("Exiting application...")

    else:
        print("Error: Avaiable Options are 1,2,3 or 4. Please try again.")