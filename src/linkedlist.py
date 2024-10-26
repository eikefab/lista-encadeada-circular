class ListaVazia(Exception):
    pass

class MembroNaoExiste(Exception):
    pass

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
        if self.is_empty():
            raise ListaVazia("Impossível remover, a lista está vazia!")

        atual = self.primeiro
        anterior = None

        # percorrer a lista inteira, se encontrar ou acabar a lista, para
        ## O(N)
        while True:
            # encontrou
            if atual == membro:
                # se for unico, redefine a lista
                if self.tamanho == 1:
                    self.primeiro = None
                # nao é o unico
                else:
                    # remoção do membro
                    if anterior is None:  
                        self.primeiro = atual.prox
                    else:
                        anterior.prox = atual.prox

                    # linhas comentadas por enquanto, corrige o apontamento do ultimo para o primeiro caso estejamos removendo o ultimo
                    # if atual.prox is None:
                    #    anterior.prox = self.primeiro
                
                # reajusta tamanho e finaliza
                self.tamanho -= 1
                return

            # mantem sequencia
            anterior = atual
            atual = atual.prox
            
            # por ser circular, se o primeiro for igual o atual, voltamos ao inicio
            if atual == self.primeiro:
                break

        # saiu do loop sem encontrar
        raise MembroNaoExiste("Impossível remover, membro não existe!")
    
            
    