from linkedlist import *

def test():
    linked_list = ListaEncadeadaCircular()
    
    abel = Membro('Abel', 'abel@email.com')
    bia = Membro('Bia', 'carlos@email.com')
    carlos = Membro('Carlos', 'carlos@email.com')
    davi = Membro('Davi', 'davi@email.com')
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)
    linked_list.adicionar_membro(carlos)
    linked_list.adicionar_membro(davi)
    
    print([x.nome for x in linked_list.to_list()])
    
    linked_list.proximo_responsavel()
    linked_list.proximo_responsavel()
    linked_list.proximo_responsavel()
    
    print(linked_list.responsavel.nome)
    
    linked_list.remover_membro(carlos)
    
    print([x.nome for x in linked_list.to_list()])
    
    linked_list.proximo_responsavel()
    linked_list.proximo_responsavel()
    
    linked_list.remover_membro(abel)
    
    print(linked_list.responsavel.nome)
    
    linked_list.proximo_responsavel()
    linked_list.proximo_responsavel()
    linked_list.proximo_responsavel()
    linked_list.proximo_responsavel()
    linked_list.proximo_responsavel()
    
    print(linked_list.responsavel.nome)
    
    print([x.nome for x in linked_list.to_list()])
    
if __name__ == "__main__":
    test()