import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from script import polygon_to_he

def run_conversion():
    zip_path = filedialog.askopenfilename(
        title="Select Polygon ZIP File",
        filetypes=[("ZIP files", "*.zip")]
    )
    if not zip_path:
        return

    target_dir = filedialog.askdirectory(
        title="Select Folder to Save Output"
    )
    if not target_dir:
        return

    zip_path = Path(zip_path)
    target_dir = Path(target_dir)

    try:
        polygon_to_he(zip_path, target_dir)
        messagebox.showinfo("Success", f"Conversion completed!\n\nSaved in: {target_dir}")
    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")

def main():
    root = tk.Tk()
    root.title("Polygon to HackerEarth Converter")

    root.geometry("400x200")
    root.resizable(False, False)

    title = tk.Label(root, text="Polygon → HackerEarth", font=("Helvetica", 16))
    title.pack(pady=20)

    convert_button = tk.Button(root, text="Select ZIP and Convert", command=run_conversion, font=("Helvetica", 12))
    convert_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()