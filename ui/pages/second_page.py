import tkinter as tkinter

import customtkinter as tk

import ui.widgets as w
from ui.constants import constants
from ui.routing import Routes


def second_page():
    this_page = Routes.second_page

    title = tk.CTkLabel(this_page, text="Second Page")
    title.pack()

    button = tk.CTkButton(
        this_page,
        text="Go to page 1",
        command=lambda: Routes.go_to(Routes.welcome_page),
    )
    button.pack()
