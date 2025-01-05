# Jai Shree Ram

from assets.img.banner import banner


def welcome():
    print(banner)
    print("""as it says, "slow worm"
note: make sure you have required permission to run the tool (it's dangerous!)\n\nJai Shree Ram\n""")

def createBlankLine():
    print("\n")


def mainMenu():
    
    def printOptList():
        print("1. Slow Worm")
        print("2. Web Server Crasher")
        print("3. Firewall Maker")
        print("4. CLI")
        print("5. Exit")



    createBlankLine()
    choice = input("Enter your choice: ")
    if choice == "1":
        print("Starting...")
    elif choice == "2":
        print("Stopping...")
        exit()
    else:
        print("Invalid choice! Try again.\n")
        mainMenu()


welcome()
mainMenu()