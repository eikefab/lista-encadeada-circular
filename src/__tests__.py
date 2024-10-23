from linkedlist import *

def test():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(Membro('Abel', 'abel@email.com'))
    linked_list.adicionar_membro(Membro('Bia', 'carlos@email.com'))
    linked_list.adicionar_membro(Membro('Carlos', 'carlos@email.com'))
    linked_list.adicionar_membro(Membro('Davi', 'davi@email.com'))
    
    for i in linked_list.to_list():
        print(f"{i.nome} - {i.email}", end=", ")
    
if __name__ == "__main__":
    test()