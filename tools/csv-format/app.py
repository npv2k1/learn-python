import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_input_folder():
    input_folder = filedialog.askdirectory(title="Select Input Folder")
    input_folder_entry.delete(0, tk.END)
    input_folder_entry.insert(0, input_folder)

def convert_csv_to_excel():
    input_path = input_folder_entry.get()
    delimiter = delimiter_entry.get()

    if not input_path or not delimiter:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if not os.path.exists(input_path):
        messagebox.showerror("Error", "Input folder does not exist.")
        return

    if not os.path.isdir(input_path):
        messagebox.showerror("Error", "Input path must be a directory.")
        return

    output_path = input_path  # Use the same folder as input
    print(f"Input path: {input_path}")

    for filename in os.listdir(input_path):
        if filename.endswith('.csv'):
            print(f"Converting {filename}...")
            input_file = os.path.join(input_path, filename)
            df = pd.read_csv(input_file, delimiter=delimiter)
            output_file = os.path.splitext(filename)[0] + '.xlsx'
            df.to_excel(os.path.join(output_path, output_file), index=False)

    messagebox.showinfo("Conversion Complete", f"All CSV files in the folder have been converted to Excel.")

app = tk.Tk()
app.title("CSV to Excel Converter")

# Input folder
input_folder_label = tk.Label(app, text="Input Folder:")
input_folder_label.pack()
input_folder_entry = tk.Entry(app)
input_folder_entry.pack()
input_folder_button = tk.Button(app, text="Browse", command=browse_input_folder)
input_folder_button.pack()

# Delimiter
delimiter_label = tk.Label(app, text="Delimiter:")
delimiter_label.pack()
delimiter_entry = tk.Entry(app)
delimiter_entry.pack()

# Convert button
convert_button = tk.Button(app, text="Convert", command=convert_csv_to_excel)
convert_button.pack()

app.mainloop()
