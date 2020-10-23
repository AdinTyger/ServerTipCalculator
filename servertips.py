import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.frame = tk.Frame(master)
        self.master.title("Take home tips")
        self.frame.pack()
        self.create_widgets(self.frame) 
    
    def start(self):
        pass

    def calcTakeHome(self, *args):
        #setting values to what the user enter
        local_subtotal = float(self.subtotal.get())
        local_nonCashTips = float(self.nonCashTips.get())
        local_cashtips = float(self.cashTips.get())
        print(local_subtotal)
        print(local_nonCashTips)
        print(local_cashtips)

        #calc vlaues to see what spilt of a night are
        tipsD = float(local_nonCashTips) + float(local_cashtips)
        busboyD = float(local_subtotal)*0.01
        credittipsD = float(local_nonCashTips)*0.04
        if(self.userinput.get() == 'Habachi'):
            chef = float(local_subtotal) * 0.07
            chef = round(chef, 2)
        else:
            chef = 0

        minustipsD = credittipsD + busboyD + chef
        totaltakeD = tipsD - minustipsD
        print('total to bus boys is ' + str(busboyD))
        self.totalToBusBoy.set(busboyD)
        print('total to chefs is ' + str(chef))
        self.totalToChef.set(chef)
        print('total to the credit card fee is ' + str(credittipsD))
        self.totalCreditCardFee.set(credittipsD)
        print('total tips you get today are ' + str(totaltakeD))
        self.totalTipsYouGet.set(totaltakeD)
        print('total take out of tips ' + str(minustipsD))
        self.totalTake.set(minustipsD)

    def create_widgets(self, Frame):
        #Subtotal entry labels and feild
        subtotalLabelQuestion = tk.Label(Frame, text='please type in your subtotal:')
        subtotalLabelQuestion.grid(row=0, column=0)
        self.subtotal = tk.StringVar()
        subtotal_entry = tk.Entry(Frame, width=7, textvariable=self.subtotal)
        subtotal_entry.grid(row=0, column=1)
        subtotalLabel = tk.Label(Frame, text='$')
        subtotalLabel.grid(row=0, column=2)

        #nonCashTips entry labels and feild
        nonCashTipsQuestion = tk.Label(Frame, text='please type in your tips excluding cash tips:')
        nonCashTipsQuestion.grid(row=1, column=0)
        self.nonCashTips = tk.StringVar()
        nonCashTips_entry = tk.Entry(Frame, width=7, textvariable=self.nonCashTips)
        nonCashTips_entry.grid(row=1, column=1)
        nonCashTipsLabel = tk.Label(Frame, text='$')
        nonCashTipsLabel.grid(row=1, column=2)

        #cashTips entry labels and feild
        cashTipsQuestion = tk.Label(Frame, text='please type in your cashtips:')
        cashTipsQuestion.grid(row=2, column=0)
        self.cashTips = tk.StringVar()
        cashTips_entry = tk.Entry(Frame, width=7, textvariable=self.cashTips)
        cashTips_entry.grid(row=2, column=1)
        cashTipsLabel = tk.Label(Frame, text='$')
        cashTipsLabel.grid(row=2, column=2)

        #Subtotal entry labels and feild
        userinputQuestion = tk.Label(Frame, text='Were you Habachi or Dine in')
        userinputQuestion.grid(row=3, column=0)
        self.userinput = tk.StringVar()
        self.userinput.set("Dine in") # initial value
        option = tk.OptionMenu(Frame, self.userinput, "Dine in", "Habachi")
        option.grid(row=3, column=1)
        

        startButton = tk.Button(Frame, text="Calculate", command=self.calcTakeHome)
        startButton.grid(column=0, row=4)

        self.totalToBusBoy = tk.StringVar()
        tk.Label(Frame, textvariable=self.totalToBusBoy).grid(column=1, row=5,)
        tk.Label(Frame, text="Total to bus boy:").grid(column=0, row=5,)

        self.totalToChef = tk.StringVar()
        tk.Label(Frame, textvariable=self.totalToChef).grid(column=1, row=6,)
        tk.Label(Frame, text="Total to Chef:").grid(column=0, row=6,)

        self.totalCreditCardFee = tk.StringVar()
        tk.Label(Frame, textvariable=self.totalCreditCardFee).grid(column=1, row=7,)
        tk.Label(Frame, text="Credit Card Fee:").grid(column=0, row=7,)

        self.totalTipsYouGet = tk.StringVar()
        tk.Label(Frame, textvariable=self.totalTipsYouGet).grid(column=1, row=8,)
        tk.Label(Frame, text="Tips you get:").grid(column=0, row=8,)

        self.totalTake = tk.StringVar()
        tk.Label(Frame, textvariable=self.totalTake).grid(column=1, row=9,)
        tk.Label(Frame, text="Total Take Home:").grid(column=0, row=9,)


root = tk.Tk()
app = Application(master=root)
app.mainloop()

