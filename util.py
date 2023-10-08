import os
import pickle
import tkinter as tk
from tkinter import messagebox
import face_recognition
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import Messagebox
# my_style=ttk.Style()
# my_style.configure('primary.TButton',font=('Helvetica bold', 20))
def get_button(window, text, color, command, fg='black'):
    button = ttk.Button(
        window,
        text=text,
        bootstyle=color,
        command=command,
        width=35,
    )
    return button

def get_img_label(window):
    label = ttk.Label(window)
    label.grid(row=0, column=0)
    return label

def get_text_label(window, text):
    label = ttk.Label(window, text=text)
    label.config(font=("sans-serif", 12), justify="left")
    return label

def get_entry_text(window):
    name = ttk.Text(window,height=0.5, width=20,font=("sans-serif", 12))
    return name

def msg_box(title, description):
    Messagebox.show_info(description, title)

def recognize(img, db_path):
    # it is assumed there will be at most 1 match in the db
    embeddings_unknown = face_recognition.face_encodings(img)
    if len(embeddings_unknown) == 0:
        return 'no_persons_found'
    else:
        embeddings_unknown = embeddings_unknown[0]

    db_dir = sorted(os.listdir(db_path))

    match = False
    j = 0
    while not match and j < len(db_dir):
        path_ = os.path.join(db_path, db_dir[j])

        file = open(path_, 'rb')
        embeddings = pickle.load(file)

        match = face_recognition.compare_faces(
            [embeddings], embeddings_unknown)[0]
        j += 1

    if match:
        return db_dir[j - 1][:-7]
    else:
        return 'unknown_person'
