class Membro:
    
    def __init__(self, nome, email, prox = None):
        self.nome = nome
        self.email = email
        self.prox = prox

class ListaEncadeadaCircular:
    
    def __init__(self):
        self.primeiro = None
        self.tamanho = 0
    
    def __len__(self):
        return self.tamanho

    def is_empty(self):
        return self.tamanho == 0
    
    def to_list(self, show_as_circular = False):
        if self.is_empty():
            return []
        
        data = []
        node = self.primeiro
        
        for _ in range(len(self)):
            data.append(node)
            
            node = node.prox
        
        if show_as_circular:
            data.append(self.primeiro)
        
        return data
    
    def adicionar_membro(self, membro: Membro):
        self.tamanho += 1
        
        if self.primeiro is None:
            self.primeiro = membro
            self.primeiro.prox = membro
            
            return
        
        node = self.primeiro
        
        while node.prox != self.primeiro:
            node = node.prox
        
        node.prox = membro
        membro.prox = self.primeiro
        
    def proximo_responsavel(self):
        node = self.primeiro
        
        while node:
            print(node.nome)
            
            node = node.prox
        
    def remover_membro(self, membro):
        pass
    
            
    