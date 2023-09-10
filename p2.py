from tkinter import *
from tkinter.messagebox import*
import requests
from PIL import Image,ImageTk

root=Tk()
root.geometry("860x460")
root.title("Weather Application")


f=("Algerian",20,"bold")


def weath():
	city=ent1.get()
	if city!="":
		try:
			a1="http://api.openweathermap.org/data/2.5/weather"
			a2="?units=metric"
			a3="&appid="+"c6e315d09197cec231495138183954bd"
			a4="&q="+city
			wa=a1+a2+a3+a4
			res=requests.get(wa)
			data=res.json()
			temp=data["main"]["temp"]
			msg="temp ="+str(temp)
			showinfo("successsful",msg)
			ent1.delete(0,END)
		except Exception as e:
			msg="issue"+str(e)
			showerror("Unsucessful",msg)
			ent1.delete(0,END)
	else :
		showerror("Error","Please fill the city field")
		ent1.delete(0,END)

bg=ImageTk.PhotoImage(file="w2.png")
bg_iamge=Label(root,image=bg).place(x=0,y=0,relwidth=1,relheight=1)
lab1=Label(root,text="Enter City Name",font=f)
lab1.pack(pady=10)


ent1=Entry(root,bd=2,font=f)
ent1.pack(pady=20)

but1=Button(root,text="Find",font=f,bg="black",fg="white",command=weath)
but1.pack(pady=30)
root.mainloop()
