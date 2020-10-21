import tkinter as tk

def calcTakeHome(*args):
    #setting values to what the user enter
    Esubtotal = float(subtotal.get())
    EnonCashTips = float(nonCashTips.get())
    EcashTips = float(cashTips.get())
    print(subtotal)
    print(EnonCashTips)
    print(EcashTips)

    #calc vlaues to see what spilt of a night are
    tipsD = float(EnonCashTips) + float(EcashTips)
    busboyD = float(Esubtotal)*0.01
    credittipsD = float(EnonCashTips)*0.04
    if(userinput.get() == 'Habachi'):
        chef = float(Esubtotal) * 0.07
        chef = round(chef, 2)
    else:
        chef = 0

    minustipsD = credittipsD + busboyD + chef
    totaltakeD = tipsD - minustipsD
    print('total to bus boys is ' + str(busboyD))
    totalToBusBoy.set(busboyD)
    print('total to chefs is ' + str(chef))
    totalToChef.set(chef)
    print('total to the credit card fee is ' + str(credittipsD))
    totalCreditCardFee.set(credittipsD)
    print('total tips you get today are ' + str(totaltakeD))
    totalTipsYouGet.set(totaltakeD)
    print('total take out of tips ' + str(minustipsD))
    totalTake.set(minustipsD)

root = tk.Tk()
root.title("Take home tips")

#Subtotal entry labels and feild
subtotalLabelQuestion = tk.Label(root, text='please type in your subtotal:')
subtotalLabelQuestion.grid(row=0, column=0)
subtotal = tk.StringVar()
subtotal_entry = tk.Entry(root, width=7, textvariable=subtotal)
subtotal_entry.grid(row=0, column=1)
subtotalLabel = tk.Label(root, text='$')
subtotalLabel.grid(row=0, column=2)

#Subtotal entry labels and feild
nonCashTipsQuestion = tk.Label(root, text='please type in your tips excluding cash tips:')
nonCashTipsQuestion.grid(row=1, column=0)
nonCashTips = tk.StringVar()
nonCashTips_entry = tk.Entry(root, width=7, textvariable=nonCashTips)
nonCashTips_entry.grid(row=1, column=1)
nonCashTipsLabel = tk.Label(root, text='$')
nonCashTipsLabel.grid(row=1, column=2)

#Subtotal entry labels and feild
cashTipsQuestion = tk.Label(root, text='please type in your cashtips:')
cashTipsQuestion.grid(row=2, column=0)
cashTips = tk.StringVar()
cashTips_entry = tk.Entry(root, width=7, textvariable=cashTips)
cashTips_entry.grid(row=2, column=1)
cashTipsLabel = tk.Label(root, text='$')
cashTipsLabel.grid(row=2, column=2)

#Subtotal entry labels and feild
subtotalLabelQuestion = tk.Label(root, text='Were you Habachi or Dine in')
subtotalLabelQuestion.grid(row=3, column=0)
userinput = tk.StringVar()
userinput.set("Dine in") # initial value
option = tk.OptionMenu(root, userinput, "Dine in", "Habachi")
option.grid(row=3, column=1)

startButton = tk.Button(root, text="Calculate", command=calcTakeHome)
startButton.grid(column=0, row=4)

totalToBusBoy = tk.StringVar()
tk.Label(root, textvariable=totalToBusBoy).grid(column=1, row=5,)
tk.Label(root, text="Total to bus boy:").grid(column=0, row=5,)

totalToChef = tk.StringVar()
tk.Label(root, textvariable=totalToChef).grid(column=1, row=6,)
tk.Label(root, text="Total to Chef:").grid(column=0, row=6,)

totalCreditCardFee = tk.StringVar()
tk.Label(root, textvariable=totalCreditCardFee).grid(column=1, row=7,)
tk.Label(root, text="Credit Card Fee:").grid(column=0, row=7,)

totalTipsYouGet = tk.StringVar()
tk.Label(root, textvariable=totalTipsYouGet).grid(column=1, row=8,)
tk.Label(root, text="Tips you get:").grid(column=0, row=8,)

totalTake = tk.StringVar()
tk.Label(root, textvariable=totalTake).grid(column=1, row=9,)
tk.Label(root, text="Total Take Home:").grid(column=0, row=9,)

root.mainloop()