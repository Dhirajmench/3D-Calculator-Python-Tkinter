# -*- coding: utf-8 -*-

from tkinter import Tk, END, Entry, N, E, S, W, Button, Label
from tkinter import font
from functools import partial


# ---------------- FUNCTIONS ---------------- #

def get_input(entry, argu):
    entry.insert(END, argu)


def backspace(entry):
    input_len = len(entry.get())
    if input_len > 0:
        entry.delete(input_len - 1, END)


def clear(entry):
    entry.delete(0, END)


def calc(entry):
    input_info = entry.get()

    try:
        output = str(eval(input_info.strip()))
    except ZeroDivisionError:
        popupmsg()
        output = ""
    except Exception:
        output = "Error"

    clear(entry)
    entry.insert(END, output)


def popupmsg():
    popup = Tk()
    popup.resizable(0, 0)
    popup.geometry("300x130")
    popup.title("Alert")
    popup.configure(bg="#1E293B")

    label = Label(
        popup,
        text="Cannot divide by 0!\nEnter valid values",
        fg="white",
        bg="#1E293B",
        font=("Arial", 11, "bold")
    )
    label.pack(side="top", fill="x", pady=15)

    B1 = Button(
        popup,
        text="Okay",
        bg="#FF8C00",
        fg="white",
        font=("Arial", 10, "bold"),
        relief="raised",
        borderwidth=4,
        padx=15,
        pady=5,
        command=popup.destroy
    )
    B1.pack()

    popup.mainloop()


# ---------------- CALCULATOR ---------------- #

def cal():

    root = Tk()

    root.title("3D Calculator")
    root.resizable(0, 0)

    # -------- BACKGROUND -------- #
    root.configure(bg="#111827")

    # -------- FONTS -------- #

    entry_font = font.Font(
        family="Arial",
        size=22,
        weight="bold"
    )

    button_font = font.Font(
        family="Arial",
        size=14,
        weight="bold"
    )

    # -------- DISPLAY -------- #

    entry = Entry(
        root,
        justify="right",
        font=entry_font,
        bg="#0F172A",
        fg="white",
        insertbackground="white",
        relief="sunken",
        borderwidth=6,
        width=20
    )

    entry.grid(
        row=0,
        column=0,
        columnspan=4,
        sticky=N + W + S + E,
        padx=10,
        pady=10,
        ipady=10
    )

    # -------- COLORS -------- #

    number_bg = "#374151"
    number_active = "#4B5563"

    operator_bg = "#F97316"
    operator_active = "#FB923C"

    special_bg = "#D1D5DB"
    special_active = "#E5E7EB"

    quit_bg = "#020617"
    quit_active = "#1E293B"

    text_white = "#FFFFFF"
    text_black = "#111827"

    # -------- 3D BUTTON CREATOR -------- #

    def number_button(text, command):

        return Button(
            root,
            text=text,
            command=command,
            font=button_font,
            fg=text_white,
            bg=number_bg,
            activebackground=number_active,
            activeforeground="white",

            # 3D EFFECT
            relief="raised",
            borderwidth=5,

            padx=15,
            pady=10
        )

    def operator_button(text, command):

        return Button(
            root,
            text=text,
            command=command,
            font=button_font,
            fg=text_white,
            bg=operator_bg,
            activebackground=operator_active,
            activeforeground="white",

            # 3D EFFECT
            relief="raised",
            borderwidth=5,

            padx=15,
            pady=10
        )

    def special_button(text, command):

        return Button(
            root,
            text=text,
            command=command,
            font=button_font,
            fg=text_black,
            bg=special_bg,
            activebackground=special_active,
            activeforeground=text_black,

            # 3D EFFECT
            relief="raised",
            borderwidth=5,

            padx=15,
            pady=10
        )

    # ---------------- ROW 1 ---------------- #

    button15 = special_button(
        "<-",
        lambda: backspace(entry)
    )

    button15.grid(
        row=1,
        column=0,
        columnspan=2,
        padx=5,
        pady=5,
        sticky=N + S + E + W
    )


    button16 = special_button(
        "C",
        lambda: clear(entry)
    )

    button16.grid(
        row=1,
        column=2,
        padx=5,
        pady=5
    )


    button14 = operator_button(
        "/",
        lambda: get_input(entry, "/")
    )

    button14.grid(
        row=1,
        column=3,
        padx=5,
        pady=5
    )

    # ---------------- ROW 2 ---------------- #

    button7 = number_button(
        "7",
        lambda: get_input(entry, "7")
    )

    button7.grid(
        row=2,
        column=0,
        padx=5,
        pady=5
    )


    button8 = number_button(
        "8",
        lambda: get_input(entry, "8")
    )

    button8.grid(
        row=2,
        column=1,
        padx=5,
        pady=5
    )


    button9 = number_button(
        "9",
        lambda: get_input(entry, "9")
    )

    button9.grid(
        row=2,
        column=2,
        padx=5,
        pady=5
    )


    button12 = operator_button(
        "*",
        lambda: get_input(entry, "*")
    )

    button12.grid(
        row=2,
        column=3,
        padx=5,
        pady=5
    )

    # ---------------- ROW 3 ---------------- #

    button4 = number_button(
        "4",
        lambda: get_input(entry, "4")
    )

    button4.grid(
        row=3,
        column=0,
        padx=5,
        pady=5
    )


    button5 = number_button(
        "5",
        lambda: get_input(entry, "5")
    )

    button5.grid(
        row=3,
        column=1,
        padx=5,
        pady=5
    )


    button6 = number_button(
        "6",
        lambda: get_input(entry, "6")
    )

    button6.grid(
        row=3,
        column=2,
        padx=5,
        pady=5
    )


    button11 = operator_button(
        "-",
        lambda: get_input(entry, "-")
    )

    button11.grid(
        row=3,
        column=3,
        padx=5,
        pady=5
    )

    # ---------------- ROW 4 ---------------- #

    button1 = number_button(
        "1",
        lambda: get_input(entry, "1")
    )

    button1.grid(
        row=4,
        column=0,
        padx=5,
        pady=5
    )


    button2 = number_button(
        "2",
        lambda: get_input(entry, "2")
    )

    button2.grid(
        row=4,
        column=1,
        padx=5,
        pady=5
    )


    button3 = number_button(
        "3",
        lambda: get_input(entry, "3")
    )

    button3.grid(
        row=4,
        column=2,
        padx=5,
        pady=5
    )


    button10 = operator_button(
        "+",
        lambda: get_input(entry, "+")
    )

    button10.grid(
        row=4,
        column=3,
        padx=5,
        pady=5
    )

    # ---------------- ROW 5 ---------------- #

    button0 = number_button(
        "0",
        lambda: get_input(entry, "0")
    )

    button0.grid(
        row=5,
        column=0,
        padx=5,
        pady=5
    )


    button13 = number_button(
        ".",
        lambda: get_input(entry, ".")
    )

    button13.grid(
        row=5,
        column=1,
        padx=5,
        pady=5
    )


    button18 = operator_button(
        "^",
        lambda: get_input(entry, "**")
    )

    button18.grid(
        row=5,
        column=2,
        padx=5,
        pady=5
    )


    button17 = operator_button(
        "=",
        lambda: calc(entry)
    )

    button17.grid(
        row=5,
        column=3,
        padx=5,
        pady=5
    )

    # ---------------- QUIT BUTTON ---------------- #

    exit_button = Button(
        root,
        text="Quit",
        fg="white",
        bg=quit_bg,
        activebackground=quit_active,
        activeforeground="white",

        font=("Arial", 11, "bold"),

        relief="raised",
        borderwidth=5,

        height=1,
        width=10,

        command=root.quit
    )

    exit_button.grid(
        row=6,
        column=0,
        columnspan=4,
        pady=10
    )

    # -------- START APPLICATION -------- #

    root.mainloop()


# ---------------- MAIN ---------------- #

if __name__ == "__main__":
    cal()
