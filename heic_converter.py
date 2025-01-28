import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
from PIL import Image
import pillow_heif  # Use pillow-heif for HEIC support

# Register HEIF format with Pillow
pillow_heif.register_heif_opener()

# Function to convert a single HEIC file to JPG
def convert_heic_to_jpg(heic_path, output_dir):
    image = Image.open(heic_path)
    jpg_path = os.path.join(output_dir, os.path.basename(heic_path).replace(".heic", ".jpg"))
    image.save(jpg_path, "JPEG")
    return jpg_path

# Function to handle bulk conversion
def bulk_convert_heic_to_jpg():
    heic_files = filedialog.askopenfilenames(
        title="Select HEIC Files", filetypes=[("HEIC files", "*.heic")], multiple=True
    )
    if not heic_files:
        messagebox.showwarning("Warning", "No HEIC files selected.")
        return

    output_dir = filedialog.askdirectory(title="Select Output Directory")
    if not output_dir:
        messagebox.showwarning("Warning", "No output directory selected.")
        return

    converted_files = []
    for heic_file in heic_files:
        try:
            jpg_path = convert_heic_to_jpg(heic_file, output_dir)
            converted_files.append(jpg_path)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to convert {heic_file}: {str(e)}")

    messagebox.showinfo("Conversion Complete", f"Converted {len(converted_files)} files to JPG.")

# GUI Setup
def main():
    root = tk.Tk()
    root.title("Bulk HEIC to JPG Converter")

    # Set window size and style
    root.geometry("400x300")
    root.configure(bg="#f0f4f8")

    # Style configuration
    style = ttk.Style()
    style.configure("TButton", font=("Segoe UI", 12), padding=10)
    style.map("TButton", background=[("active", "#3498db")], foreground=[("active", "white")])
    style.configure("TFrame", background="#f0f4f8")
    
    frame = ttk.Frame(root, padding=20, style="TFrame")
    frame.pack(expand=True)

    label = ttk.Label(frame, text="HEIC to JPG Converter", font=("Segoe UI", 16), background="#f0f4f8", foreground="#333")
    label.pack(pady=(0, 20))

    convert_button = ttk.Button(frame, text="Select HEIC Files and Convert", command=bulk_convert_heic_to_jpg)
    convert_button.pack(pady=20)

    exit_button = ttk.Button(frame, text="Exit", command=root.quit)
    exit_button.pack()

    # Run the application
    root.mainloop()

if __name__ == "__main__":
    main()
