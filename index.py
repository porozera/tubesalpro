from cProfile import label
from tkinter import *
from turtle import back


def star_main_page():
    def start_game(args):
        main_window.destroy()
        if args == 1:
            from options import hewan
            hewan.main()
        if args == 2:
            from options import kota
            kota.main()
        if args == 3:
            from options import makanan
            makanan.main()
        if args == 4:
            from options import barang
            barang.main()
    

    def option():
        lab_image1 = Button(
            main_window,
            text='Pilih kategori',
            border=0,
            justify='center',
            font=("Arial",12)
        )
        sel_btn1 = Button(
            text='Hewan',
            width=18,
            borderwidth=8,
            font=("",18),
            cursor="hand2",
            command=lambda: start_game(1),
        )

        sel_btn2 = Button(
            text='Kota',
            width=18,
            borderwidth=8,
            font=("",18),
            cursor="hand2",
            command=lambda: start_game(2),
        )

        sel_btn3 = Button(
            text='Makanan',
            width=18,
            borderwidth=8,
            font=("",18),
            cursor="hand2",
            command=lambda: start_game(3),
        )

        sel_btn4 = Button(
            text='Barang',
            width=18,
            borderwidth=8,
            font=("",18),
            cursor="hand2",
            command=lambda: start_game(4),
        )

        lab_image1.grid(row=0, column=0, padx= 20)
        sel_btn1.grid(row=0, column=4,pady= (10,0), padx= 50)
        sel_btn2.grid(row=1, column=4,pady= (10,0), padx= 50)
        sel_btn3.grid(row=2, column=4,pady= (10,0), padx= 50)
        sel_btn4.grid(row=3, column=4,pady= (10,0), padx= 50)
    
    def show_option():
        start_btn.destroy()
        lab_img.destroy ()
        option()
    
    main_window = Tk()
    main_window.geometry('500x300')
    main_window.resizable(0,0)
    main_window.title("GAME TEBAK KATA")
    main_window.configure(background="#C0C0C0")

    

    lab_img = Label(
        main_window,
        text="Game Tebak Kata",
        bg="#C0C0C0",
        font=("Courier",28)
    )
    lab_img.pack(pady=(50,0))

    start_btn = Button(
        main_window,
        text="Start",
        width=18,
        borderwidth=8,
        font=("",13),
        cursor="hand2",
        command=show_option,
    )
    start_btn.pack(pady=(50,20))

    main_window.mainloop()

star_main_page()
