import tkinter as tk
from tryout import Flu_info

root = tk.Tk()

tk.Label(root, text="Vaccine Name: ").grid(row=0)
tk.Label(root, text="Number of locations needed: (Optional)").grid(row=1)
tk.Label(root, text="Latitude of your location: (Optional)").grid(row=2)
tk.Label(root, text="Longitude of your location: (Optional)").grid(row=3)

textbox1 = tk.Entry(root)
textbox2 = tk.Entry(root)
textbox3 = tk.Entry(root)
textbox4 = tk.Entry(root)
textbox1.grid(row=0, column=1)
textbox2.grid(row=1, column=1)
textbox3.grid(row=2, column=1)
textbox4.grid(row=3, column=1)

button = tk.Button(
    root, text="Get Information", command=lambda: display_text()
)
clean_button = tk.Button(
    root, text="Clear Text Box", command=lambda: clean_up()
)

displaybox = tk.Text(root)

button.grid(row=4, columnspan=2)
clean_button.grid(row=5, columnspan=2)
displaybox.grid(row=6, columnspan=2)


def display_text():
    lab_info = Flu_info("Flu_Vaccines_Provider_NC.db")
    text1 = textbox1.get()
    text2 = textbox2.get()
    text3 = textbox3.get()
    text4 = textbox4.get()
    if len(text2) == 0:
        ll = lab_info.getLocationByVaccineName(text1)
        # ll = "a"
    elif len(text3) != 0 and len(text4) != 0:
        ll = lab_info.getInfoByPosition(text3, text4)
        # ll = "d"
    elif len(text3) != 0 or len(text4) != 0:
        ll = "Please enter the full location info!"
    else:
        ll = lab_info.getLimitedLocationByVaccineName(text1, int(text2))
        # ll = "b"
    displaybox.insert(tk.END, ll)


def clean_up():
    textbox1.delete(0, tk.END)
    textbox2.delete(0, tk.END)
    textbox3.delete(0, tk.END)
    textbox4.delete(0, tk.END)
    displaybox.delete("1.0", tk.END)


root.mainloop()
