# contacts={}
def add_contact():
    name=input("What name do you want to add?").lower()
    if name in contacts:
        return ("Contact already exists. ")
        # contacts[name]
    if name not in contacts:
        phone_num=(input("Enter your Phone Number: "))
        email=input("Enter your email")
        contacts[name]={"phone": phone_num,"email": email}
        return "Your contact is saved"
contacts={}
# print(add_contact())

def search_contact():
    name=input("What name do you want to Search?").lower()
    if name in contacts:
        print("-"*30)
        print("Name:", name)
        print("Phone",contacts[name]["phone"])
        print("Email" ,contacts[name]["email"])
        print("-"*30)
    else:
        print("Sorry Not Found")
        
    
# print(search_contact())
def del_contact():
    name=input("What name do you want to delete? ").lower()
    if name in contacts:
        del contacts[name]
        return "Deleted Successfully"
    else:
        return "Contact not found"
def show_contact():
    if not contacts:
        print("No contacts found")
    for name in sorted(contacts):
        print("-"*30)
        print("Name:", name)
        print("Phone",contacts[name]["phone"])
        print("Email" ,contacts[name]["email"])
        print("-"*30)
while True:
    choice = input("1)Add Contacts \n 2) Search Contact 3)Delete Contact 4)Show COntact 5)Exit")
    if choice=="1":
        print("-"*30)
        print(add_contact())
    elif choice=="2":
        print("-"*30)
        search_contact()
    elif choice=="3":
        print("-"*30)
        print(del_contact())
    elif choice=="4":
        print("-"*30)
        show_contact()
    elif choice=="5":
        break
    else:
        print("-"*30)
        print("Invalid Input")











