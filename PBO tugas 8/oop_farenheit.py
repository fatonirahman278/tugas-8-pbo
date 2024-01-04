from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W,E,N,S

class FrmSuhu:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, bg='aquamarine')
        mainFrame.grid(row=0, column=0, padx=10, pady=10, sticky=N+S+E+W)

        Label(mainFrame, text='Konversi Suhu', font=('Helvetica', 16, 'bold'), bg='green').grid(row=0, column=1, columnspan=2, pady=10)


        # pasang Label
        Label(mainFrame, text='Fahrenheit:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        # pasang textbox
        self.txtFahrenheit = Entry(mainFrame, bg='yellow',font=('Helvetica', 12)) 
        self.txtFahrenheit.grid(row=1, column=1, padx=5, pady=5,sticky=W+E)  
        self.txtCelcius = Entry(mainFrame, bg='lightblue',font=('Helvetica', 12))
        self.txtCelcius .grid(row=3, column=1, padx=5, pady=5,sticky=W+E) 
        self.txtReamur = Entry(mainFrame, bg='lightgreen',font=('Helvetica', 12))
        self.txtReamur .grid(row=4, column=1, padx=5, pady=5,sticky=W+E)
        self.txtKelvin = Entry(mainFrame, bg='white',font=('Helvetica', 12))
        self.txtKelvin .grid(row=5, column=1, padx=5, pady=5,sticky=W+E) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung,bg='white',font=('heltiva',12,'bold'))
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self):
        F = int(self.txtFahrenheit.get())
        value_C = (F - 32) * (5/9)
        self.txtCelcius.delete(0,END)
        self.txtCelcius.insert(END,str(value_C))
        value_R = (4/9) * (F - 32)
        self.txtReamur.delete(0,END)
        self.txtReamur.insert(END,str(value_R))
        value_K = (F + 459.67) * (5/9)
        self.txtKelvin.delete(0, END)
        self.txtKelvin.insert(END,str(value_K))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
        
if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    root.config(bg='lightgray')
    aplikasi = FrmSuhu(root, "Program Konversi Suhu")
    root.mainloop() 