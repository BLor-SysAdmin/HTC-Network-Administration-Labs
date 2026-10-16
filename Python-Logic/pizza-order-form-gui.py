from tkinter import *
import random

def Closing():
    frmOrder.destroy()

def Reset():
    entCustomerName.delete(0,END)
    lblCustomerCopy["text"]=""
    pizzaSize.set("Small")
    extraCheese.set(0)
    sausage.set(0)
    pepperoni.set(0)
    lbxPayments.select_set(0)
    lblOrderNum["text"]=f"Order #: {random.randint(100,1000)}"
    lblPizzaPrice["text"]="Price/pizza = "
    lblToppingsPrice["text"]="Toppings price = "
    lblTax["text"]="MN Tax 10% = "
    lblTotalCost["text"]="Pizza Total = "
    entCustomerName.focus()

def Process():
    strCustomerName = entCustomerName.get()

    sizeCost={"Small":5,"Medium":10,"Large":15}
    toppingCost=1

    totalCost=sizeCost[pizzaSize.get()]
    toppingsCost=0
    if extraCheese.get():
        toppingsCost += toppingCost
    if sausage.get():
        toppingsCost += toppingCost
    if pepperoni.get():
        toppingsCost += toppingCost
    tax = (totalCost+toppingsCost) * 0.1
    totalCost += toppingsCost + tax

    lblPizzaPrice["text"]=f"Price/pizza = ${sizeCost[pizzaSize.get()]:.2f}"
    lblToppingsPrice["text"]=f"Toppings price = ${toppingsCost:.2f}"
    lblTax["text"]=f"MN Tax 10% = ${tax:.2f}"
    lblTotalCost["text"]=f"Pizza Total = ${totalCost:.2f}"

    lblCustomerCopy["text"]=(
        f"Customer: {strCustomerName}\n"
        f"Order Total: ${totalCost:.2f}\n"
        f"{lblOrderNum['text']}"
    )
    
frmOrder = Tk()
frmOrder.configure(width=800, height=600,bg="sky blue")
frmOrder.title("Best Pizza Ever Order Form (Owned by Blong Lor)")

lblCompanyName=Label(text="Best Pizza Ever!!",font="Arial 16 bold",bg = "sky blue",fg="navy")
lblCompanyName.place(x=300,y=20)
#Random Order Number
lblOrderNum = Label(text=f"Order #: {random.randint(100, 1000)}", font="Arial 14", bg="sky blue", fg="navy")
lblOrderNum.place(x=600,y=50)

lblCustomerName = Label(text="Customer Name:",font="Arial 14",bg = "sky blue",fg="navy")
lblCustomerName.place(x=100,y=50)

lblCustomerCopy = Label(text="",font="Arial 14 bold",bg="sky blue",fg="red")
lblCustomerCopy.place(x=260,y=300)
#Pizza Size
lblPizzaSize=Label(frmOrder,text="Pizza Size",font="Arial 14 bold",bg="sky blue",fg="navy")
lblPizzaSize.place(x=100,y=100)
pizzaSize = StringVar()
rbSmall=Radiobutton(frmOrder,text="Small",variable=pizzaSize, value="Small",font="Arial 14",bg="sky blue",fg="navy")
rbSmall.place(x=100,y=130)
rbMedium=Radiobutton(frmOrder, text="Medium", variable=pizzaSize,value="Medium", font="Arial 14", bg="sky blue", fg="navy")
rbMedium.place(x=100, y=160)
rbLarge=Radiobutton(frmOrder, text="Large", variable=pizzaSize,value="Large", font="Arial 14", bg="sky blue", fg="navy")
rbLarge.place(x=100, y=190)
pizzaSize.set("Small")
#Pizza Toppings
lblToppings=Label(frmOrder,text="Pizza Toppings",font="Arial 14 bold",bg="skyblue",fg="navy")
lblToppings.place(x=300,y=100)
extraCheese = IntVar()
sausage = IntVar()
pepperoni = IntVar()
cbExtraCheese=Checkbutton(frmOrder,text="Extra Cheese",variable=extraCheese,font="Arial 14",bg="sky blue",fg="navy")
cbExtraCheese.place(x=300,y=130)
cbSausage=Checkbutton(frmOrder, text="Sausage",variable=sausage, font="Arial 14", bg="sky blue", fg="navy")
cbSausage.place(x=300, y=160)
cbPepperoni=Checkbutton(frmOrder, text="Pepperoni",variable=pepperoni, font="Arial 14", bg="sky blue", fg="navy")
cbPepperoni.place(x=300, y=190)
#Payment Method
lblPayments=Label(frmOrder,text="Payment Method",font="Arial 14 bold",bg="sky blue",fg="navy")
lblPayments.place(x=500,y=100)
lbxPayments=Listbox(fg="navy",font="Arial 14 bold",height=5)
lbxPayments.place(x=500,y=130)
lbxPayments.insert(0,"Cash")
lbxPayments.insert(1, "Check")
lbxPayments.insert(2, "Visa")
lbxPayments.insert(3, "MasterCard")
lbxPayments.insert(4, "American Express")
lbxPayments.select_set(0)
#Price/pizza, MN Tax 10%, Pizza Total, and Toppings price
lblPizzaPrice=Label(frmOrder,text="Price/pizza = ",font="Arial 14",bg="sky blue",fg="navy")
lblPizzaPrice.place(x=100,y=400)
lblTax=Label(frmOrder, text="MN Tax 10% = ",font="Arial 14", bg="sky blue", fg="navy")
lblTax.place(x=100, y=430)
lblTotalCost=Label(frmOrder, text="Pizza Total = ",font="Arial 14", bg="sky blue", fg="navy")
lblTotalCost.place(x=100, y=460)
lblToppingsPrice=Label(frmOrder, text="Toppings price = ",font="Arial 14", bg="sky blue", fg="navy")
lblToppingsPrice.place(x=300, y=400)

entCustomerName = Entry(font="Arial 14",bg= "white",fg="navy",width=30)
entCustomerName.place(x=260,y=50)

btnClose = Button(text="Quit",font="Arial 14",bg = "sky blue",fg="navy",width=8, command=Closing)
btnClose.place(x=650,y=500)

btnReset = Button(text="Reset",font="Arial 14",bg = "sky blue",fg="navy",width=8, command=Reset)
btnReset.place(x=550,y=500)

btnProcess = Button(text="Process",font="Arial 14",bg = "sky blue",fg="navy",width=8, command=Process)
btnProcess.place(x=450,y=500)

frmOrder.mainloop()
