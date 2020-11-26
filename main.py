from boardgame import BoardGame, console_play
from boardgamegui import gui_play
from random import choice

class Threeinarow(BoardGame):

    def __init__(self, w: int, h: int):
        self._w, self._h = w, h
        self._board = [1] * self._w * self._h  #0: Bianco || 1: Grigio || 2: Nero
        self._fisse = (7, 14, 17, 21, 25, 28, 30, 31, 33 ) # Celle fisse
        for i in self._fisse:
            self._board[i] = choice((0,2)) #Valori Casuali assunti dalle celle fisse

    def cols(self) -> int:
        return self._w

    def rows(self) -> int:
        return self._h

    def message(self) -> str:
        return "Puzzle solved!"

    def value_at(self, x: int, y: int) -> str:
        b, w, h = self._board, self._w, self._h
        if 0 <= y < h and 0 <= x < w and b[y * w + x] > 0:
            if b[y * self._w + x] == 1: #Settaggio colori
                g2d.set_color((200,200,200))
                g2d.fill_rect((x*40, y*40, 39, 39))
            elif b[y * self._w + x] == 2:
                g2d.set_color((0,0,0))
                g2d.fill_rect((x*40, y*40, 39, 39))
            return str(b[y * w + x])
        return ""

    def play_at(self, x: int, y: int):
        w, h = self._w, self._h
        if 0 <= y < h and 0 <= x < w:
            b = self._board
            if not (y * self._w + x) in self._fisse: #Se fisse pass
                if b[y * self._w + x] == 0:
                    b[y * self._w + x] = 1
                elif b[y * self._w + x] == 1:
                    b[y * self._w + x] = 2
                elif b[y * self._w + x] == 2:
                    b[y * self._w + x] = 0
                                    
    def flag_at(self, x: int, y: int):
        pass

    def firstcond(self) -> bool:
        contgr = 0
        for i in range (len(self._board)):
            if self._board[i] != 1:
                contgr += 1
                if contgr == (self._w * self._h):                    
                    return True
                
    def secondcond(self) -> bool: #Controllo sulle colonne
        total = 0
        for k in range(self._w):
            cont0, cont2 = 0, 0
            for p in range(self._h):
                if self._board[p * self._h + k] == 0:
                    cont0 += 1
                elif self._board[p * self._h + k] == 2:
                    cont2 += 1    
            if cont0 == cont2:
                total += 1
        if total == self._w:
            return True 
        
    def thirdcond(self) -> bool:
        total = 0
        for y in range(self._w):
            cont0, cont2 = 0, 0
            for x in range(self._h):
                if self._board[y * self._h + x] == 0:
                    cont0 += 1
                elif self._board[y * self._h + x] == 2:
                    cont2 += 1    
            if cont0 == cont2:
                total += 1
        if total == self._w:
            return True 
        
    def fourthcond(self) -> bool: #Controllo sulle 3 contigue
         for q in range(self._h): 
            b, w, h = self._board, self._w, self._h
            for s in range(w):
                if s < (h - 2):
                    totale = b[q*w+s] + b[q*w+s+1] + b[q*w+s+2]
                    if (totale == 0) or (totale == 6): # se 0 + 0 + 0 = 0 o se 2 + 2 + 2 = 6
                        return False
                    else:
                        return True
        
        
        
    def finished(self) -> bool:
        if self.firstcond() and self.secondcond() and self.thirdcond() and self.fourthcond(): #Controllo 4 condizioni
            return True
            
            
            
def main():
    game = Threeinarow(6, 6)
    gui_play(game)
    ##console_play(game)

main()
