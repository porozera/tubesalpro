from cgitb import text
from tkinter import *
from random import *
from tkinter import messagebox
import time

from setuptools import Command

food_answer = ['BATAGOR','BUBUR','PIZZA','ROTI','SATE','BAKSO','MARTABAK','OMELETE','SEBLAK',
            'CIMOL','CIRENG','NASTAR','KASTENGEL','BAKWAN','TEMPE','TAHU','STEAK','RAMEN','BASRENG',
            'KEBAB','SUSHI','SIOMAY','BURGER','SOTO','BIHUN','RENDANG','PANGSIT','MAKARONI','PECEL',
            'KWETIAU','DOCLANG','KETOPRAK','OPOR','KERIPIK','PAPEDA','GEMBLONG','LUMPIA','RISOL',
            'KENTANG','SOSIS','KARAGE','WAFFLE','NASI','DONAT','CILOR','DIMSUM']

food_word = ['AORBATG','RBUUB','ZIAPZ','TROI','TSAE','SKOAB','KBRMTAAA','EMTOELE','LBESKA',
            'ICOLM','NGRICE','RTASAN','SETLNEGKA','NWAAKB','PMETE','HTAU','EAKST','NERMA','RBAENGS',
            'BKBEA','ISSHU','MYAOSI','RGREBU','TSOO','NHIUB','ANRDNGE','STINGPA','KRAANINOM','CLPEE',
            'TWKIAEU','GNALDCO','OTPEAKKR','RPOO','PRIIKEK','PPAEDA','BEOLNMGG','MLPIUA','SLOIR',
            'GNTANKE','SSISO','GRKAAE','FLFEWA','SINA','NDAOT','LOCIR','SMMUDI']

ran_num = randrange(0, (len(food_word)))
jumbled_rand_word = food_word[ran_num]

points = 0

def main():
    def back():
        my_window.destroy()
        import index
        index.star_main_page()
    
    def changes ():
        global ran_num
        ran_num = randrange(0, (len(food_word)))
        word.configure(text=food_word[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def check():
        global points, ran_num
        user_word = get_input.get().upper()
        
        try:
            while user_word != food_answer[ran_num]:
                raise ValueError
            else:
                points += 5
                score.configure(text="Score: " + str(points))
                ran_num = randrange(0,(len(food_word)))
                word.configure(text=food_word[ran_num])
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
            ans_lab.configure(text=food_answer[ran_num])
        else:
            ans_lab.configure(text="Point anda tidak cukup")



    my_window = Tk()
    my_window.geometry("500x500")
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
