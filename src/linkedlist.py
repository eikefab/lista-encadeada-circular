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
    
    def to_list(self):
        if self.is_empty():
            return []
        
        data = [self.primeiro]
        node = self.primeiro
        
        while node.prox is not None: 
            node = node.prox
            
            data.append(node)
        
        return data 
    
    def adicionar_membro(self, membro: Membro):
        if self.primeiro is None:
            self.primeiro = membro
            
            return
        
        node = self.primeiro
        
        while node.prox is not None:
            node = node.prox
        
        node.prox = membro
        
        self.tamanho += 1
        
    def proximo_responsavel(self):
        pass
                    
    def remover_membro(self, membro):
        pass
    
            
    