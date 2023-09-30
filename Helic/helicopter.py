# 🚁
from utils import randcell
import os

class Helicopter:
    def __init__(self, w, h):
        rc = randcell(w, h)
        rx, ry = rc[0], rc[1]
        self.x = rx
        self.y = ry
        self.h = h
        self.w = w
        self.maxtank = 1
        self.tank = 0
        self.score = 0
        self.lives = 20

        
      

    def move(self, dx, dy):
        mx, my = dx + self.x, dy + self.y
        if (mx >= 0 and my >= 0 and mx < self.h and my < self.w):
            self.x, self.y = mx, my

    def print_menu(self):
        print('🛢️ ', self.tank, '/', self.maxtank, sep='', end=' | ')
        print('🏆', self.score, end=' | ')
        print('🧡', self.lives)        
    
    def game_over(self):
        os.system("cls")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
        print("X                                X")
        print("X  GAME OVER, YOUR SCORE IS", self.score, " X")
        print("X                                X")
        print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")            
        exit(0)

    def export_data(self):
        return{"score": self.score,
                "lives": self.lives,
                "x": self.x, "y": self.y,
                "tank": self.tank, "maxtank": self.maxtank}

    def import_data(self, data):
          self.x = data["x"] or 0
          self.y = data["y"] or 0
          self.lives = data["lives"] or 3
          self.tank = data["tank"] or 0
          self.score = data["score"] or 0
          self.maxtank = data["maxtank"] or 1