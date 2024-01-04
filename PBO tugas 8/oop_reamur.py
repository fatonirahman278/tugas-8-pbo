from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W,E,N,S

class FrmSuhu:
    def __init__(self, parent, title):
        self.parent = parent       
     
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, bg='dark green')
        mainFrame.grid(row=0, column=0, padx=10, pady=10, sticky=N+S+E+W)

        Label(mainFrame, text='Konversi Suhu', font=('Helvetica', 16, 'bold'), bg='lightgray').grid(row=0, column=1, columnspan=2, pady=10)

        # pasang Label
        Label(mainFrame, text='Reamur:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        
        # pasang textbox
        self.txtReamur = Entry(mainFrame,bg='lightgreen',font=('Helvetica', 12)) 
        self.txtReamur.grid(row=1, column=1, padx=5, pady=5,sticky=W+E)  
        self.txtCelcius = Entry(mainFrame,bg='pink') 
        self.txtCelcius .grid(row=3, column=1, padx=5, pady=5,sticky=W+E) 
        self.txtFahrenheit = Entry(mainFrame,bg='orange',font=('Helvetica', 12)) 
        self.txtFahrenheit .grid(row=4, column=1, padx=5, pady=5,sticky=W+E)
        self.txtKelvin = Entry(mainFrame,bg='lightyellow',font=('Helvetica', 12)) 
        self.txtKelvin .grid(row=5, column=1, padx=5, pady=5,sticky=W+E) 

        # Pasang Button
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung,bg='white',font=('heltiva',12,'bold'))
        self.btnHitung.grid(row=2, column=1, padx=5, pady=5)
        
           
    # fungsi "onHitung" berfungsi untuk menghitung luas persegi panjang  
    def onHitung(self):
        R = int(self.txtReamur.get())
        value_C = (R/0.8)
        self.txtCelcius.delete(0,END)
        self.txtCelcius.insert(END,str(value_C))
        value_F = (R * 2.25) + 32
        self.txtFahrenheit.delete(0,END)
        self.txtFahrenheit.insert(END,str(value_F))
        value_K = (R/0.8) + 273,15
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
