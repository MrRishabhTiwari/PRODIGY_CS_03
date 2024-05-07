import string
import tkinter as tk

def check_pwd():
    password = password_entry.get()
    strength = 0
    remarks = ''
    lower_count = upper_count = num_count = wspace_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count +=1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count +=1
        else:
            special_count +=1

    if lower_count >= 1:
        strength +=1
    if upper_count >= 1:
        strength +=1
    if num_count >= 1:
        strength +=1
    if wspace_count>=1:
        strength +=1
    if special_count>=1:
        strength +=1

    if strength == 1:
        remarks = "Very Bad Password!!! Change ASAP"
    elif strength == 2:
        remarks = "Not A Good Password!!! Change ASAP"
    elif strength ==3:
        remarks = "It's a weak password, consider changing"
    elif strength == 4:
        remarks = "It's a hard password, but can be better"
    elif strength == 5:
        remarks = "A very strong password"

    result_label.config(text=f"Your password has:\n{lower_count} lowercase characters\n{upper_count} uppercase characters\n{num_count} numeric characters\n{wspace_count} whitespace characters\n{special_count} special characters")
    strength_label.config(text=f"Password Strength: {strength}")
    remarks_label.config(text=f"Hint: {remarks}")

root = tk.Tk()
root.title("Password Checker")
root.geometry("500x300") # Set the size of the window

password_label = tk.Label(root, text="Password:")
password_label.pack()

password_entry = tk.Entry(root, font=("Helvetica", 24))  # Show password as asterisks by default
password_entry.pack(pady=20)

check_button = tk.Button(root, text="Check Password", command=check_pwd)
check_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack()

strength_label = tk.Label(root, text="")
strength_label.pack()

remarks_label = tk.Label(root, text="")
remarks_label.pack()

def toggle_show_password():
    if show_password_var.get():
        password_entry.config(show="")  # Show password as plain text
    else:
        password_entry.config(show="*")  # Show password as asterisks

show_password_var = tk.BooleanVar()
show_password_checkbutton = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_show_password)
show_password_checkbutton.pack(pady=10)

root.mainloop()
