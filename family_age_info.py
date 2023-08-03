import tkinter as tk
from tkinter import messagebox


def family_age_info():
    family_members = []
    warning_shown = False

    def add_family_member():
        nonlocal family_members, warning_shown
        name = name_entry.get()
        age = age_entry.get()
        if name and age:
            age = int(age)
            family_members.append({'name': name, 'age': age})
            name_entry.delete(0, tk.END)
            age_entry.delete(0, tk.END)
            update_family_info()
            if len(family_members) == 5:
                add_button.config(state=tk.DISABLED)
                submit_button.config(state=tk.NORMAL)
                if not warning_shown:
                    messagebox.showwarning("Warning", "Only five inputs allowed.")
                    warning_shown = True
        else:
            messagebox.showwarning("Error", "Please enter both name and age.")

    def update_family_info():
        nonlocal family_members
        family_listbox.delete(0, tk.END)
        for member in family_members:
            family_listbox.insert(tk.END, f"{member['name']}: {member['age']} years")

    def calculate_age_stats():
        nonlocal family_members
        if len(family_members) < 5:
            messagebox.showwarning("Error", "Please enter all 5 family members' information.")
            return

        sum_of_ages = sum(member['age'] for member in family_members)
        average_age = sum_of_ages / len(family_members)

        sum_label.config(text=f"Sum of Ages: {sum_of_ages}")
        average_label.config(text=f"Average Age: {average_age:.2f}")

        if average_age > 60:
            message_label.config(text="The family is mature.")
        else:
            message_label.config(text="It's young.")

    def reset_inputs():
        nonlocal family_members, warning_shown
        family_members.clear()
        add_button.config(state=tk.NORMAL)
        submit_button.config(state=tk.DISABLED)
        family_listbox.delete(0, tk.END)
        sum_label.config(text="Sum of Ages: ")
        average_label.config(text="Average Age: ")
        message_label.config(text="")
        warning_shown = False

    # Create the main window
    root = tk.Tk()
    root.title("Family Age Information")

    # Set window background color and font
    root.configure(bg="#f7f7f7")
    root.option_add("*Font", "Helvetica 10")

    # Create and place widgets
    name_label = tk.Label(root, text="Name:", bg="#f7f7f7")
    name_label.grid(row=0, column=0, padx=5, pady=5)
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    age_label = tk.Label(root, text="Age:", bg="#f7f7f7")
    age_label.grid(row=0, column=2, padx=5, pady=5)
    age_entry = tk.Entry(root)
    age_entry.grid(row=0, column=3, padx=5, pady=5)

    add_button = tk.Button(root, text="Add", command=add_family_member, bg="#4CAF50", fg="white")
    add_button.grid(row=0, column=4, padx=5, pady=5)

    family_listbox = tk.Listbox(root, width=30, height=10, bg="#ffffff", bd=0, highlightthickness=0)
    family_listbox.grid(row=1, column=0, columnspan=5, padx=5, pady=5)

    submit_button = tk.Button(root, text="Submit", command=calculate_age_stats, bg="#2196F3", fg="white",
                              state=tk.DISABLED)
    submit_button.grid(row=2, column=0, columnspan=5, padx=5, pady=5)

    sum_label = tk.Label(root, text="Sum of Ages: ", bg="#f7f7f7")
    sum_label.grid(row=3, column=0, columnspan=5, padx=5, pady=5)

    average_label = tk.Label(root, text="Average Age: ", bg="#f7f7f7")
    average_label.grid(row=4, column=0, columnspan=5, padx=5, pady=5)

    message_label = tk.Label(root, text="", bg="#f7f7f7")
    message_label.grid(row=5, column=0, columnspan=5, padx=5, pady=5)

    reset_button = tk.Button(root, text="Reset", command=reset_inputs, bg="#f44336", fg="white")
    reset_button.grid(row=6, column=0, columnspan=5, padx=5, pady=5)

    # Run the main loop
    root.mainloop()


# Call the function to display the GUI and collect family age information
family_age_info()
