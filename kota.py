from cgitb import text
from tkinter import *
from random import *
from tkinter import messagebox
import time

city_answer = ['BOGOR','BANDUNG','JAKARTA','PALEMBANG','YOGYAKARTA','BEKASI','DEPOK','BANJARMASIN',
            'SURABAYA','SERANG','BANJAR','DENPASAR','BENGKULU','GORONTALO','JAMBI','BELU','CILEGON',
            'CIMAHI','CIREBON','SUKABUMI','TASIKMALAYA','BANJAR','MAGELANG','PEKALONGAN','TEGAL','SEMARANG',
            'LAMPUNG','MAGELANG','SOLOK','SOLO','SURAKARTA','BATU','BLITAR','PATI','KEDIRI','MADIUN',
            'MAKASSAR','MOJOKERTO','PASURUAN','SURABAYA','BATAM','BALIKPAPAN','BANJARMASIN','PONTIANAK',
            'AMBON','BIMA','MATARAM','KUPANG']

city_word = ['OOGRB','ADNUNGB','TARJKAA','APMGNBELA','YKYAROATAG','KEBAIS','PEOKD','RAJBSNIMNAA',
            'BARYAASU','NGRESA','JBANAR','ARNAESPD','KNBUGLEU','AOONORTLG','MBIJA','LBEU','LGEICON',
            'IMAICH','ORBEICN','MUKAUBSI','AITMAAKSAYL','RJANBA','LEAGNMAG','LAEGPNNAOK','GELAT','RNGAAESM',
            'MLPGNUA','GNLAAMEG','KLOOS','OOSL','ARSUAKTRA','TBAU','LTARBI','TPAI','DRIKEI','IDUNAM',
            'KSRSAAMA','KRMEJOTOO','RSAPUANU','AAARBUSY','MTAAB','IPBKAAPLAN','IBSNJAAANRM','INATAPONK',
            'BMAON','MIAB','RMTAAAM','PGAUKN']

ran_num = randrange(0, (len(city_word)))
jumbled_rand_word = city_word[ran_num]

points = 0

def main():
    def back():
        my_window.destroy()
        import index
        index.star_main_page()
    
    def changes ():
        global ran_num
        ran_num = randrange(0, (len(city_word)))
        word.configure(text=city_word[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")
    
    def check():
        global points, ran_num
        user_word = get_input.get().upper()
        try:
            if user_word == city_answer[ran_num]:
                points += 5
                score.configure(text="Score: " + str(points))
                messagebox.showinfo('Benar', "Jawaban Anda Benar!")
                ran_num = randrange(0,(len(city_word)))
                word.configure(text=city_word[ran_num])
                get_input.delete(0,END)
                ans_lab.configure(text="")
            else:
                raise ValueError
        except ValueError:
            messagebox.showerror("Salah","Jawaban Anda Salah")
            get_input.delete(0,END)
    
    def show_answer():
        global points
        if points>4:
            points -= 10
            score.configure(text='Score: ' + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=city_answer[ran_num])
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

