from googletrans import Translator

translator = Translator()

while True:
    try:
        text = input("Enter a string :")

        conv_lang = input("which language would you like to translate :")

        trans = translator.translate(text, dest=conv_lang)
        print(trans.text)
    except :
        print("invalid Entry")

    quest = input("Do You Want To Continue....??? : ")
    if quest == 'y' or quest == 'yes':
        print(" ")
    else:
        print("******𝐄𝐱𝐢𝐭𝐞𝐝******")
        break