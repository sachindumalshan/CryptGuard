# import classes
import random
from tkinter import *

def clearEncryptField():
    preText_field.delete(0, END)
    encryptText_field.delete(0, END)
    encryptKeyCode_field.delete(0, END)

def clearDecryptField():
    postText_field.delete(0, END)
    decryptText_field.delete(0, END)
    decryptKeyCode_field.delete(0, END)


# Function to convert the normal text into encrypted text
def encryptTexttoCode():
    encryptText_field.delete(0, END)
    shiftPosition = random.randint(1, 26)
    encryptText = preText_field.get()

    unrecognizeLetterCount = 0
    for string in encryptText:
        if not string.isalpha():
            unrecognizeLetterCount = unrecognizeLetterCount + 1

    if (unrecognizeLetterCount != 0):
        print("Unrecognized Character was Detected!")
    else:
        encryptList = []
        for letter in encryptText:
            if (letter.isupper()):
                updateNumericValue = (ord(letter) - 64) + shiftPosition
                if (updateNumericValue > 26):
                    updateNumericValue = updateNumericValue % 26
                    convertValue = updateNumericValue + 64
                    encryptList.append(chr(convertValue))
                else:
                    convertValue = updateNumericValue + 64
                    encryptList.append(chr(convertValue))

            elif (letter.islower()):
                updateNumericValue = (ord(letter) - 96) + shiftPosition
                if (updateNumericValue > 26):
                    updateNumericValue = updateNumericValue % 26
                    convertValue = updateNumericValue + 96
                    encryptList.append(chr(convertValue))
                else:
                    convertValue = updateNumericValue + 96
                    encryptList.append(chr(convertValue))
            else:
                code = ["Unrecognized Character was detected!"]
                break

        encryptText = ''.join(encryptList)
        encryptText_field.insert(0,encryptText)

        if (len(encryptList) != 0):
            encryptKeyCode_field.delete(0, END)
            encryptKeyCode_field.insert(0, shiftPosition)

def decryptTexttoCode():
    decryptText_field.delete(0, END)
    decryptText = postText_field.get()
    keycodeStr = decryptKeyCode_field.get()

    numbers=[]
    for number in keycodeStr:
        numbers.insert(0,number)
    keycode = int(''.join(numbers))

    unrecognizeLetterCount = 0
    for string in decryptText:
        if not string.isalpha():
            unrecognizeLetterCount = unrecognizeLetterCount + 1

    if (unrecognizeLetterCount != 0):
        print("Unrecognized Character was Detected!")
    else:
        decryptList = []
        for letter in decryptText:
            if (letter.isupper()):
                updateNumericValue = (ord(letter) - 64) - keycode
                if (updateNumericValue < 1):
                    updateNumericValue = updateNumericValue + 26
                    convertValue = updateNumericValue + 64
                    decryptList.append(chr(convertValue))
                else:
                    convertValue = updateNumericValue + 64
                    decryptList.append(chr(convertValue))

            elif (letter.islower()):
                updateNumericValue = (ord(letter) - 96) - keycode
                if (updateNumericValue < 1):
                    updateNumericValue = updateNumericValue + 26
                    convertValue = updateNumericValue + 96
                    decryptList.append(chr(convertValue))
                else:
                    convertValue = updateNumericValue + 96
                    decryptList.append(chr(convertValue))
            else:
                code = ["Unrecognized Character was detected!"]
                break

        decryptText = ''.join(decryptList)
        decryptText_field.insert(0,decryptText)



if __name__ == "__main__":
    # Create a GUI window
    root = Tk()

    w = 500  # width
    h = 670  # height

    # Get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()

    # Calculate x and y coordinates
    x = (ws / 2) - (w / 2)
    y = (hs / 2) - (h / 2)

    # set the dimensions of the screen and where it is placed
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    # set the name of tkinter GUI window
    root.title("CryptGuard")

    # CryptGuard Logo Card
    logo_card = Frame(root, bg='lightgray', padx=10, pady=10)
    logo_card.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # CryptGuard Logo
    originalPhoto = PhotoImage(file=r"C:\Users\ASUS\Desktop\CryptGuard\key.png")
    resized_photo = originalPhoto.subsample(15, 15)  # You can adjust the subsample factor as needed
    cryptguard = Label(root, text="CryptGuard", image=resized_photo, compound="top", fg='black', font=("Lato", 15, "bold"), justify="center")
    cryptguard.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    # Create a frame for the encrypt fields
    encryptCard = Frame(root, bd=1, relief="solid", padx=10, pady=10)
    encryptCard.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    # Encryption Title
    encryptHeader = Label(encryptCard, text="Encryption", fg='gray', font=("Lato", 12, "italic"))
    encryptHeader.grid(row=0, column=0, padx=10, pady=10)

    # Text to Encrypt section
    preText = Label(encryptCard, text="Text to Encrypt", fg='black', font=("Lato", 12, "bold"))
    preText.grid(row=1, column=0, padx=10, pady=10)

    preText_field = Entry(encryptCard, font=("Lato", 12))
    preText_field.grid(row=1, column=1, padx=10, pady=10)

    # Encrypted Text
    encryptText = Label(encryptCard, text="Encrypted Text", fg='black', font=("Lato", 12, "bold"))
    encryptText.grid(row=2, column=0, padx=10, pady=10)

    encryptText_field = Entry(encryptCard, font=("Lato", 12))
    encryptText_field.grid(row=2, column=1, padx=10, pady=10)

    # Key Code
    encryptKeyCode = Label(encryptCard, text="Key Code", fg='black', font=("Lato", 12, "bold"))
    encryptKeyCode.grid(row=3, column=0, padx=10, pady=10)

    encryptKeyCode_field = Entry(encryptCard, font=("Lato", 12))
    encryptKeyCode_field.grid(row=3, column=1, padx=10, pady=10)

    # Create a submit button to encrypt the text
    encryptButton = Button(encryptCard, height=4, width=8, text="Encrypt", fg="black", font=("Lato", 12, "bold"), command=encryptTexttoCode)
    encryptButton.grid(row=1, rowspan=2, column=2, pady=10, padx=10)

    # Create a submit button to clear the encrypt fields
    clearEncrypt = Button(encryptCard, height=1, width=8, text="Clear", fg="black", font=("Lato", 12, "bold"), command=clearEncryptField)
    clearEncrypt.grid(row=3, column=2, pady=10, padx=10)



    # Create a frame for the decrypt fields
    decryptCard = Frame(root, bd=1, relief="solid", padx=10, pady=10)
    decryptCard.grid(row=3, column=0, columnspan=3, padx=10, pady=10, sticky="ew")

    # Decryption Title
    decryptHeader = Label(decryptCard, text="Decryption", fg='gray', font=("Lato", 12, "italic"))
    decryptHeader.grid(row=0, column=0, padx=10, pady=10)

    # Text to Decrypt section
    postText = Label(decryptCard, text="Text to Decrypt", fg='black', font=("Lato", 12, "bold"))
    postText.grid(row=1, column=0, padx=10, pady=10)

    postText_field = Entry(decryptCard, font=("Lato", 12))
    postText_field.grid(row=1, column=1, padx=10, pady=10)

    # Key Code
    decryptKeyCode = Label(decryptCard, text="Key Code", fg='black', font=("Lato", 12, "bold"))
    decryptKeyCode.grid(row=2, column=0, padx=10, pady=10)

    decryptKeyCode_field = Entry(decryptCard, font=("Lato", 12))
    decryptKeyCode_field.grid(row=2, column=1, padx=10, pady=10)


    # Decrypted Text
    decryptText = Label(decryptCard, text="Decrypted Text", fg='black', font=("Lato", 12, "bold"))
    decryptText.grid(row=3, column=0, padx=10, pady=10)

    decryptText_field = Entry(decryptCard, font=("Lato", 12))
    decryptText_field.grid(row=3, column=1, padx=10, pady=10)

    # Create a submit button to decrypt the text
    decryptButton = Button(decryptCard, height=4, width=8, text="Decrypt", fg="black", font=("Lato", 12, "bold"), command=decryptTexttoCode)
    decryptButton.grid(row=1, rowspan=2,column=2, pady=10, padx=10)

    # Create a submit button to clear the decrypt fields
    clearDecrypt = Button(decryptCard, height=1, width=8, text="Clear", fg="black", font=("Lato", 12, "bold"), command=clearDecryptField)
    clearDecrypt.grid(row=3, column=2, pady=10, padx=10)



    # Create a frame ownership
    ownership = Frame(root, padx=10, pady=10)
    ownership.grid(row=4, column=0, columnspan=3)

    # ownership with your name
    ownershipFooter = Label(ownership, text="© 2024 Sachindu Malshan | All rights reserved.", fg='black', font=("Lato", 12), justify="center")
    ownershipFooter.grid(row=1, column=0, columnspan=3)

    # Start the GUI
    root.mainloop()