import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser

import os


class Ui(tk.Tk):
    width = 800
    height = 600
    title = "Untitled - Notepad"
    file = None
    text_changed = False
    font_family = "Arial"
    font_size = 12
    font_style = "normal"