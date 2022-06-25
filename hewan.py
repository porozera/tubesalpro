from cgitb import text
from tkinter import *
from random import *
from tkinter import messagebox
import time

animals_answer = ['AYAM','IKAN','KATAK','SINGA','BEBEK','KUCING','GAJAH','HARIMAU','JERAPAH','HIU',
                'PAUS','ZEBRA','JAGUAR','MACAN','ELANG','ANOA','RUSA','SEMUT','KELINCI','ANJING',
                'BABI','BERUANG','KUDANIL','MERAK','UNTA','BELALANG','GURITA','KAMBING','DOMBA',
                'PANDA','SIMPANSE','MONYET','ORANGUTAN','LANDAK','RAKUN','TIKUS','ULAR','KADAL',
                'KANGGURU','TRENGGILING','KOMODO','TAPIR']

animals_word = ['MYAMA','NKAI','TKAKA','IGASN','KBEEB','CIKGNU','HAGJA','URMHAAI','RPAHJEA','IHU',
                'SAPU','BERAZ','UGAJRA','AANCM','ALGEN','NAOA','SRAU','EUSMT','CILKNIE','GJAINN',
                'IABB','RNBAUGE','IKNUADL','MKERA','TNUA','NLGLABEA','GTUIAR','BMGANIK','BMDOA',
                'NDAPA','PMISNAES','EYMOTN','TONARANGU','LDAANK','KNURA','KTIUS','RLAU','DLAKA',
                'GGRKAUUN','ENILGIRGTNG','ODMOOK','RPTAI']

ran_num = randrange(0, (len(animals_word)))
jumbled_rand_word = animals_word[ran_num]

points = 0

    
def main():
    def back():
        my_window.destroy()
        import index
        index.star_main_page()
    
    def changes ():
        global ran_num
        ran_num = randrange(0, (len(animals_word)))
        word.configure(text=animals_word[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")
    
    def check():
        global points, ran_num
        user_word = get_input.get().upper()
        
        try:
            while user_word != animals_answer[ran_num]:
                raise ValueError
            else:
                points += 5
                score.configure(text="Score: " + str(points))
                ran_num = randrange(0,(len(animals_word)))
                word.configure(text=animals_word[ran_num])
                get_input.delete(0,END)
                ans_lab.configure(text="")
                messagebox.showinfo('Benar', "Jawaban Anda Benar!")
        except ValueError:
            messagebox.showerror("Salah","Jawaban Anda Salah")
            get_input.delete(0,END)
    
    def show_answer():
        global points
        if points>4:
            points -= 10
            score.configure(text='Score: ' + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=animals_answer[ran_num])
        else:
            ans_lab.configure(text="Point anda tidak cukup")
        

    my_window = Tk()
    my_window.geometry("600x500")
    my_window.resizable(0,0)
    my_window.title("Game Tebak Kata")
    my_window.configure(background="#C0C0C0")

            

    lab_img1 = Button(
        my_window,
        text="Back",
        bg="#C0C0C0",
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)
    

    score = Label(
        text= "Score:- 0",
        pady=10,
        bg="#C0C0C0",
        fg="#000000",
        font="Arial 14 bold",
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="#C0C0C0",
        fg="#000000",
        font="Arial 50 bold",
    )
    word.pack()

    get_input = Entry(
        font = "none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Cek Jawaban",
        width=18,
        borderwidth=8,
        font=("",13),
        bg="#C0C0C0",
        fg="#000000",
        command=check
    )
    submit.pack(pady=(10,20))

    change = Button(
        text= "Ganti Kata",
        width=18,
        borderwidth=8,
        font=("",13),
        bg="#C0C0C0",
        fg="#000000",
        command=changes,
    )
    change.pack()

    ans= Button(
        text="Spill Jawaban",
        width=18,
        borderwidth=8,
        font=("",13),
        bg="#C0C0C0",
        fg="#000000",
        command=show_answer,
    )
    ans.pack(pady=(20,10))

    ans_lab = Label(
        text="",
        bg="#C0C0C0",
        fg="#000000",
        font="Courier 15 bold"
    )
    ans_lab.pack()

    my_window.mainloop()

