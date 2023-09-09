from tkinter import *


tk = Tk()
tk.geometry("1534x773+0+0")
tk.title('FOOD BILLING SYSTEM')
tk.config(background='lime')


heading_frame = Frame(tk, bg="blue", bd=21, pady=5, relief=RIDGE)
heading_frame.grid(row=0)

heading = Label(heading_frame, text="------ FOOD BILLING SYSTEM -----", width=60, font=('ariel', 30, 'bold'), bd=21, bg='red', fg = 'yellow', justify=CENTER)
heading.grid(row=0)


Name=StringVar()
Phone_no=StringVar()
Bill_no=StringVar()


detail_frame = LabelFrame(tk, bg="blue", bd=10, pady=5, relief=SUNKEN, text=' customer details ', font=('ariel', 15, 'italic'), fg='pink', width=60)
detail_frame.grid(row=1)

name = Label(detail_frame, text="  Customer name:  ", width=16, font=('poppins', 15, 'italic'), bd=6, bg='skyblue', fg='navy', relief=RIDGE)
name.grid(row=1, column=1, padx= 15)
name_entry = Entry(detail_frame, width=20, font=('poppins', 15), justify=LEFT, textvariable=Name, relief=RIDGE, bd=6, bg='light pink')
name_entry.grid(row=1, column=2, padx=18)
ph_no = Label(detail_frame, text="  Phone no.  ", width=12, font=('poppins', 15, 'italic'), bd=6, bg='skyblue', fg='navy', relief=RIDGE)
ph_no.grid(row=1, column=3, padx=15)
ph_no_entry = Entry(detail_frame, width=15, font=('poppins', 15), justify=LEFT, textvariable=Phone_no, relief=RIDGE, bd=6, bg='light pink')
ph_no_entry.grid(row=1, column=4, padx=18)
bill_no = Label(detail_frame, text="  Bill no.  ", width=12, font=('poppins', 15, 'italic'), bd=6, bg='skyblue', fg='navy', justify=LEFT, relief=RIDGE)
bill_no.grid(row=1, column=5, padx=15)
bill_no_entry = Entry(detail_frame, width=15, font=('poppins', 15), justify=LEFT, textvariable=Bill_no, relief=RIDGE, bd=6, bg='light pink')
bill_no_entry.grid(row=1, column=6, padx=18)


def enter():
    global customer_name, customer_phone_number, customer_bill_number
    customer_name = Name.get()
    customer_phone_number = Phone_no.get()
    customer_bill_number = Bill_no.get()
    print(f"{customer_name} | {customer_phone_number} | {customer_bill_number}")

enter_details = Button(detail_frame, text=' -> Enter <- ', font=('jokerman,', 14, 'bold'), bg='yellow', fg='red', width=11, command=enter, relief=RIDGE, bd=6)
enter_details.grid(row=1,column=7, padx=21)


quantity_bathSoap = IntVar()
cost_bathSoap = 50
quantity_faceCream = IntVar()
cost_faceCream = 200
quantity_faceWash = IntVar()
cost_faceWash = 70
quantity_bodyLotion = IntVar()
cost_bodyLotion = 140
quantity_hairSpray = IntVar()
cost_hairSpray = 90


cosmetics_frame = LabelFrame(tk, bg="blue", bd=10, pady=5, relief=SUNKEN, text=' cosmetics ', font=('ariel', 15, 'italic'), fg='pink', width=60)
cosmetics_frame.place(x=0, y=240, relwidth=0.24)

bathSoap = Label(cosmetics_frame, text=" Bath soap (50/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
bathSoap.grid(row=1, column=1, padx= 10, pady=7)
bathSoap_entry = Entry(cosmetics_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_bathSoap, relief=RIDGE, bd=6, bg='light green')
bathSoap_entry.grid(row=1, column=2, padx=12, pady=7)
faceCream = Label(cosmetics_frame, text=" Face cream (200/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
faceCream.grid(row=2, column=1, padx= 10, pady=7)
faceCream_entry = Entry(cosmetics_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_faceCream, relief=RIDGE, bd=6, bg='light green')
faceCream_entry.grid(row=2, column=2, padx=12, pady=7)
faceWash = Label(cosmetics_frame, text=" Face Wash (70/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
faceWash.grid(row=3, column=1, padx= 10, pady=7)
faceWash_entry = Entry(cosmetics_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_faceWash, relief=RIDGE, bd=6, bg='light green')
faceWash_entry.grid(row=3, column=2, padx=12, pady=7)
bodyLotion = Label(cosmetics_frame, text=" Body Lotion (140/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
bodyLotion.grid(row=4, column=1, padx= 10, pady=7)
bodyLotion_entry = Entry(cosmetics_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_bodyLotion, relief=RIDGE, bd=6, bg='light green')
bodyLotion_entry.grid(row=4, column=2, padx=12,pady=7)
hairSpray = Label(cosmetics_frame, text=" Hair spray (90/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
hairSpray.grid(row=5, column=1, padx= 10, pady=7)
hairSpray_entry = Entry(cosmetics_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_hairSpray, relief=RIDGE, bd=6, bg='light green')
hairSpray_entry.grid(row=5, column=2, padx=12, pady=7)


quantity_rice = IntVar()
cost_rice = 400
quantity_foodOil = IntVar()
cost_foodOil = 200
quantity_daal = IntVar()
cost_daal = 150
quantity_wheat = IntVar()
cost_wheat = 500
quantity_sugar = IntVar()
cost_sugar = 80


grocery_frame = LabelFrame(tk, bg="blue", bd=10, pady=5, relief=SUNKEN, text=' grocery ', font=('ariel', 15, 'italic'), fg='pink', width=60)
grocery_frame.place(x=375, y=240, relwidth=0.24)

rice = Label(grocery_frame, text=" Rice: 5kg (400/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
rice.grid(row=1, column=1, padx= 10, pady=7)
rice_entry = Entry(grocery_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_rice, relief=RIDGE, bd=6, bg='light green')
rice_entry.grid(row=1, column=2, padx=12, pady=7)
foodOil = Label(grocery_frame, text=" Food oil: 1ltr (200/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
foodOil.grid(row=2, column=1, padx= 10, pady=7)
foodOil_entry = Entry(grocery_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_foodOil, relief=RIDGE, bd=6, bg='light green')
foodOil_entry.grid(row=2, column=2, padx=12, pady=7)
daal = Label(grocery_frame, text=" Daal: 1kg (150/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
daal.grid(row=3, column=1, padx= 10, pady=7)
daal_entry = Entry(grocery_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_daal, relief=RIDGE, bd=6, bg='light green')
daal_entry.grid(row=3, column=2, padx=12, pady=7)
wheat = Label(grocery_frame, text=" Wheat: 5kg (500/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
wheat.grid(row=4, column=1, padx= 10, pady=7)
wheat_entry = Entry(grocery_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_wheat, relief=RIDGE, bd=6, bg='light green')
wheat_entry.grid(row=4, column=2, padx=12,pady=7)
sugar = Label(grocery_frame, text=" Sugar: 1kg (80/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
sugar.grid(row=5, column=1, padx= 10, pady=7)
sugar_entry = Entry(grocery_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_sugar, relief=RIDGE, bd=6, bg='light green')
sugar_entry.grid(row=5, column=2, padx=12, pady=7)


quantity_maza = IntVar()
cost_maza = 75
quantity_coke = IntVar()
cost_coke = 100
quantity_frooti = IntVar()
cost_frooti = 70
quantity_chips = IntVar()
cost_chips = 80
quantity_biscuits = IntVar()
cost_biscuits = 60


others_frame = LabelFrame(tk, bg="blue", bd=10, pady=5, relief=SUNKEN, text=' other ', font=('ariel', 15, 'italic'), fg='pink', width=60)
others_frame.place(x=750, y=240, relwidth=0.24)

maza = Label(others_frame, text=" Maza: 500ml (75/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
maza.grid(row=1, column=1, padx= 10, pady=7)
maza_entry = Entry(others_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_maza, relief=RIDGE, bd=6, bg='light green')
maza_entry.grid(row=1, column=2, padx=12, pady=7)
coke = Label(others_frame, text=" Coke: 500ml (100/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
coke.grid(row=2, column=1, padx= 10, pady=7)
coke_entry = Entry(others_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_coke, relief=RIDGE, bd=6, bg='light green')
coke_entry.grid(row=2, column=2, padx=12, pady=7)
frooti = Label(others_frame, text=" Frooti: 500ml (70/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
frooti.grid(row=3, column=1, padx= 10, pady=7)
frooti_entry = Entry(others_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_frooti, relief=RIDGE, bd=6, bg='light green')
frooti_entry.grid(row=3, column=2, padx=12, pady=7)
chips = Label(others_frame, text=" Chips: 100gm (80/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
chips.grid(row=4, column=1, padx= 10, pady=7)
chips_entry = Entry(others_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_chips, relief=RIDGE, bd=6, bg='light green')
chips_entry.grid(row=4, column=2, padx=12,pady=7)
biscuits = Label(others_frame, text=" Biscuits: 5pcs (60/-) ", width=16, font=('poppins', 14, 'italic'), bd=7, bg='skyblue', fg='navy', relief=RIDGE)
biscuits.grid(row=5, column=1, padx= 10, pady=7)
biscuits_entry = Entry(others_frame, width=9, font=('poppins', 14), justify=LEFT, textvariable=quantity_biscuits, relief=RIDGE, bd=6, bg='light green')
biscuits_entry.grid(row=5, column=2, padx=12, pady=7)


billing_frame = LabelFrame(tk, bg="white", bd=10, pady=5, relief=RAISED, text=' bill ', font=('ariel', 15, 'italic'), fg='purple', width=60)
billing_frame.place(x=1125, y=240, relwidth=0.258, relheight=0.4)


billMenu_frame = LabelFrame(tk, bg="blue", bd=10, pady=5, relief=SUNKEN, text=' customer details ', font=('ariel', 15, 'italic'), fg='pink', width=60)
billMenu_frame.place(x=0, y=558, relwidth=0.992, relheight=0.27)


totalCosmetics = Label(billMenu_frame, text="Total cosmetics", width=15, font=('poppins', 14, 'italic'), bd=10, bg='skyblue', fg='navy', relief=RIDGE)
totalCosmetics.grid(row=1, column=1, padx= 15, pady=5)
totalCosmetics_value = Label(billMenu_frame, text=0, width=10, font=('poppins', 14, 'italic'), bd=10, bg='light pink', fg='black', relief=RIDGE)
totalCosmetics_value.grid(row=1, column=2, padx= 15, pady=5)
totalGrocery = Label(billMenu_frame, text="Total grocery", width=15, font=('poppins', 14, 'italic'), bd=10, bg='skyblue', fg='navy', relief=RIDGE)
totalGrocery.grid(row=2, column=1, padx=15, pady=5)
totalGrocery_value = Label(billMenu_frame, text=0, width=10, font=('poppins', 14, 'italic'), bd=10, bg='light pink', fg='black', relief=RIDGE)
totalGrocery_value.grid(row=2, column=2, padx= 15, pady=5)
totalOther = Label(billMenu_frame, text="Total other", width=15, font=('poppins', 14, 'italic'), bd=10, bg='skyblue', fg='navy', justify=LEFT, relief=RIDGE)
totalOther.grid(row=3, column=1, padx=15, pady=5)
totalOther_value = Label(billMenu_frame, text=0, width=10, font=('poppins', 14, 'italic'), bd=10, bg='light pink', fg='black', relief=RIDGE)
totalOther_value.grid(row=3, column=2, padx= 15, pady=5)

tax = 7.5

Cosmetics_tax = Label(billMenu_frame, text="Cosmetics tax", width=15, font=('poppins', 14, 'italic'), bd=10, bg='skyblue', fg='navy', relief=RIDGE)
Cosmetics_tax.grid(row=1, column=3, padx= 15, pady=5)
Cosmetics_tax_value = Label(billMenu_frame, text=0, width=10, font=('poppins', 14, 'italic'), bd=10, bg='light pink', fg='black', relief=RIDGE)
Cosmetics_tax_value.grid(row=1, column=4, padx= 15, pady=5)
Grocery_tax = Label(billMenu_frame, text="Grocery tax", width=15, font=('poppins', 14, 'italic'), bd=10, bg='skyblue', fg='navy', relief=RIDGE)
Grocery_tax.grid(row=2, column=3, padx=15, pady=5)
Grocery_tax_value = Label(billMenu_frame, text=0, width=10, font=('poppins', 14, 'italic'), bd=10, bg='light pink', fg='black', relief=RIDGE)
Grocery_tax_value.grid(row=2, column=4, padx= 15, pady=5)
Other_tax = Label(billMenu_frame, text="Other tax", width=15, font=('poppins', 14, 'italic'), bd=10, bg='skyblue', fg='navy', justify=LEFT, relief=RIDGE)
Other_tax.grid(row=3, column=3, padx=15, pady=5)
Other_tax_value = Label(billMenu_frame, text=0, width=10, font=('poppins', 14, 'italic'), bd=10, bg='light pink', fg='black', relief=RIDGE)
Other_tax_value.grid(row=3, column=4, padx= 15, pady=5)


def total():
    global cosmetics_amt, grocery_amt, others_amt, cosmetics_tax, grocery_tax, others_tax

    cosmetics_amt = (quantity_bathSoap.get()*cost_bathSoap)+(quantity_faceCream.get()*cost_faceCream)+(quantity_faceWash.get()*cost_faceWash)
    +(quantity_bodyLotion.get()*cost_bodyLotion)+(quantity_hairSpray.get()*cost_hairSpray)

    grocery_amt = (quantity_rice.get()*cost_rice)+(quantity_foodOil.get()*cost_foodOil)+(quantity_daal.get()*cost_daal)+(quantity_wheat.get()*cost_wheat)
    +(quantity_sugar.get()*cost_sugar)

    others_amt = (quantity_maza.get()*cost_maza)+(quantity_coke.get()*cost_coke)+(quantity_chips.get()*cost_chips)+(quantity_frooti.get()*cost_frooti)
    +(quantity_biscuits.get()*cost_biscuits)

    cosmetics_tax = cosmetics_amt*(tax/100)
    grocery_tax = grocery_amt*(tax/100)
    others_tax = others_amt*(tax/100)

    totalCosmetics_value.config(text=cosmetics_amt)
    totalGrocery_value.config(text=grocery_amt)
    totalOther_value.config(text=others_amt)

    Cosmetics_tax_value.config(text=cosmetics_tax)
    Grocery_tax_value.config(text=grocery_tax)
    Other_tax_value.config(text=others_tax)


scroll_y = Scrollbar(billing_frame, orient=VERTICAL)
scroll_y.pack(side=RIGHT, fill=Y)
txt = Text(billing_frame, yscrollcommand=scroll_y.set, font=('monaco', 9, 'bold'))
scroll_y.config(command=txt.yview)
txt.pack(fill=BOTH, expand=1)


def bill():
    try:
        txt.insert(END, '    <<<<<<<------- FOOD  BILLING ------->>>>>>>\n\n')
        txt.insert(END, f"  CUSTOMER NAME:    {customer_name}\n")
        txt.insert(END, f"  PHONE NO.:        {customer_phone_number}\n")
        txt.insert(END, f"  BILL NO.:         {customer_bill_number}\n\n")
        txt.insert(END, '  Product              Quantity         Price\n ------------------------------------------------\n')

        if quantity_bathSoap.get()!=0:
            txt.insert(END, f"  Bath soap               {quantity_bathSoap.get()}           Rs.{quantity_bathSoap.get()*cost_bathSoap}\n")
        if quantity_faceCream.get()!=0:
            txt.insert(END, f"  Face cream              {quantity_faceCream.get()}           Rs.{quantity_faceCream.get()*cost_faceCream}\n")
        if quantity_faceWash.get()!=0:
            txt.insert(END, f"  Face wash               {quantity_faceWash.get()}           Rs.{quantity_faceWash.get()*cost_faceWash}\n")
        if quantity_bodyLotion.get()!=0:
            txt.insert(END, f"  Body lotion             {quantity_bodyLotion.get()}           Rs.{quantity_bodyLotion.get()*cost_bodyLotion}\n")
        if quantity_hairSpray.get()!=0:
            txt.insert(END, f"  Hair spray              {quantity_hairSpray.get()}           Rs.{quantity_hairSpray.get()*cost_hairSpray}\n")

        if quantity_rice.get()!=0:
            txt.insert(END, f"  Rice                    {quantity_rice.get()}           Rs.{quantity_rice.get()*cost_rice}\n")
        if quantity_foodOil.get()!=0:
            txt.insert(END, f"  Food oil                {quantity_foodOil.get()}           Rs.{quantity_foodOil.get()*cost_foodOil}\n")
        if quantity_daal.get()!=0:
            txt.insert(END, f"  Daal                    {quantity_daal.get()}           Rs.{quantity_daal.get()*cost_daal}\n")
        if quantity_wheat.get()!=0:
            txt.insert(END, f"  Wheat                   {quantity_wheat.get()}           Rs.{quantity_wheat.get()*cost_wheat}\n")
        if quantity_sugar.get()!=0:
            txt.insert(END, f"  Sugar                   {quantity_sugar.get()}           Rs.{quantity_sugar.get()*cost_sugar}\n")

        if quantity_maza.get()!=0:
            txt.insert(END, f"  Maza                    {quantity_maza.get()}           Rs.{quantity_maza.get()*cost_maza}\n")
        if quantity_coke.get()!=0:
            txt.insert(END, f"  Coke                    {quantity_coke.get()}           Rs.{quantity_coke.get()*cost_coke}\n")
        if quantity_frooti.get()!=0:
            txt.insert(END, f"  Frooti                  {quantity_frooti.get()}           Rs.{quantity_frooti.get()*cost_frooti}\n")
        if quantity_chips.get()!=0:
            txt.insert(END, f"  Chips                   {quantity_chips.get()}           Rs.{quantity_chips.get()*cost_chips}\n")
        if quantity_biscuits.get()!=0:
            txt.insert(END, f"  Bicuits                 {quantity_biscuits.get()}           Rs.{quantity_biscuits.get()*cost_biscuits}\n")
            
        txt.insert(END, ' ------------------------------------------------\n')    
        txt.insert(END, f"  Total(inclusive of all taxes):  Rs.{cosmetics_amt+grocery_amt+others_amt+cosmetics_tax+grocery_tax+others_tax}\n")    
        txt.insert(END, ' ================================================\n')
    except:
        print('Provide more information to bill\n')
        txt.insert(END, '\n\n\t ERROR IN PROSSESING THE BILL\n\n\t\tCLEAR OR EXIT\n')
    finally:
        print('press clear to clear all values or exit to destroy the window\n\n')


def clear_bill():
    txt.delete('1.0',END)


def clear():
    clear_bill()

    name_entry.delete(0, END)
    ph_no_entry.delete(0, END)
    bill_no_entry.delete(0, END)

    quantity_bathSoap.set(0)
    quantity_faceCream.set(0)
    quantity_faceWash.set(0)
    quantity_bodyLotion.set(0)
    quantity_hairSpray.set(0)
    
    quantity_rice.set(0)
    quantity_foodOil.set(0)
    quantity_daal.set(0)
    quantity_wheat.set(0)
    quantity_sugar.set(0)

    quantity_maza.set(0)
    quantity_coke.set(0)
    quantity_frooti.set(0)
    quantity_chips.set(0)
    quantity_biscuits.set(0)

    totalCosmetics_value.config(text=0)
    totalGrocery_value.config(text=0)
    totalOther_value.config(text=0)

    Cosmetics_tax_value.config(text=0)
    Grocery_tax_value.config(text=0)
    Other_tax_value.config(text=0)


def exit():
    exitsure = Tk()
    exitsure.title('exit?')

    areyousure = Label(exitsure, text="Are you sure you want to exit?")
    areyousure.grid(column=0, row=0)

    def close_yes():
        exitsure.destroy()
        tk.destroy()
                
    def close_no():
        exitsure.destroy()

    ExitYes = Button(exitsure, text="Yes", command = close_yes)
    ExitYes.grid(column=0, row=2, padx=5, pady=5)

    ExitNo = Button(exitsure, text="No", command = close_no)
    ExitNo.grid(column=1, row=2, padx=5, pady=5)
    exitsure.mainloop()


total_button = Button(billMenu_frame, text='Total', font=('jokerman', 17), bg='yellow', fg='red', width=8, height=3, command=total, relief=RIDGE, bd=10)
total_button.grid(row=1, column= 5, padx = 17, pady=5, rowspan=3)
bill_button = Button(billMenu_frame, text='Generate Bill', font=('jokerman', 17), bg='yellow', fg='red', width=12, height=3, command=bill, relief=RIDGE, bd=10)
bill_button.grid(row=1, column= 6, padx = 17, pady=5, rowspan=3)
clear_button = Button(billMenu_frame, text='Clear', font=('jokerman', 17), bg='yellow', fg='red', width=7, height=3, command=clear, relief=RIDGE, bd=10)
clear_button.grid(row=1, column= 7, padx = 17, pady=5, rowspan=3)
exit_button = Button(billMenu_frame, text='Exit', font=('jokerman', 17), bg='yellow', fg='red', width=7, height=3, command=exit, relief=RIDGE, bd=10)
exit_button.grid(row=1, column= 8, padx = 17, pady=5, rowspan=3)


tk.mainloop()