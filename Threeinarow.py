from boardgame import BoardGame, console_play
from boardgamegui import gui_play
from random import choice, randint
import g2d

class Threeinarow(BoardGame):

    def __init__(self, w: int, h: int):
        self._w, self._h = w, h
        self._board = [1] * self._w * self._h  #0: Bianco || 1: Grigio || 2: Nero

        with open("config.csv", "r") as f:
            first_line = f.readline()
            print(first_line)

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

    def automatism(self):      
        for q in range(self._h):  #Automatismo 2 Celle Contigue Righe
            b, w, h = self._board, self._w, self._h
            for s in range(w):
                if s < (h - 2):
                    totale = b[q*w+s] + b[q*w+s+1]
                    if totale == 0: # se 0 + 0 = 0 o se 2 + 2 = 4
                        if ((q*w+s-1) not in self._fisse) and ((q*w+s+2) not in self._fisse):
                            if (b[q*w+s-1] == 1):
                                b[q*w+s-1] = 2
                            if (b[q*w+s+2] == 1):
                                b[q*w+s+2] = 2
                    elif totale == 4:
                        if ((q*w+s-1) not in self._fisse) and ((q*w+s+2) not in self._fisse):
                            if (b[q*w+s-1] == 1):
                                b[q*w+s-1] = 0
                            if (b[q*w+s+2] == 1):
                                b[q*w+s+2] = 0

        for t in range(self._h):  #Automatismo 2 Celle Contigue Colonne
            b, w, h = self._board, self._w, self._h
            for c in range(w):
                if ((c*w+t-6) not in self._fisse) and ((c*w+t+12) not in self._fisse):                   
                    if (c*w+t+6) <= (len(self._board)-1):
                        totale = b[c*w+t] + b[c*w+t+6]
                        if totale == 0: # se 0 + 0 = 0 o se 2 + 2 = 4
                            if (c*w+t-6) >= 0 and b[c*w+t-6] == 1:
                                b[c*w+t-6] = 2
                            if (c*w+t+12) <= (len(self._board)-1) and b[c*w+t+12] == 1:
                                b[c*w+t+12] = 2
                        elif totale == 4:                            
                            if (c*w+t-6) >= 0 and b[c*w+t-6] == 1:
                                b[c*w+t-6] = 0
                            if (c*w+t+12) <= (len(self._board)-1) and b[c*w+t+12] == 1:
                                b[c*w+t+12] = 0

        list1 = []
        for k in range(self._w): #Automatismo Colonne
            cont0, cont2 = 0, 0
            list1 = []
            for p in range(self._h):
                if self._board[p * self._h + k] == 0:
                    cont0 += 1
                elif self._board[p * self._h + k] == 1:
                    list1.append(p * self._h + k)
                elif self._board[p * self._h + k] == 2:
                    cont2 += 1    
            if cont0 == 3 and cont2 == 0:
                self._board[list1[0]] = 2
                self._board[list1[1]] = 2
                self._board[list1[2]] = 2 

            elif cont0 == 3 and cont2 == 1:
                self._board[list1[0]] = 2
                self._board[list1[1]] = 2

            elif cont0 == 3 and cont2 == 2:
                self._board[list1[0]] = 2

            elif cont0 == 0 and cont2 == 3:
                self._board[list1[0]] = 0
                self._board[list1[1]] = 0
                self._board[list1[2]] = 0

            elif cont0 == 1 and cont2 == 3:
                self._board[list1[0]] = 0
                self._board[list1[1]] = 0

            elif cont0 == 2 and cont2 == 3:
                self._board[list1[0]] = 0


        list2 = []
        for z in range(self._w): #Automatismo Righe
            cont0, cont2 = 0, 0
            list2 = []
            for w in range(self._h):
                if self._board[z * self._h + w] == 0:
                    cont0 += 1
                elif self._board[z * self._h + w] == 1:
                    list2.append(z * self._h + w)
                elif self._board[z * self._h + w] == 2:
                    cont2 += 1    
            if cont0 == 3 and cont2 == 0:
                self._board[list2[0]] = 2
                self._board[list2[1]] = 2
                self._board[list2[2]] = 2 

            elif cont0 == 3 and cont2 == 1:
                self._board[list2[0]] = 2
                self._board[list2[1]] = 2

            elif cont0 == 3 and cont2 == 2:
                self._board[list2[0]] = 2

            elif cont0 == 0 and cont2 == 3:
                self._board[list2[0]] = 0
                self._board[list2[1]] = 0
                self._board[list2[2]] = 0

            elif cont0 == 1 and cont2 == 3:
                self._board[list2[0]] = 0
                self._board[list2[1]] = 0

            elif cont0 == 2 and cont2 == 3:
                self._board[list2[0]] = 0




    def unsolvable(self) -> bool:
        for y in range(self._w):
            cont0, cont2 = 0, 0
            for x in range(self._h):
                if self._board[y * self._h + x] == 0:
                    cont0 += 1
                elif self._board[y * self._h + x] == 2:
                    cont2 += 1    
            if cont0 > 3 or cont2>3:
                return True

        for k in range(self._w):
            cont0_, cont2_ = 0, 0
            for p in range(self._h):
                if self._board[p * self._h + k] == 0:
                    cont0_ += 1
                elif self._board[p * self._h + k] == 2:
                    cont2_ += 1    
            if cont0_ > 3 or cont2_ > 3:
                return True

        for q in range(self._h): 
            b, w, h = self._board, self._w, self._h
            for s in range(w):
                if s < (h - 2):
                    totale = b[q*w+s] + b[q*w+s+1] + b[q*w+s+2]
                    if (totale == 0) or (totale == 6): # se 0 + 0 + 0 = 0 o se 2 + 2 + 2 = 6
                        return True

        for m in range(self._h):
            b, w= self._board, self._w
            for n in range(w):
                if (n*w+m+6) > len(self._board) or (n*w+m+12) > len(self._board):
                    return False
                totale = b[n*w+m] + b[n*w+m+6] + b[n*w+m+12]
                if (totale == 0) or (totale == 6):  # se 0 + 0 + 0 = 0 o se 2 + 2 + 2 = 6
                    return True
                else:
                    return False


        for i in range (len(self._board)):
            if self._board[i] == 1:
                return False


    def hint(self):
        n = randint(0, len(self._board)-1) #Numero casuale per dare il suggerimento
        while (n in self._fisse) or (self._board[n] != 1):
            n = randint(0, len(self._board)-1)
        new_board = self._board[:]
        self._board[n] = 2
        for _ in range (1000): #Valore Arbitrario, dopo 1000 automatism sicuramente avrà terminato la board
            self.automatism()
        if self.unsolvable():
            new_board[n] = 0
        else:
            new_board[n] = 2

        self._board = new_board[:]

        
        
    def backtracking_recursive(self, i: int) -> bool:
        while i < len(self._board) and self._board[i] != 1:
            i += 1
        if i < len(self._board):
            saved = self._board[:]
            for color in (0, 2):
                self._board[i] = color
                if self.backtracking_recursive(i + 1):
                    return True
                self._board = saved
        return self.finished()


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

    
    def fifthcond(self) -> bool:
            for t in range(self._h): 
                b, w = self._board, self._w
                for c in range(w):
                    if (c*w+t+12) < len(self._board):                           
                        totale = b[c*w+t] + b[c*w+t+6] + b[c*w+t+12]
                        if (totale == 0) or (totale == 6):
                            return False
                        else:
                            return True
        
        
    def finished(self) -> bool:
        return self.firstcond() and self.secondcond() and self.thirdcond() and self.fourthcond() and self.fifthcond() #Controllo 5 condizioni
           
