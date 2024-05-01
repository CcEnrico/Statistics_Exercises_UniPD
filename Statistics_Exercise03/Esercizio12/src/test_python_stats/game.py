import random

class PartitaScacchi:
    def __init__(self):
        self.scacchiera = [[0] * 12 for _ in range(20)]
        self.posizioni_pedine = [0] * 12
        
        for i in range(12):
            self.posizioni_pedine[i] = 0  
            self.scacchiera[0][i] = 1  
        
        self.mosse = 0
        self.win = False
    
    def lancioDadi(self):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        return dado1 + dado2
    
    def avanzaPedina(self, colonna):
        riga_attuale = self.posizioni_pedine[colonna]
        self.scacchiera[riga_attuale][colonna] = 0 
        
        if riga_attuale < 19:
            self.posizioni_pedine[colonna] += 1
            self.scacchiera[self.posizioni_pedine[colonna]][colonna] = 1  

    def check_win(self):
        for i in range(12):
            if self.posizioni_pedine[i] == 19:
                return True
        return False
    
    def winning_column(self):
        for i in range(12):
            if self.posizioni_pedine[i] == 19:
                return i
        return -1
    
    def get_mosse(self):
        return self.mosse
    
    def pedina_colonna_7_prima_di_8(self):
        if self.posizioni_pedine[6] > self.posizioni_pedine[7]:
            return True
        return False
        
    def pedina_colonna_k_prima_di_tutte_le_altre(self, k):
        for i in range(12):
            if i != k and self.posizioni_pedine[k] <= self.posizioni_pedine[i]:
                return False
        return True
    
    def check_mosse_200(self):
        return self.mosse <= 200
    
    def results(self):
        print("Numero di mosse:", self.mosse)
        print("Posizioni pedine:", self.posizioni_pedine)
        for riga in self.scacchiera:
            print(riga)
        
        print("Pedina in colonna 7 prima di colonna 8:", self.pedina_colonna_7_prima_di_8())
        for i in range(12):
            print("Pedina in colonna", i, "prima di tutte le altre:", self.pedina_colonna_k_prima_di_tutte_le_altre(i))
        
        print("Il gioco ha durata di esattamente N mosse con N compreso tra 0 e 200", self.check_mosse_200())
        print("Il gioco ha piu' di 200 mosse", not self.check_mosse_200())

    def play(self):
        while not self.win:
            somma_dadi = self.lancioDadi()
            colonna = somma_dadi - 1  
            self.avanzaPedina(colonna)
            self.mosse += 1

            self.win = self.check_win()

    def reset(self):
        self.scacchiera = [[0] * 12 for _ in range(20)]
        self.posizioni_pedine = [0] * 12
        
        for i in range(12):
            self.posizioni_pedine[i] = 0  
            self.scacchiera[0][i] = 1  
        
        self.mosse = 0
        self.win = False


