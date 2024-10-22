#author - Xiaolei Huang

def encode(password):
    encoded_password= ""
    for digit in password: #converts each digit on a char by char basis
        if digit== "7":
            encoded_password+= "0"
        elif digit== "8":
            encoded_password+="1"
        elif digit=="9":
            encoded_password+= "2"
        elif digit== "0":
            encoded_password+="3"
        elif digit=="1":
            encoded_password+= "4"
        elif digit== "2":
            encoded_password+="5"
        elif digit=="3":
            encoded_password+= "6"
        elif digit== "4":
            encoded_password+="7"
        elif digit=="5":
            encoded_password+= "8"
        elif digit== "6":
            encoded_password+= "9"
    return encoded_password

# Added by partner: Nicholas Cuc
def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        # Shift each digit back by 3
        decoded_password += str((int(digit) - 3) % 10)
    return decoded_password


if __name__== '__main__':
    """Comment by Nicholas: put whats under here in a main function like 
    def main():
        code
    Then whats ran is main() after if __name__== '__main__':
    """
    encoded_password = None
    go= True
    while go: #main loop
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        option= input('Please enter an option: ')
        if option== '1': #encoder
            pw= input("Please enter your password to encode: ")
            encoded_password= encode(pw)
            print('Your password has been encoded and stored!')
            print()
        if option=='2': #decoder
            if encoded_password is None:    # If no password encoded, tell user to enter a password to option 1
                print("No encoded password found. Please encode a password first.")
                print()
            else:   # Decodes password and prints out encoded password and original password
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
                print()
        if option=="3": #quit function
            quit()