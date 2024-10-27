from linkedlist import *

def test():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(Membro('Abel', 'abel@email.com'))
    linked_list.adicionar_membro(Membro('Bia', 'carlos@email.com'))
    linked_list.adicionar_membro(Membro('Carlos', 'carlos@email.com'))
    linked_list.adicionar_membro(Membro('Davi', 'davi@email.com'))
    
    print([x.nome for x in linked_list.to_list()])
    
    
    linked_list.proximo_responsavel()
    
if __name__ == "__main__":
    test()