from tkinter import Frame, Label,Entry,Button,Tk, W, E, N, S, messagebox

class FrmSuhu:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10, bg='black')
        mainFrame.grid(row=0, column=0, padx=10, pady=10, sticky=N+S+E+W)

        # Judul Program
        Label(mainFrame, text='Konversi Suhu', font=('Helvetica', 16, 'bold'), bg='green').grid(row=1, column=1, columnspan=2, pady=10)

        # Pasang Label dengan warna latar belakang
        Label(mainFrame, text='Celcius:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=5, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=6, column=0,
            sticky=W, padx=5, pady=5)
        
        # Pasang textbox dengan warna latar belakang
        self.txtCelcius = Entry(mainFrame, bg='lightblue', font=('Helvetica', 12))
        self.txtCelcius.grid(row=2, column=1, padx=5, pady=5, sticky=W+E)  
        self.txtFahrenheit = Entry(mainFrame, bg='lightgreen', font=('Helvetica', 12))
        self.txtFahrenheit.grid(row=4, column=1, padx=5, pady=5, sticky=W+E) 
        self.txtReamur = Entry(mainFrame, bg='lightyellow', font=('Helvetica', 12))
        self.txtReamur.grid(row=5, column=1, padx=5, pady=5, sticky=W+E)
        self.txtKelvin = Entry(mainFrame, bg='lightcoral', font=('Helvetica', 12))
        self.txtKelvin.grid(row=6, column=1, padx=5, pady=5, sticky=W+E) 

        # Pasang Button dengan warna latar belakang
        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung, bg='white', font=('Helvetica', 12, 'bold'))
        self.btnHitung.grid(row=3, column=1, padx=5, pady=5)

    # fungsi "onHitung" berfungsi untuk menghitung konversi suhu  
    def onHitung(self):
        try:
            C = float(self.txtCelcius.get())
            value_F = (9/5 * C) + 32
            self.txtFahrenheit.delete(0, 'end')
            self.txtFahrenheit.insert('end', f'{value_F:.2f}')
            value_R = (4/5 * C)
            self.txtReamur.delete(0, 'end')
            self.txtReamur.insert('end', f'{value_R:.2f}')
            value_K = C + 273.15
            self.txtKelvin.delete(0, 'end')
            self.txtKelvin.insert('end', f'{value_K:.2f}')
        except ValueError:
            messagebox.showerror('Error', 'Masukkan angka valid untuk suhu Celcius.')

    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()
    root.geometry("400x300")
    root.config(bg='lightgray')
    aplikasi = FrmSuhu(root, "Program Konversi Suhu")
    root.mainloop()