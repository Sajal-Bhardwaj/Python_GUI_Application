from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql

win=Tk()
win.geometry("900x640")
win.title("Admission Form")

s= ttk.Style()
s.configure("new.TFrame", background="orange")

tabs=ttk.Notebook(win)

tab1=ttk.Frame(tabs,style='new.TFrame')
tabs.add(tab1,text="AD")
tabs.pack(expan=1,fil="both")

#Personal Information
label_t=Label(tab1,text="Admission Form",font=("Times New Roman",18),bg="orange")
label_space=Label(tab1,text="        ",bg="orange")
label_pi=Label(tab1,text="Personal Information",font=("Times New Roman",16),bg="orange")
label_space1=Label(tab1,text="        ",font=("Times New Roman",14),bg="orange")
label1=Label(tab1,text="First Name",font=("Times New Roman",14),bg="orange")
label2=Label(tab1,text="Last Name",font=("Times New Roman",14),bg="orange")
label3=Label(tab1,text="Mother's Name",font=("Times New Roman",14),bg="orange")
label4=Label(tab1,text="Father's Name",font=("Times New Roman",14),bg="orange")
label5=Label(tab1,text="Local Guardian's",font=("Times New Roman",14),bg="orange")
label6=Label(tab1,text="Date Of Birth",font=("Times New Roman",14),bg="orange")

entry1=Entry(tab1,font=("Times New Roman",14))
entry2=Entry(tab1,font=("Times New Roman",14))
entry3=Entry(tab1,font=("Times New Roman",14))
entry4=Entry(tab1,font=("Times New Roman",14))
entry5=Entry(tab1,font=("Times New Roman",14))
entry6=Entry(tab1,font=("Times New Roman",14))

label_t.grid(row=0,column=2)
label_space.grid(row=1,column=2)
label_pi.grid(row=2,column=0)
label_space1.grid(row=3,column=2)
label1.grid(row=4,column=0)
label2.grid(row=4,column=2)
label3.grid(row=6,column=0)
label4.grid(row=6,column=2)
label5.grid(row=7,column=0)
label6.grid(row=5,column=0)

entry1.grid(row=4,column=1)
entry2.grid(row=4,column=3)
entry3.grid(row=6,column=1)
entry4.grid(row=6,column=3)
entry5.grid(row=7,column=1)
entry6.grid(row=5,column=1)

var=StringVar()
male_cb=Checkbutton(tab1,text="Male",variable=var,onvalue="on",offvalue="off",font=("Times New Roman",16),bg="orange")
female_cb=Checkbutton(tab1,text="Female",variable=var,onvalue="on",offvalue="off",font=("Times New Roman",16),bg="orange")
male_cb.deselect()
female_cb.deselect()
male_cb.grid(row=5,column=2)
female_cb.grid(row=5,column=3)

# contact Details
label_space2=Label(tab1,text="        ",bg="orange")
label_cd=Label(tab1,text="Contact Details",font=("Times New Roman",16),bg="orange")
label_space3=Label(tab1,text="        ",bg="orange")
label12=Label(tab1,text="Student's Phone Number",font=("Times New Roman",14),bg="orange")
label7=Label(tab1,text="Student's Email Id",font=("Times New Roman",14),bg="orange")
label8=Label(tab1,text="Father's Phone Number",font=("Times New Roman",14),bg="orange")
label9=Label(tab1,text="Mother's Phone Number",font=("Times New Roman",14),bg="orange")
label10=Label(tab1,text="Local Guardian's Phone Number",font=("Times New Roman",14),bg="orange")
label11=Label(tab1,text="Local Guardian's Email Id",font=("Times New Roman",14),bg="orange")


entry7=Label(tab1,text="",font=("Times New Roman",14),bg="orange")
entry8=Entry(tab1,font=("Times New Roman",14))
entry9=Entry(tab1,font=("Times New Roman",14))
entry10=Entry(tab1,font=("Times New Roman",14))
entry11=Entry(tab1,font=("Times New Roman",14))
entry12=Entry(tab1,font=("Times New Roman",14))

label_space2.grid(row=8,column=2)
label_cd.grid(row=9,column=0)
label_space3.grid(row=10,column=2)
label7.grid(row=11,column=0)
label8.grid(row=11,column=2)
label9.grid(row=12,column=0)
label10.grid(row=12,column=2)
label11.grid(row=13,column=0)
label12.grid(row=13,column=2)

entry7.grid(row=11,column=1)
entry8.grid(row=11,column=3)
entry9.grid(row=12,column=1)
entry10.grid(row=12,column=3)
entry11.grid(row=13,column=1)
entry12.grid(row=13,column=3)

# Address Details
label_space4=Label(tab1,text="        ",bg="orange")
label_ad_d=Label(tab1,text="Address Details",font=("Times New Roman",16),bg="orange")
label_space5=Label(tab1,text="        ",bg="orange")
label13=Label(tab1,text="Country",font=("Times New Roman",14),bg="orange")
label14=Label(tab1,text="State",font=("Times New Roman",14),bg="orange")
label15=Label(tab1,text="City",font=("Times New Roman",14),bg="orange")
label16=Label(tab1,text="Zip code",font=("Times New Roman",14),bg="orange")
label17=Label(tab1,text="Temporary Address",font=("Times New Roman",14),bg="orange")
label18=Label(tab1,text="Permanant Address",font=("Times New Roman",14),bg="orange")

entry13=Entry(tab1,font=("Times New Roman",14))
entry14=Entry(tab1,font=("Times New Roman",14))
entry15=Entry(tab1,font=("Times New Roman",14))
entry16=Entry(tab1,font=("Times New Roman",14))
entry17=Entry(tab1,font=("Times New Roman",14))
entry18=Entry(tab1,font=("Times New Roman",14))

label_space4.grid(row=14,column=2)
label_ad_d.grid(row=15,column=0)
label_space5.grid(row=16,column=2)
label13.grid(row=17,column=0)
label14.grid(row=17,column=2)
label15.grid(row=18,column=0)
label16.grid(row=18,column=2)
label17.grid(row=19,column=0)
label18.grid(row=19,column=2)

entry13.grid(row=17,column=1)
entry14.grid(row=17,column=3)
entry15.grid(row=18,column=1)
entry16.grid(row=18,column=3)
entry17.grid(row=19,column=1)
entry18.grid(row=19,column=3)

def sub1():
    tab1.destroy()
    tab2=ttk.Frame(tabs,style='new.TFrame')
    tabs.add(tab2,text="Qual")
    tabs.pack(expan=1,fil="both")


    label_t=Label(tab2,text="Qualification ",font=("Times New Roman",18),bg="orange")
    label_space=Label(tab2,text="        ",bg="orange")
    label_pe=Label(tab2,text="Primary education",font=("Times New Roman",16),bg="orange")
    label1=Label(tab2,text="School Name",font=("Times New Roman",14),bg="orange")
    label2=Label(tab2,text="Board",font=("Times New Roman",14),bg="orange")
    label3=Label(tab2,text="Grade/ Percentage",font=("Times New Roman",14),bg="orange")
    label4=Label(tab2,text="Passing year",font=("Times New Roman",14),bg="orange")
    label5=Label(tab2,text="Country",font=("Times New Roman",14),bg="orange")
    label6=Label(tab2,text="State",font=("Times New Roman",14),bg="orange")
    label7=Label(tab2,text="City",font=("Times New Roman",14),bg="orange")
    label8=Label(tab2,text="Zip Code",font=("Times New Roman",14),bg="orange")
    label9=Label(tab2,text="Address",font=("Times New Roman",14),bg="orange")

    entry1=Entry(tab2,font=("Times New Roman",14))
    entry2=Entry(tab2,font=("Times New Roman",14))
    entry3=Entry(tab2,font=("Times New Roman",14))
    entry4=Entry(tab2,font=("Times New Roman",14))
    entry5=Entry(tab2,font=("Times New Roman",14))
    entry6=Entry(tab2,font=("Times New Roman",14))
    entry7=Entry(tab2,font=("Times New Roman",14))
    entry8=Entry(tab2,font=("Times New Roman",14))
    entry9=Entry(tab2,font=("Times New Roman",14))

    label_t.grid(row=0,column=2)
    label_space.grid(row=1,column=2)
    label_pe.grid(row=2,column=0)
    label1.grid(row=5,column=0)
    label2.grid(row=5,column=2)
    label3.grid(row=6,column=0)
    label4.grid(row=6,column=2)
    label5.grid(row=7,column=0)
    label6.grid(row=7,column=2)
    label7.grid(row=8,column=0)
    label8.grid(row=8,column=2)
    label9.grid(row=9,column=0)

    entry1.grid(row=5,column=1)
    entry2.grid(row=5,column=3)
    entry3.grid(row=6,column=1)
    entry4.grid(row=6,column=3)
    entry5.grid(row=7,column=1)
    entry6.grid(row=7,column=3)
    entry7.grid(row=8,column=1)
    entry8.grid(row=8,column=3)
    entry9.grid(row=9,column=1)

    label_space20=Label(tab2,text="        ",font=("Times New Roman",14),bg="orange")
    label_pi=Label(tab2,text="Secondory education",font=("Times New Roman",16),bg="orange")
    label9=Label(tab2,text="College Name",font=("Times New Roman",14),bg="orange")
    label34=Label(tab2,text="Board",font=("Times New Roman",14),bg="orange")
    label32=Label(tab2,text="Grade/ Percentage",font=("Times New Roman",14),bg="orange")
    label43=Label(tab2,text="Passing year",font=("Times New Roman",14),bg="orange")
    label53=Label(tab2,text="Country",font=("Times New Roman",14),bg="orange")
    label69=Label(tab2,text="State",font=("Times New Roman",14),bg="orange")
    label63=Label(tab2,text="City",font=("Times New Roman",14),bg="orange")
    label61=Label(tab2,text="Zip Code",font=("Times New Roman",14),bg="orange")
    label62=Label(tab2,text="Address",font=("Times New Roman",14),bg="orange")

    entry9=Entry(tab2,font=("Times New Roman",14))
    entry10=Entry(tab2,font=("Times New Roman",14))
    entry11=Entry(tab2,font=("Times New Roman",14))
    entry12=Entry(tab2,font=("Times New Roman",14))
    entry13=Entry(tab2,font=("Times New Roman",14))
    entry14=Entry(tab2,font=("Times New Roman",14))
    entry15=Entry(tab2,font=("Times New Roman",14))
    entry16=Entry(tab2,font=("Times New Roman",14))
    entry17=Entry(tab2,font=("Times New Roman",14))
    entry18=Entry(tab2,font=("Times New Roman",14))


    label_space20.grid(row=10,column=2)
    label_pi.grid(row=11,column=0)
    label9.grid(row=13,column=0)
    label34.grid(row=13,column=2)
    label32.grid(row=14,column=0)
    label43.grid(row=14,column=2)
    label53.grid(row=15,column=0)
    label69.grid(row=15,column=2)
    label63.grid(row=16,column=0)
    label61.grid(row=16,column=2)
    label62.grid(row=17,column=0)


    entry10.grid(row=13,column=1)
    entry11.grid(row=13,column=3)
    entry12.grid(row=14,column=1)
    entry13.grid(row=14,column=3)
    entry14.grid(row=15,column=1)
    entry15.grid(row=15,column=3)
    entry16.grid(row=16,column=1)
    entry17.grid(row=16,column=3)
    entry18.grid(row=17,column=1)


    label_space6=Label(tab2,text="       ",bg="orange")
    label19=Label(tab2,text="PURSUIG DEGREE",font=("Times New Roman",16),bg="orange")
    label20=Label(tab2,text="Degree",font=("Times New Roman",16),bg="orange")
    options=["BCOM",
                "BA",
                "BBA",
                "LLB",
                "BCOM (HON)",
                "BMS",
                "CA",
                "ACCA",
                "BCA",
                "BSC"
                "B.TECH"]

    click=StringVar()
    click.set("DEGREE")

    dd_b=OptionMenu(tab2,click,*options)

    label_space6.grid(row=18,column=2)
    label19.grid(row=19,column=0)
    dd_b.grid(row=20,column=1)
    label20.grid(row=20,column=0)

    def TC():
        messagebox.showinfo("button_agree", "This disclaimer says that, you have provided all the  etails as best of your knoowledge and  if this information is found to be wromg or framed or misleading than the institute has complete authority to reject your application. you will not be provided with any refund, and also that institute has complete authority to bann you from further apllication")

    button_tc=Button(tab2,text="Terms and Condition",font=("Times New Roman",16),command=TC)
    button_tc.grid(row=21,column=1)
    def ag():
        if ag:
            def sub2():
                messagebox.showinfo("Submit","Your Form has been submitted")
                tab2.destroy()
                win.destroy()
            button1=Button(tab2,text="Submit",font=("Times New Roman",16),command=sub2)
            button1.grid(row=22,column=2)

    var1=StringVar()
    Agree=Checkbutton(tab2,text="Agree",variable=var1,onvalue="on",offvalue="off",font=("Times New Roman",16),bg="orange",command=ag)
    Agree.deselect()
    Agree.grid(row=21,column=2)

button=Button(tab1,text="Submit",font=("Times New Roman",14),command=sub1)
button.grid(row=20,column=2)

win.mainloop()
