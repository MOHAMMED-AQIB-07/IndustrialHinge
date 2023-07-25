from tkinter import *
root = Tk()
root.title("Industrial Hinge")
root.geometry("400x600")

Label(root, font = ("Arial", 16), text = "Industrial Hinge"). place (x=100, y=50)

force Entry(root, width= 8)
Width Entry(root, width = 8)
Length Entry(root, width = 8) =

force.place(x=200, y = 150)
Width.place(x = 200, y = 200)
Length.place(x = 200, y = 250)

force_label = Label(root, font = ("Helvitica", 14), width = 8, text = "Force")
width_label= Label (Foot, font = ("Helvitica", 14), width = 8, text ="Width")
Length_label = Label(root, font = ("Helvitica", 14), width= 8, text = "Length")

force_label.place(x = 100, y = 150)
width_label.place(x = 100, y = 200)
Length label.place(x = 100, y = 250)

def calculate_func():
  f=float(force.get())
  w=float(width.get())
  l=float (Length.get())
  area = w*l
  stress = f/area
  Area_label.config(text = "Area: + str(area))
  Stress_label.config(text = "Stress: " + str(stress))

calculate = Button (root, font = ("Helvitica", 14), width = 8, text = "Calculate", command = calculate_func, bg = "orange")
calculate.place(x = 200, y = 300)

Area_label = Label(root, font = ("Helvitica", 14), text = "Area:", fg = "blue")
Area_label.place(x = 100, y = 350)

Stress_label = Label (root, font = ("Helvitica", 14), text = "stress", fg = "blue")
Stress_label.place(x = 100, y = 400)

root.mainloop()
