from tkinter import *
import os
from PIL import ImageTk,Image
import mysql.connector
import random
import pathlib
root=Tk()

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="qweabc",
  database="trivia"
)


#backgroundz
root.geometry('800x500')


root.title("TRIVIA")

PATH_DIR = pathlib.Path(__file__).parent.resolve()
PATH_BG = str(PATH_DIR)+'\\background.png'
PATH_SCR = str(PATH_DIR)+'\\Screenshot (5).png'
# print(str(PATH_DIR)+'\\icon.ico')



root.iconbitmap(PATH_DIR)

im = Image.open(PATH_BG)
Img=ImageTk.PhotoImage(im)
label11 = Label( root, image = Img)
label11.place(x = 0,y = 0)

#second image
IM = Image.open(PATH_SCR)
IMG=ImageTk.PhotoImage(IM)





#function of start button
def START():
     
     newwindow =Toplevel(root, background= "skyblue")
    
    # newwindow.iconbitmap("C:\\Users\\aditi\\Desktop\\icon2.ico")
      
    # sets the title of the
    # Toplevel widget why no property set wiyh icon
     
     width= newwindow.winfo_screenwidth() 
     height= newwindow.winfo_screenheight()
     #setting tkinter window size
     newwindow.geometry("%dx%d" % (width, height))
     newwindow.resizable(0,0)
     
     global Qno
     global score
     Qno = 0
     score = 0
    
     OPTION=IntVar()
        
     


     def DisplayQues(Qno):
          newwindow.title("TRIVIA")
          Label13=Label(newwindow,text="TOPIC: GENERAL KNOWLEDGE",font=("bookman",16,"bold"),bg="lightblue",fg="red")
          Label13.place(x=500,y=1)
          Label14=Label(newwindow,text=" ",bg="lightblue")
          Label16=Label(newwindow,text=" ",bg="lightblue")
          Label15=Label(newwindow,text=" ",bg="lightblue")
          Label17=Label(newwindow,text=" ",bg="lightblue")
          x = str(Qno  + 1) + ". "
          Label18=Label(newwindow,text=x,fg="black",bg="lightblue",font=("bookman",18))
          Label12=Label(newwindow,text=question[Qno],fg="black",bg="lightblue",font=("bookman",18))
          Label12.grid(row=5,column=2)
          Label14.grid(row=1,column=0)
          Label15.grid(row=4,column=0)
          Label16.grid(row=2,column=0 )   
          Label17.grid(row=3,column=0 ) 
          Label18.grid(row=5,column=1)

     def DisplayOption(Qno):
          
          r1 = Radiobutton(newwindow,variable=OPTION,value=1,text=options[Qno][0],bg="lightblue",font=("bookman",16))
          r1.place(x=250,y=120)
          r2 = Radiobutton(newwindow,variable=OPTION,value=2,text=options[Qno][1],bg="lightblue",font=("bookman",16))
          r2.place(x=250,y=160)
          r3 = Radiobutton(newwindow,variable=OPTION,value=3,text=options[Qno][2],bg="lightblue",font=("bookman",16))
          r3.place(x=250,y=200)
          r4 = Radiobutton(newwindow,variable=OPTION,value=4,text=options[Qno][3],bg="lightblue",font=("bookman",16))
          r4.place(x=250,y=240)
          #print(OPTION.get())

     def NEXTButton():
           global Qno
           if Qno==9:
               next=Button(newwindow,text="SUBMIT",command=NEXT,fg="black",bg="orange",font=("bookman",18))
               next.place(x=950,y=600)
               quit=Button(newwindow,text="QUIT",command=newwindow.quit,fg="black",bg="orange",font=("bookman",18))
               quit.place(x=1070,y=600)
           else:
               next=Button(newwindow,text="NEXT",command=NEXT,fg="black",bg="orange",font=("bookman",18))
               next.place(x=980,y=600)
               quit=Button(newwindow,text="QUIT",command=newwindow.quit,fg="black",bg="orange",font=("bookman",18))
               quit.place(x=1070,y=600)
     
     def DisplayResult():
          # print("Result")
          labelIMG = Label( newwindow, image = IMG)
          labelIMG
          labelIMG.place(x=0,y=0)
          
          
          Label20=Label(newwindow,text="RESULT",font=("bookman",36,"bold"),fg="red")
          Label20.place(x=560,y=20)

          quit=Button(newwindow,text="QUIT",command=newwindow.quit,fg="yellow",bg="black",font=("bookman",18))
          quit.place(x=1070,y=600)
          ScoreT=("Score=",score)
          Label21=Label(newwindow,text=ScoreT,font=("bookman",24,"bold"),bg="dark blue",fg="lightblue")
          Label21.place(x=800,y=330)
          
          percentage = str((score/10)*100)
          PercentageT=("Percentage=",percentage)
          Label22=Label(newwindow,text=PercentageT,font=("bookman",24,"bold"),bg="darkblue",fg="lightblue")
          Label22.place(x=800,y=380)

          
          NAMEEE=str("Thankyou "+E1.get()+" for attempting the Trivia")
          Label23=Label(newwindow,text=NAMEEE,font=("bookman",30,"bold"),bg="darkblue",fg="orange")
          Label23.place(x=200,y=250)

          
     def Checkanswer():
          
          global score
          value = OPTION.get()
         
          if options[Qno][value-1] == answer[Qno]:
               score = score + 1
          

     def NEXT():

          for widget in newwindow.winfo_children():
              widget.destroy()

          global Qno
          if Qno==9:
               Checkanswer()
               #print(score)
               DisplayResult()
          else:
               Checkanswer()
               Qno = Qno + 1
               DisplayQues(Qno)
               DisplayOption(Qno)
               NEXTButton()

     DisplayQues(Qno)
     DisplayOption(Qno)
     NEXTButton()

     


 
#variable and name
Label1=Label(root,text="TOPIC: GENERAL KNOWLEDGE",font=("bookman",16,"bold"),bg="yellow",fg="black")

Label2=Label(root,text="NAME: ",font=("arial",10,"bold"))
#extra space
Label6=Label(root,text="",bg="black")
Label7=Label(root,text="",bg="black")
Label9=Label(root,text="",bg="black")
Label10=Label(root,text="",bg="black")
Label3=Label(root,text="",bg="black")




E1=Entry(root)
def func1():
     E1.get
     Label4=Label(root,text=" Hello " + E1.get(),font=("arial",12,"bold"),fg="white",bg="blue")
     Label5=Label(root,text= """INSTRUCTION :

     Select an answer for every question.
      Unanswered questions will be scored as incorrect.
     All questions are single correct answer 
     Total number of questions = 10
     there is no negative marking
      Maximum marks = 10
     Your progress won't be saved if you quit the test
     Click on start to start the test
     """,anchor=NW,font=(12,),fg="white",bg="grey")
     Button3=Button(root,text="Exit",font=('arial',14,"bold"),bg="red",fg="black",command=root.quit)

	 
    
#     #position#
     Label4.grid(row=6,column=3)
     Label5.grid(row=7,column=4)
     Button2=Button(root,text="Start",font=('arial',14,"bold"),bg="red",fg="black",command=START)
     Button2.grid(row=10,column=8)
     Button3.grid(row=10,column=9)
	 

Button1=Button(root,text="CLICK ME",command=func1,bg="green",fg="white",font=("ariel",8,"bold"))






 #position
Label1.grid(row=0,column=4)
Label3.grid(row=1,column=4)
Label2.grid(row=3,column=0,)
E1.grid(row=3,column=1)
Label6.grid(row=3,column=2)
Button1.grid(row=3,column=3)
Label7.grid(row=5,column=1)
Label9.grid(row=8,column=6)
Label10.grid(row=9,column=7)



#database connection
mycursor = mydb.cursor()

mycursor.execute("SELECT count(*) FROM questions")

val = mycursor.fetchall()

x = random.sample(range(1,val[0][0]+1), 10)
# print(x)

lst = [2,3,4,5]
question = []
options = []
answer = []

# set the question, options, and answer
for i in range(10):
	y = "SELECT * FROM questions where qno = \'{}\'".format(x[i])
	mycursor.execute(y)
	Val = mycursor.fetchall()
	question.append(Val[0][1])
	answer.append(Val[0][2])
	random.shuffle(lst)
	op = []
	op.extend([Val[0][lst[0]],Val[0][lst[1]],Val[0][lst[2]],Val[0][lst[3]]])
	options.append(op)







root.resizable(0,0)
root.mainloop()










# CREATE TABLE `questions` (
#   `qno` int(11) DEFAULT NULL,
#   `question` varchar(256) DEFAULT NULL,
#   `option1` varchar(256) DEFAULT NULL,
#   `option2` varchar(256) DEFAULT NULL,
#   `option3` varchar(256) DEFAULT NULL,
#   `option4` varchar(256) DEFAULT NULL
# ) 