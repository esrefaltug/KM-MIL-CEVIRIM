import tkinter
import tkinter.messagebox

class kiloConverterGUI:
            
    def __init__(self):

               
        
        self.pencerem=tkinter.Tk()

        self.topframe=tkinter.Frame(self.pencerem)
        self.bottomframe=tkinter.Frame(self.pencerem)

        self.label1=tkinter.Label(self.topframe,text="çevrilecek km:")
        self.kiloentry=tkinter.Entry(self.topframe,width=10)

        self.label1.pack(side='left')
        self.kiloentry.pack(side="left")

        self.calcbutton=tkinter.Button(self.bottomframe,text="Çevir",command=self.convert)

        self.cksbutton=tkinter.Button(self.bottomframe,text='çıkış',command=self.pencerem.destroy)

        self.calcbutton.pack(side='left')
        self.cksbutton.pack(side='left')

        self.topframe.pack()
        self.bottomframe.pack()


    def convert(self):
        kilo=float(self.kiloentry.get())
        miles=kilo*0.6214

        tkinter.messagebox.showinfo('Results',str(kilo)+'çevirim'+str(miles)+'miles.')

kiloConverterGUI()

  


    
