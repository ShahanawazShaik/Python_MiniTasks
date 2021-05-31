import pywhatkit as kit
from pywhatkit.main import info, playonyt, search
print("Welcome to The Fun choiceone:\n1.Play a song in Yotube\n2.Convert image into ASCII Representation/\n3.Text to Handwritten\n4.Google it\n5.Get Info\n6.What's app Someone")
choice = int(input())
if(choice == 1):
    a = input(str("Enter the song you wish to play in Youtube: "))
    kit.playonyt(a)
elif(choice == 2):
    kit.image_to_ascii_art(r"C:\Users\noush\Downloads\67586673.jpg",r"C:\Users\noush\OneDrive\Desktop\x.txt")
    print("Your Converted image has been Writen in path specified")
elif(choice == 3):
    text = input(str("Enter the text you want to Convert to Handwritting: "))
    try:
        kit.text_to_handwriting(text,r"C:\Users\noush\OneDrive\Desktop\x.png")
    except(FileNotFoundError,IOError):
        print("Specify the Correct Path")
elif(choice == 4):
    key = input(str("Enter the key you want to Google: "))
    kit.search(key)
elif(choice == 5):
    x = input(str("Type in What info you need?: "))
    kit.info(x)
elif(choice == 6):
    no = int(input("Enter the Number you would like to text: "))
    msg = str(input("Enter the Message: "))
    kit.sendwhatmsg(f"+91{no}",msg,14,3)
else:
    print("Invalid Option!")

