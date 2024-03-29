
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

window =Tk()






#____________________________Account Password____________________________________#
# acc_owner = False
# def account_passord(acc_password):
#     if acc_password == "011001":
#         acc_owner = True
#

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project

# acc_owner = False
# def account_password(acc_password):
#     if acc_password == "011001":
#         acc_owner = True
#         return acc_owner
#     else:
#         return False





def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols =[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers =[choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    #Join the passwords in the lists
    password = "".join(password_list)

    #insert the password into the input session:
    password_entry.insert(0, password)

    #Automatically copy the password into the clipboard:
    pyperclip.copy(password)






# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    password_acc_data = password_account_entry.get()
    real_password = "0000"

    #Create a dictionary to use later for the json file:
    new_data={website:{
        "email": email,
        "password": password,
    }}

    if password_acc_data != real_password:
        messagebox.showinfo(title="error", message="Wrong password")
    else:

        if "@" not in email:
            messagebox.showinfo(title="oops", message=" Please input a valid email!")


        if len(website) == 0 or len(password) == 0 or len(email) == 0:
            messagebox.showinfo(title="oops", message= " Please make sure you haven't left any fields empty!")


        else:
            #create and write to the json file
            try:
                with open("data.json","r") as data_file:
                    #Read old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                   json.dump(new_data, data_file, indent= 4)

            else:
                data.update(new_data)
                with open("data.json", "w") as data_file:
                    json.dump(data, data_file, indent=4)

            finally:
                #This will delete the information a user type once we click Add so we can add another details:
                website_entry.delete(0, END)
                password_entry.delete(0, END)

#----------------------------Find Password-------------------------------#
def find_password():
   website = website_entry.get()
   password_acc_data= password_account_entry.get()
   real_password = "0000"

   try:
       with open("data.json") as data_file:
           data = json.load(data_file)
   except FileNotFoundError:
       messagebox.showinfo(title="error", message="No data file not found")
   else:
       if password_acc_data != real_password:
        messagebox.showinfo(title="error", message="Wrong password")

       else:

        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")

        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exist")


# ---------------------------- UI SETUP ------------------------------- #


window.title("Password Manager")
# window.minsize(width=500, height=200)
window.config(padx= 50, pady= 50)


canvas = Canvas(width=200, height= 200)
locked_img = PhotoImage(file = "logo.png" )
canvas.create_image(100,100, image =locked_img)
canvas.grid(row=0,column=1)


#Labels
password_account= Label(text="Account Password")
password_account.grid(row=1, column=0)



website_label = Label(text="Website:")
website_label.grid(row=2, column= 0)

email_label =Label(text="Email/Username:")
email_label.grid(row=3,column=0)

password_label = Label(text="Password:")
password_label.grid(row=4, column=0)

#Entry
website_entry = Entry(width=21)
website_entry.focus() #This will put our cursor in the webiste input session when the program launch
website_entry.grid(row= 2, column = 1)

email_entry = Entry(width=35)
email_entry.grid(row= 3, column = 1,columnspan=2)
email_entry.insert(0,"example@email.com")

password_entry = Entry(width=21)
password_entry.grid(row= 4, column = 1)

password_account_entry = Entry(width = 21)
password_account_entry.grid(row=1,column= 1)

#Buttons
generate_password= Button(text= "Generate password", command= generate_password)
generate_password.grid(row=3 ,column=2)

add_password = Button(text= "Add", width= 36, command = save)
add_password.grid(row=5, column= 1,columnspan=2)

search_buttom = Button(text="Search", width=13, command = find_password)
search_buttom.grid(row=2,column=2)


window.mainloop()
