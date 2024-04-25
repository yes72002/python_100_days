# -----------------------------------------------------------------------------------
# File name  : main.py
# Source     : 100 Days of Code: day 85
# Author     : Jim Li
# Project    : Image Watermarking Desktop App
# Description: A Desktop program where you can upload images and add a watermark.
# -----------------------------------------------------------------------------------
# Revision History :
# Date       | Version | PIC    | Discription
# 2024.04.13 | 0       | Jim Li | Initial version
# -----------------------------------------------------------------------------------
# https://github.com/ousmall/Image_Watermarking_Desktop_App/blob/master/main.py
from tkinter import *
import ttkbootstrap as ttk
from tkinter import messagebox, filedialog
from PIL import Image, ImageDraw, ImageFont, ImageTk
import os

image_with_watermark = None
tk_image = None

def add_watermark(image_path, watermark_text, font_size=400):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)

    # use textbbox to get the size
    text_width, text_height = draw.textbbox((0, 0), watermark_text, font=font)[2:4]

    # set the watermark position
    x = (image.width - text_width) / 2
    y = (image.height - text_height) / 5 * 4

    draw.text((x, y), watermark_text, font=font, fill="#401F71")
    return image

def update_canvas_with_thumbnail(watermarked_image, display_canvas, canvas_photo):
    global tk_image
    thumbnail_size = (300, 450)
    watermarked_image.thumbnail(thumbnail_size)
    tk_image = ImageTk.PhotoImage(watermarked_image)
    display_canvas.itemconfig(canvas_photo, image=tk_image)
    return tk_image

def convert_image():
    global image_with_watermark, tk_image
    file_path = path_textbox.get()
    watermark_text = watermark_entry.get()
    if file_path and watermark_text:
        image_with_watermark = add_watermark(file_path, watermark_text)
        if image_with_watermark:
            tk_image = update_canvas_with_thumbnail(image_with_watermark, canvas, canvas_image)
            canvas.itemconfig(canvas_image, image=tk_image)
        else:
            messagebox.showerror('Error', 'Failed to add watermark.')
    else:
        messagebox.showerror('Error', 'Please provide both an image file and a watermark text.')

def save_image():
    global canvas_image
    if image_with_watermark:
        if image_with_watermark:
            original_file_path = path_textbox.get()
            # Get original file name without extension
            original_file_name = os.path.splitext(os.path.basename(original_file_path))[0]
            file_types = [('JPEG / JPG Files', '*.jpg'),
                          ('PNG Files', '*.png'), ('GIF Files', '*.gif'),
                          ('BMP Files', '*.bmp')]

            # Create a new filename and change the extension to .jpg
            save_path = filedialog.asksaveasfilename(defaultextension='.jpg',
                                                     filetypes=file_types,
                                                     initialfile=f"{original_file_name}_watermarked")
            # Check if file path is selected
            if save_path:
                try:
                    image_with_watermark.save(save_path)
                    messagebox.showinfo('Success', 'Image has been saved successfully.')
                    path_textbox.delete(0, END)
                    watermark_entry.delete(0, END)
                    canvas.itemconfig(canvas_image, image=default_image_tk)

                except Exception as e:
                    messagebox.showerror('Error', f'Failed to save image: {e}')
            else:
                messagebox.showerror('Error', 'No file selected.')
        else:
            messagebox.showerror('Error', 'No image to save. Please add a watermark first.')

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        path_textbox.delete(0, END)
        path_textbox.insert(0, file_path)


root = ttk.Window()
style = ttk.Style("pulse")
root.config(padx=50, pady=50)
root.title('Image Watermark App')

frame = Frame(root)
frame.grid(column=1, row=1, rowspan=5)
frame.config(padx=20)

canvas = Canvas(frame, width=300, height=450, bg='#492E87')
canvas.grid(column=1, row=1, rowspan=5)

default_image = Image.open("default_image.png")
default_image.thumbnail((300, 450))
default_image_tk = ImageTk.PhotoImage(default_image)
canvas_image = canvas.create_image(0, 0, anchor=NW, image=default_image_tk)

path_label = Label(root, text="Please Select Your Image:")
path_label.grid(column=2, row=1, sticky=W + S)

path_textbox = Entry(root, width=30)
path_textbox.grid(column=2, row=2)

select_button = Button(root, text='Select File', command=select_image)
select_button.grid(column=3, row=2)

watermark_label = Label(root, text="Watermark Text:")
watermark_label.grid(column=2, row=3, sticky=W + S)

watermark_entry = Entry(root, width=30)
watermark_entry.grid(column=2, row=4)

convert_button = Button(root, text='  Convert  ', command=convert_image)
convert_button.grid(column=3, row=4, padx=10)

save_button = Button(root, text='Download', command=save_image)
save_button.grid(column=2, row=5)

root.mainloop()