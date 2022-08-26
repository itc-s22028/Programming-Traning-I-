import random
import math
import time

class Ball:
    def __init__(self, canvas, color, paddle):
        self.canvas = canvas
        self.paddle = paddle

        self.count = 0

        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.init_x = self.canvas_width / 2 - 7.5
        self.init_y = self.canvas_height / 2 - 7.5
        self.speed = 0
        self.x = 0
        self.y = 0
        
    def start(self, evt):
        if self.speed != 0:
            return

        self.canvas.moveto(self.id, self.init_x, self.init_y)
        self.speed = 10
        
        self.canvas.create_text(250, 325, text="GAME START", font=("",40), fill="#fff", tag="text2")
        self.canvas.delete("text1")
        self.canvas.delete("score")
        self.canvas.delete("cl")
        self.canvas.delete("sc")
        self.count = 0
       
        angle = math.radians(random.choice(list(range(20, 65, 5))))
        direction = random.choice([1, -1])  
        self.x = math.cos(angle) * self.speed * direction
        self.y = math.sin(angle) * self.speed
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)

        pos = self.canvas.coords(self.id)

        if pos[0] <= 0:
            self.fix(pos[0] - 0, 0)
            
        if pos[1] <= 0:
            self.fix(0, pos[1])
            
        if pos[2] >= self.canvas_width:
            self.fix(pos[2] - self.canvas_width, 0)
           
        if pos[3] >= self.canvas_height:
            self.fix(0, pos[3] - self.canvas_height)
            self.failed()
            
            self.canvas.create_text(250, 325, text="GAME OVER", font=("",40), fill="#fff", tag="text1")
            self.canvas.delete("text2")
            self.canvas.delete("score")
            self.canvas.create_text(250, 230, text=self.count, font=("",40), fill="#fff", tag="score a")
            self.canvas.create_text(250, 190, text="SCORE", font=("",20), fill="#fff", tag="sc")

            
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] \
           and paddle_pos[1] <= pos[3] <= paddle_pos[3]:
                self.fix(0, pos[3] - paddle_pos[1])
                self.canvas.delete("text2")

                self.canvas.delete("score")
                self.count += 1
                self.canvas.create_text(250, 325, text=self.count, font=("",40), fill="#fff", tag="score")

                if self.count == 5:
                    self.canvas.delete("score")
                    self.canvas.create_text(250, 325, text="GAME CLEAR", font=("",40), fill="#fff", tag="cl")
                    self.failed()
                    
    def fix(self, diff_x, diff_y):
        self.canvas.move(self.id, -(diff_x * 2), -(diff_y * 2))

        if diff_x != 0:
            self.x = -self.x

            
        if diff_y != 0:
            self.y = -self.y

    def failed(self):
        self.x = 0
        self.y = 0
        self.speed = 0
