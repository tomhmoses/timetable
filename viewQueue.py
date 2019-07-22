import pickle

queueFilePath = "queue.pickle"

def main():
    while True:
        choice = getMenuChoice()
        if choice == 0:
            view()
        elif choice == 1:
            removeDuplicates()
        elif choice == 2:
            viewWithShortTitle()
        elif choice == 3:
            changeOnToTrue()
        elif choice == 4:
            duplicateFirst()
        elif choice == 5:
            removeFirst()
        elif choice == 6:
            viewWithInfo()
        elif choice == 7:
            changeEmail()

def getMenuChoice():
    choice = ""
    printMenu()
    menuItems = 8
    while choice not in range(menuItems):
        try:
            choice = int(input("Choice: "))
        except:
            None
        if choice not in range(menuItems):
            print("Invalid choice, try again...")
    return choice

def tester(input=None):
    if input: print (input)

def printMenu():
    menu = """\nView Queue Main menu:
    0. View queue normally
    1. Remove duplicates from the queue
    2. View with short title info
    3. Change on to True in shortTitle Boolean
    4. Duplicate first item
    5. Remove first item
    6. View All Queue info (-csv)
    7. Change email for a request\n"""
    print(menu)

def view():
    queue = loadPickle(queueFilePath)
    for count in range(len(queue)):
        print(str(count) + ". " + queue[count]["username"])
        print("'" + queue[count]["email"] + "'")
    print("\nLength: " + str(len(queue)))

def changeEmail():
    queue = loadPickle(queueFilePath)
    number = int(input("number: "))
    newEmail = input("new email: ")
    confirm = input("confirm email '" + newEmail + "' (Y/n): ").strip()
    if confirm == "Y":
        queue[number]["email"] = newEmail
        saveQueue(queue)
        print("changed")
    else:
        print("nothing changed")

def viewWithInfo():
    queue = loadPickle(queueFilePath)
    for count in range(len(queue)):
        print(str(count) + ". " + queue[count]["username"])
        print(" "*(len(str(count))+2) + "'" + queue[count]["email"] + "'")
        print(" "*(len(str(count))+2) + str(queue[count]["shortenTitle"]))
        print(" "*(len(str(count))+2) + "'" + str(queue[count]["customTitle"])+ "'")
    print("\nLength: " + str(len(queue)))

def viewWithShortTitle():
    queue = loadPickle(queueFilePath)
    for count in range(len(queue)):
        print(str(count) + ". " + queue[count]["username"])
        print("'" + queue[count]["email"] + "'")
        print(queue[count]["shortenTitle"])
    print("\nLength: " + str(len(queue)))

def changeOnToTrue():
    queue = loadPickle(queueFilePath)
    for count in range(len(queue)):
        if queue[count]["shortenTitle"] == "on":
            queue[count]["shortenTitle"] = True
    saveQueue(queue)


def removeDuplicates():
    queue = loadPickle(queueFilePath)
    newQueue = []
    for count in range(len(queue)):
        print(str(count) + ". " + queue[count]["username"])
        print("'" + queue[count]["email"] + "'")
        if queue[count]["email"].upper() not in str(newQueue).upper():
            newQueue.append(queue[count])
    print(len(queue))
    print()

    for count in range(len(newQueue)):
        print(str(count) + ". " + newQueue[count]["username"])
        print("'" + newQueue[count]["email"] + "'")
    print(len(newQueue))

    saveQueue(newQueue)
    print("saved")

def removeFirst():
    queue = loadPickle(queueFilePath)
    newQueue = []
    for count in range(1, len(queue)):
        newQueue.append(queue[count])
    saveQueue(newQueue)

def duplicateFirst():
    queue = loadPickle(queueFilePath)
    newQueue = []
    newQueue.append(queue["username"])
    for count in range(len(queue)):
        newQueue.append(queue[count])
    saveQueue(newQueue)


def savePickle(file_name, obj):
    with open(file_name, 'wb') as fobj:
        pickle.dump(obj, fobj)

def loadPickle(file_name):
    with open(file_name, 'rb') as fobj:
        return pickle.load(fobj)

def saveQueue(queue):
    savePickle(queueFilePath,queue)


if __name__ == "__main__":
    main()