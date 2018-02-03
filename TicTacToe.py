from tkinter import *
from tkinter import messagebox

class Game:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(width=False,height=False)
        self.root.title('TicTacToe')
        self.canvas = Canvas(master= self.root, width= 600,height=600,bg='blue')
        self.canvas.grid(row=0,column=0)

        self.menubar = Menu(self.root)
        filemenu = Menu(self.menubar, tearoff=0)
        filemenu.add_command(label="New Game", command=self.new)

        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.root.quit)
        self.menubar.add_cascade(label="File", menu=filemenu)

        #GAME LOGIC VARIABLES
        self.board = [[0,0,0],[0,0,0],[0,0,0]]
        self.player = 1
        #Bindings
        self.canvas.bind('<Configure>', func=self.grid)
        self.canvas.bind('<Button-1>',func=self.clicked)

    def grid(self,event:Event):
        w,h = self.canvas.winfo_width()/3,self.canvas.winfo_height()/3
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                self.canvas.create_rectangle(j * w, i * h, (j * w) + w, (i * h) + h,width = 10)

    def clicked(self,event:Event):
        w,h = self.canvas.winfo_width()/3,self.canvas.winfo_height()/3
        r,c = 0,0
        for i in range(len(self.board)):
            if i * h < event.y < (i * w) + h:
                r = i
        for j in range(len(self.board[0])):
            if j * w < event.x < (j * w) + w:
                c= j
        if not self.over():
            if self.board[r][c] == 0:
                self.board[r][c] = self.player
                self.player *= -1
                self.draw()
        else:
            self.root.destroy()


    def draw(self):

        w,h = self.canvas.winfo_width()/3,self.canvas.winfo_height()/3
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                if self.board[i][j] == 1:
                    # self.canvas.create_line(100,100,200,200)
                    # self.canvas.create_line(200,100,100,200)

                    self.canvas.create_line(j*w, i*h, (j*w) + w, (i*h) + h, fill='red',width=7)
                    self.canvas.create_line((j*w) + w, i*h, j*w,(i*h) + h ,fill='red',width=7)
                elif self.board[i][j] == -1:
                    self.canvas.create_oval(j*w, i*h, (j*w) + w, (i*h) + h, outline='red',width=7)

    def over(self):

        if all(self.board[0][i]==1 for i in range(3)) or all(self.board[1][i]==1 for i in range(3)) or all(self.board[2][i]==1 for i in range(3)):
            messagebox._show(title="Game Over",message="Player X wins")
            return True

        elif all(self.board[0][i] == -1 for i in range(3)) or all(self.board[1][i] == -1 for i in range(3)) or all(self.board[2][i] == -1 for i in range(3)):
            messagebox._show(title="Game Over", message="Player O wins")
            return True

        elif all(self.board[i][0] == -1 for i in range(3)) or all(self.board[i][1] == -1 for i in range(3)) or all(self.board[i][2] == -1 for i in range(3)):
            messagebox._show(title="Game Over", message="Player O wins")
            return True

        elif all(self.board[i][0] == 1 for i in range(3)) or all(self.board[i][1] == 1 for i in range(3)) or all(self.board[i][2] == 1 for i in range(3)):
            messagebox._show(title="Game Over", message="Player X wins")
            return True

        elif all(self.board[i][i] == 1 for i in range(3)) or all(self.board[i][i] == 1 for i in reversed(range(3))):
            messagebox._show(title="Game Over", message="Player X wins")
            return True

        elif all(self.board[i][i] == -1 for i in range(3)) or all(self.board[i][i] == -1 for i in reversed(range(3))):
            messagebox._show(title="Game Over", message="Player O wins")
            return True

        elif self.board_full():
            messagebox._show(title="Game Over", message="No Winner")
            return True

    def board_full(self):
        if all(j == 1 or j == -1 for i in self.board for j in i):
            return True

    def run(self):
        self.root.config(menu=self.menubar)
        self.root.mainloop()


    def new(self):
        self.root.destroy()
        Game().run()



if __name__ == '__main__':

    Game().run()
