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


#todo: implement Decoding function



if __name__== '__main__':
    go= True
    while go: #main loop
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        option= input('Please enter an option:')
        if option== '1': #encoder
            pw= input("Please enter your password to encode:")
            encoded_password= encode(pw)
            print('Your password has been encoded and stored!')
        if option=='2': #decoder
             #decoding stuff
        if option=="3": #quit function
            quit()