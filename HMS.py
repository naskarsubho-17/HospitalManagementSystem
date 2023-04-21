from tkinter import*
from tkinter import ttk
win=Tk()
win.state('zoomed')
win.config(bg='black')
#Heading
Label(win,text='Hospital Management System',font='impack 31 bold',bg='blue',fg='white').pack(fill=X)
#Frame1
frame1=Frame(win,bd=15,relief=RIDGE)
frame1.place(x=0,y=54,width=1280,height=310)
#Label Frame For Patient Info.
lf1=LabelFrame(frame1,text='Patient Information',font='arial 10 bold',bd=10,bg='pink')
lf1.place(x=10,y=0,width=750,height=280)
#Labels for patient information
Label(lf1,text='Name of Tablets',bg='pink').place(x=5,y=10)
Label(lf1,text='Reference No.',bg='pink').place(x=5,y=40)
Label(lf1,text='Dose',bg='pink').place(x=5,y=70)
Label(lf1,text='No. of Tablets',bg='pink').place(x=5,y=100)
Label(lf1,text='Issue Date',bg='pink').place(x=5,y=130)
Label(lf1,text='Exp. Date',bg='pink').place(x=5,y=160)
Label(lf1,text='Daily Dose',bg='pink').place(x=5,y=190)
Label(lf1,text='Side Effect',bg='pink').place(x=5,y=220)
Label(lf1,text='Blood Pressure',bg='pink').place(x=370,y=10)
Label(lf1,text='Storage Device',bg='pink').place(x=370,y=40)
Label(lf1,text='Medication',bg='pink').place(x=370,y=70)
Label(lf1,text='Patient id',bg='pink').place(x=370,y=100)
Label(lf1,text='Name of Patient',bg='pink').place(x=370,y=130)
Label(lf1,text='DOB',bg='pink').place(x=370,y=160)
Label(lf1,text='Patient Address',bg='pink').place(x=370,y=190)
#Entry Field for all Labels
e1=Entry(lf1,bd=4)
e1.place(x=130,y=10,width=200)

e2=Entry(lf1,bd=4)
e2.place(x=130,y=40,width=200)

e3=Entry(lf1,bd=4)
e3.place(x=130,y=70,width=200)

e4=Entry(lf1,bd=4)
e4.place(x=130,y=100,width=200)

e5=Entry(lf1,bd=4)
e5.place(x=130,y=130,width=200)

e6=Entry(lf1,bd=4)
e6.place(x=130,y=160,width=200)

e7=Entry(lf1,bd=4)
e7.place(x=130,y=190,width=200)

e8=Entry(lf1,bd=4)
e8.place(x=130,y=220,width=200)

e9=Entry(lf1,bd=4)
e9.place(x=500,y=10,width=200)

e10=Entry(lf1,bd=4)
e10.place(x=500,y=40,width=200)

e11=Entry(lf1,bd=4)
e11.place(x=500,y=70,width=200)

e12=Entry(lf1,bd=4)
e12.place(x=500,y=100,width=200)

e13=Entry(lf1,bd=4)
e13.place(x=500,y=130,width=200)

e14=Entry(lf1,bd=4)
e14.place(x=500,y=160,width=200)

e15=Entry(lf1,bd=4)
e15.place(x=500,y=190,width=200)

#Label Frame for Prescription
lf2=LabelFrame(frame1,text='Prescription',font='arial 12 bold',bd=10)
lf2.place(x=760,y=0,width=470,height=280)
#Textbox for Prescription
txt_frme=Text(lf2,font='impack 10 bold',width=40,height=30,bg='yellowgreen')
txt_frme.pack(fill=BOTH)

#Frame2
frame2=Frame(win,bd=15,relief=RIDGE)
frame2.place(x=0,y=360,width=1280,height=250)
#Button
#Delete Button
d_btn=Button(win,text='Delete',font='ariel 15 bold',bg='brown',fg='white',bd=6,cursor='hand2')
d_btn.place(x=0,y=600,width=270)
#Prescription Button
p_btn=Button(win,text='Prscription',font='ariel 15 bold',bg='purple',fg='white',bd=6,cursor='hand2')
p_btn.place(x=270,y=600,width=330)
#Save Prescriptioin Data
pd_btn=Button(win,text='Save Prescription Data',font='ariel 15 bold',bg='green',fg='white',bd=6,cursor='hand2')
pd_btn.place(x=600,y=600,width=340)
#Clear Button
c_btn=Button(win,text='Clear',font='ariel 15 bold',bg='blue',fg='white',bd=6,cursor='hand2')
c_btn.place(x=940,y=600,width=170)
#Exit Button
e_btn=Button(win,text='Exit',font='ariel 15 bold',bg='red',fg='white',bd=6,cursor='hand2')
e_btn.place(x=1110,y=600,width=170)
#Scroll Bar for Prescription Data
scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
scroll_x.pack(side='bottom',fill='x')
scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
scroll_y.pack(side='right',fill='y')

table=ttk.Treeview(frame2,columns=('not','ref','dose','nots','issd','expd','dd','sd','pn','dob','pa'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
scroll_x=ttk.Scrollbar(command=table.xview)
scroll_y=ttk.Scrollbar(command=table.yview)
#Heading for Prescription data 
table.heading('not',text='Name of Tablets')
table.heading('ref',text='Reference No.')
table.heading('dose',text='Dose')
table.heading('nots',text='No. of Tablets')
table.heading('issd',text='Issue Date')
table.heading('expd',text='Exp. Date')
table.heading('dd',text='Daily Dose')
table.heading('sd',text='Side Effect')
#table.heading('dd',text='Blood Pressure')
#table.heading('dd',text='Storage Device')
table.heading('pn',text='Patient Name')
table.heading('dob',text='DOB')
table.heading('pa',text='Patient Address')
table['show']='headings'
table.pack(fill=BOTH,expand=1)


table.column('not',width=100)
table.column('ref',width=100)
table.column('not',width=100)
table.column('dose',width=100)
table.column('nots',width=100)
table.column('issd',width=100)
table.column('expd',width=100)
table.column('dd',width=100)
table.column('sd',width=100)
table.column('pn',width=100)
table.column('dob',width=100)
table.column('pa',width=100)

mainloop()