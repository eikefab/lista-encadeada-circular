class ListaVazia(Exception):
    pass

class MembroNaoExiste(Exception):
    pass

class Membro:
    
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.prox = None

class ListaEncadeadaCircular:
    
    def __init__(self):
        self.primeiro = None
        self.ultimo = None
        self.responsavel = None
        self.tamanho = 0
    
    def __len__(self):
        return self.tamanho

    def is_empty(self):
        '''
            Verdadeiro caso a variável TAMANHO esteja em 0.
        '''
        
        return self.tamanho == 0
    
    def to_list(self):
        '''
            O(N), sendo N a quantidade de nós. Retorna a lista encadeada numa array normal.
        '''
        
        if self.is_empty():
            return []
        
        data = []
        node = self.primeiro
        
        # Por ser circular, caso percorresse utilizando um 'while', ficaria num loop infinito e teriam de ser feitas verificações. Por armazenar o tamanho, fica cômodo utilizar um laço.
        for _ in range(len(self)):
            data.append(node)
            
            node = node.prox # Altera o cursor para o próximo
        
        return data
    
    def adicionar_membro(self, membro: Membro):
        '''
            O(1), sendo N a quantidade de nós até encontrar o próximo nó diferente da cabeça.
        '''
        
        self.tamanho += 1
        
        # Caso o item a ser adicionado seja o primeiro da lista
        if self.primeiro is None:
            self.primeiro = membro
            self.ultimo = membro
            self.responsavel = membro
            self.primeiro.prox = membro
            
            return
        
        self.ultimo.prox = membro
        membro.prox = self.primeiro
        
        self.ultimo = membro
    
    def proximo_responsavel(self):
        '''
            Avança com o cursor de responsável.
        
            O(1) pois não precisa percorrer nada, uma vez que os membros já foram adicionados de maneira circular.
            
            Ex.:
                Abel -> Bia -> Carlos -> Davi -> Abel
            
            Ao chegar em "Davi" e a função ser chamada novamente, o ponteiro da variável responsável é apontado de volta para Abel, que possui toda
            a estrutura da lista encadeada armazenada em si, mantendo a ordem e circularidade da lista encadeada.
        '''
        
        if self.is_empty():
            raise ListaVazia("A lista está vazia!")
        
        self.responsavel = self.responsavel.prox
        
    def remover_membro(self, membro: Membro):
        '''
            O(N), sendo N o número de nós.
            
            Remove o membro, disparando excecções caso não o encontre ou a lista esteja vazia.
        '''
        
        if self.is_empty():
            raise ListaVazia("A lista está vazia!")
        
        if membro == self.responsavel:
            self.proximo_responsavel()
        
        if membro == self.primeiro: # Caso o item a ser removido seja o primeiro nó.
            if self.tamanho == 1: # Caso haja apenas um nó na lista, invalida os dados (equivalente ao __init__).
                self.primeiro = None
                self.responsavel = None
                self.tamanho = 0

                return
            
            node = self.primeiro
            
            while node.prox != self.primeiro: # Busca o penúltimo ponteiro
                node = node.prox
            
            node.prox = membro.prox # Aponta o penúltimo ponteiro para o antes 2o, agora primeiro nó da lista.
            self.primeiro = membro.prox
            
            self.tamanho -= 1
            
            return
        
        node = self.primeiro
        anterior = None
        
        for _ in range(len(self)):
            if membro == node:
                anterior.prox = membro.prox # Dá um "shift" no membro atual, removendo ele da lista ao indicar que o nó anterior aponta para seu próximo e não mais ele.
                self.tamanho -= 1

                return
            
            anterior = node
            node = node.prox
        
        raise MembroNaoExiste("Impossível remover, o membro não existe!")
