import random
import tkinter as tk
import numpy as np



class Application(tk.Frame):
    
    def __init__(self, master=None, FONT=20, height=150, width=150):
        super().__init__(master)
        self.FONT = FONT
        self.HEIGHT = height
        self.WIDTH = width
        self.CELL_SIZE = 10 
        
        self.state = np.zeros((self.HEIGHT, self.WIDTH), dtype=np.int8)
        self.next_state = np.empty((self.HEIGHT, self.WIDTH), dtype=np.int8)
        self.state = np.random.randint(
            2, size=(self.HEIGHT, self.WIDTH), dtype=np.int8
        )

        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        # Canvas
        w = self.CELL_SIZE * self.WIDTH
        h = self.CELL_SIZE * self.HEIGHT
        self.cv = tk.Canvas(width=w, height=h)
        self.cv.pack()

        self.cv.create_rectangle(
            0, 0, w, h, fill="white", tag="dead"
        )
        self.cv.tag_bind("dead", "<1>", self.dead_or_alive)

        # Buttons
        self.ss_button = tk.Button(self, font=self.FONT)
        self.toggle_start()
        self.ss_button.grid(row=0, column=1)

        self.next_button = tk.Button(
                self, text=">", font=self.FONT,
                command=self.next_generation
            )
        self.next_button.grid(row=0, column=2)

        self.previous_button = tk.Button(
                self, text="<", font=self.FONT,
            )
        self.previous_button.grid(row=0, column=0)

        self.show_matrix(self.state)
        self.flag = False
        self.master.after(1, self.scanning)

    def toggle_start(self):
        self.ss_button["text"] = "START"
        self.ss_button["command"] = self.start

    def toggle_stop(self):
        self.ss_button["text"] = "STOP"
        self.ss_button["command"] = self.stop

    def scanning(self):
        if self.flag:
            self.next_generation()
        self.master.after(1, self.scanning)

    def start(self):
        self.flag = True
        self.toggle_stop()

    def stop(self):
        self.flag = False
        self.toggle_start()

    def next_generation(self):
        state, next_state = self.state, self.next_state
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                # nw: north west, ne: north east, c: center ...
                nw = state[i-1,j-1]
                n  = state[i-1,j]
                ne = state[i-1,(j+1)%self.WIDTH]
                w  = state[i,j-1]
                c  = state[i,j]
                e  = state[i,(j+1)%self.WIDTH]
                sw = state[(i+1)%self.HEIGHT,j-1]
                s  = state[(i+1)%self.HEIGHT,j]
                se = state[(i+1)%self.HEIGHT,(j+1)%self.WIDTH]
                neighbor_cell_sum = nw + n + ne + w + e + sw + s + se
                if c == 0 and neighbor_cell_sum == 3:
                   next_state[i,j] = 1
                elif c == 1 and neighbor_cell_sum in (2,3):
                   next_state[i,j] = 1
                else:
                   next_state[i,j] = 0
            self.state, self.next_state = next_state, state
        self.cv.tag_bind("alive", "<1>", self.dead_or_alive)
        self.show_matrix(next_state)
    
    def previous_generation(self):
        pass

    def dead_or_alive(self, event):
        x, y = event.x // self.CELL_SIZE, event.y // self.CELL_SIZE
        d_or_a = self.state[x, y]
        self.state[x, y] = 1 - d_or_a
        self.show_matrix(self.state)

    def show_matrix(self, matrix):
        self.cv.delete("alive")
        for i in range(self.HEIGHT):
            for j in range(self.WIDTH):
                if matrix[i, j] == 1:
                    self.cv.create_rectangle(
                        i*self.CELL_SIZE, j*self.CELL_SIZE,
                        (i+1)*self.CELL_SIZE, (j+1)*self.CELL_SIZE,
                        fill="black", tag="alive"
                    )
        self.cv.update()



root = tk.Tk()
app = Application(master=root)
app.mainloop()
