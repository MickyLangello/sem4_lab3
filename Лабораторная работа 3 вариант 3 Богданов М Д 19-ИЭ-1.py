'''
На форме располагается главное меню на четыре опции.
Три первых (птицы, рыбы, звери) из них поочередно активизируют свои
компоненты Canvas. К каждому такому компоненты привязано контекстное меню
для выбора отображаемого на Canvas рисунка (по 6 экземпляров).
При активизации одного из Canvas предыдущий активный виджет
становится невидимым. Название отображаемого объекта указывается
в заголовке формы. Опция «Закрытие окна» заканчивает программу.
'''

from tkinter import *

image = 0

def fishh(*args):
    root.unbind("<Button-3>")
    root.bind("<Button-3>", lambda event: fish.post(event.x_root, event.y_root))

def animall(*args):
    root.unbind("<Button-3>")
    root.bind("<Button-3>", lambda event: animal.post(event.x_root, event.y_root))

def birdd(*args):
    root.unbind("<Button-3>")
    root.bind("<Button-3>", lambda event: bird.post(event.x_root, event.y_root))
    
def showImage():
    global tmn, image
    if tmn.get()==11:
        image =PhotoImage(file = "popka.png")
        root.title("Попугай")
    elif tmn.get()==12:
        image =PhotoImage(file = "golub.png")
        root.title("Голубь")
    elif tmn.get()==13:
        image =PhotoImage(file = "vorona.png")
        root.title("Ворона")
    elif tmn.get()==14:
        image =PhotoImage(file = "vorobej.png")
        root.title("Воробей")
    elif tmn.get()==15:
        image =PhotoImage(file = "40ka.png")
        root.title("Сорока")
    elif tmn.get()==16:
        image =PhotoImage(file = "sinitsa.png")
        root.title("Синица")
        
    elif tmn.get()==21:
        image =PhotoImage(file = "karp.png")
        root.title("Карп")
    elif tmn.get()==22:
        image =PhotoImage(file = "shark.png")
        root.title("Акула")
    elif tmn.get()==23:
        image =PhotoImage(file = "losos.png")
        root.title("Лосось")
    elif tmn.get()==24:
        image =PhotoImage(file = "osetr.png")
        root.title("Осётр")
    elif tmn.get()==25:
        image =PhotoImage(file = "piranja.png")
        root.title("Пиранья")
    elif tmn.get()==26:
        image =PhotoImage(file = "krilatka.png")
        root.title("Крылатка")

    elif tmn.get()==31:
        image =PhotoImage(file = "auf.png")
        root.title("Волк")
    elif tmn.get()==32:
        image =PhotoImage(file = "zayac.png")
        root.title("Заяц")
    elif tmn.get()==33:
        image =PhotoImage(file = "zebra.png")
        root.title("Зебра")
    elif tmn.get()==34:
        image =PhotoImage(file = "giraffe.png")
        root.title("Жираф")
    elif tmn.get()==35:
        image =PhotoImage(file = "fox.png")
        root.title("Лиса")
    elif tmn.get()==36:
        image =PhotoImage(file = "kaban.png")
        root.title("Кабан")

    canv.create_image(0, 0, anchor='nw', image=image)

root = Tk()
root.geometry('480x480')
root['bg'] = 'pink'
root.title('Богданов Максим 19-ИЭ-1')
root.resizable(0,0)

mainMenu = Menu(root)
root.config(menu = mainMenu)

bird=Menu(mainMenu,tearoff = 0)
fish=Menu(mainMenu,tearoff = 0)
animal=Menu(mainMenu,tearoff = 0)
close=Menu(mainMenu,tearoff = 0)
tmn = IntVar()

canv=Canvas(root, width=480, height=480, bg='pink')
canv.pack()

bird.add_checkbutton(label = "Попугай", variable = tmn, onvalue  = 11, offvalue=0, command=showImage)
bird.add_checkbutton(label = "Голубь", variable = tmn, onvalue  = 12, offvalue=0, command=showImage)
bird.add_checkbutton(label = "Ворона", variable = tmn, onvalue  = 13, offvalue=0, command=showImage)
bird.add_checkbutton(label = "Воробей", variable = tmn, onvalue  = 14, offvalue=0, command=showImage)
bird.add_checkbutton(label = "Сорока", variable = tmn, onvalue  = 15, offvalue=0, command=showImage)
bird.add_checkbutton(label = "Синица", variable = tmn, onvalue  = 16, offvalue=0, command=showImage)

fish.add_checkbutton(label = "Карп", variable = tmn, onvalue  = 21, offvalue=0, command=showImage)
fish.add_checkbutton(label = "Акула", variable = tmn, onvalue  = 22, offvalue=0, command=showImage)
fish.add_checkbutton(label = "Лосось", variable = tmn, onvalue  = 23, offvalue=0, command=showImage)
fish.add_checkbutton(label = "Осётр", variable = tmn, onvalue  = 24, offvalue=0, command=showImage)
fish.add_checkbutton(label = "Пиранья", variable = tmn, onvalue  = 25, offvalue=0, command=showImage)
fish.add_checkbutton(label = "Крылатка", variable = tmn, onvalue  = 26, offvalue=0, command=showImage)

animal.add_checkbutton(label = "Волк", variable = tmn, onvalue  = 31, offvalue=0, command=showImage)
animal.add_checkbutton(label = "Заяц", variable = tmn, onvalue  = 32, offvalue=0, command=showImage)
animal.add_checkbutton(label = "Зебра", variable = tmn, onvalue  = 33, offvalue=0, command=showImage)
animal.add_checkbutton(label = "Жираф", variable = tmn, onvalue  = 34, offvalue=0, command=showImage)
animal.add_checkbutton(label = "Лиса", variable = tmn, onvalue  = 35, offvalue=0, command=showImage)
animal.add_checkbutton(label = "Кабан", variable = tmn, onvalue  = 36, offvalue=0, command=showImage)

mainMenu.add_command(label = "Птицы", command = birdd)
mainMenu.add_command(label = "Рыбы", command = fishh)
mainMenu.add_command(label = "Звери", command = animall)
mainMenu.add_command(label = "Закрытие окна", command = root.destroy)


root.mainloop()

