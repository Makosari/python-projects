import tkinter

#creating lamp by clicking on the screen and also creating its mirror image

okno = tkinter.Tk()

sirka = 1000
vyska = 650

platno = tkinter.Canvas(width=sirka, height=vyska)  # text veci a pozadie
platno.pack()

platno.create_rectangle(0, 0, 1000, 325, fill='green', outline='')
platno.create_rectangle(0, 325, 1000, 650, fill='blue', outline='')

counter = 0


def createLamp(event):
	global counter
	if counter < 9:
		counter += 1

		if event.y < 326:
			x = event.x
			y = event.y

			platno.create_rectangle(x - 20, y - 40, x, y, fill='grey')
			platno.create_rectangle(x - 12, y - 40, x - 8, y - 90, fill='grey', outline='')
			platno.create_oval(x - 20, y - 110, x, y - 90, fill='yellow', outline='')
			platno.create_text(x - 10, y - 20, text=str(counter))

			y = 650 - y

			platno.create_rectangle(x - 20, y - 40, x, y, fill='grey')
			platno.create_rectangle(x - 12, y, x - 8, y + 50, fill='grey', outline='')
			platno.create_oval(x - 20, y + 70, x, y + 50, fill='yellow', outline='')
			platno.create_text(x - 10, y - 20, text=str(counter), angle=180)

			platno.update()


platno.bind_all('<Button-1>', createLamp)

tkinter.mainloop()
