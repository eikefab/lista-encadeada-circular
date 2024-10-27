from linkedlist import *

abel = Membro("Abel", "abel@email.com")
bia = Membro("Bia", "carlos@email.com")
carlos = Membro("Carlos", "carlos@email.com")
davi = Membro("Davi", "davi@email.com")

def test_abel_abel():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    
    assert linked_list.responsavel, abel
    assert linked_list.to_list(), [abel]
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel, abel

def test_abel_bia_abel():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)
    
    assert linked_list.responsavel, abel
    assert linked_list.to_list(), [abel, bia]
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel, bia

    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel, abel


def test_abel_bia_carlos_abel():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)
    linked_list.adicionar_membro(carlos)
    
    assert linked_list.responsavel, abel
    assert linked_list.to_list(), [abel, bia, carlos]
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel, bia

    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel, carlos
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel, abel
    
def test_abel_bia_carlos_davi_abel():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)
    linked_list.adicionar_membro(carlos)
    linked_list.adicionar_membro(davi)
    
    assert linked_list.responsavel, abel
    assert linked_list.to_list(), [abel, bia, carlos, davi]
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel, bia

    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel, carlos
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel, davi
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel, abel

def test_error_remove():
    linked_list = ListaEncadeadaCircular()
    
    try:
        linked_list.remover_membro(abel)
        
        assert False, "Erro: Exceção não lançada para lista vazia."
    except Exception as e:
        assert str(e) == "A lista está vazia!", "Erro: Mensagem de erro inesperada"
        
    bruno = Membro("Bruno", "bruno@email.com")
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)
    linked_list.adicionar_membro(carlos)
    linked_list.adicionar_membro(davi)
    
    try:
        linked_list.remover_membro(bruno)
        
        assert False, "Erro: Exceção não lançada para elemento não existente."
    except Exception as e:
        assert str(e) == "Impossível remover, o membro não existe!", "Erro: Mensagem de erro inesperada"

def test_removes():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)
    linked_list.adicionar_membro(carlos)
    linked_list.adicionar_membro(davi)
    
    assert linked_list.to_list(), [abel, bia, carlos, davi]
    assert len(linked_list) == 4, "Erro: A lista apresenta tamanho diferente de 4"
    
    linked_list.remover_membro(abel)
    
    assert linked_list.to_list(), [bia, carlos, davi]
    assert len(linked_list) == 3, "Erro: A lista apresenta tamanho diferente de 3"
    
    linked_list.remover_membro(bia)
    
    assert linked_list.to_list(), [carlos, davi]
    assert len(linked_list) == 2, "Erro: A lista apresenta tamanho diferente de 2"
    
    linked_list.remover_membro(carlos)
    
    assert linked_list.to_list(), [davi]
    assert len(linked_list) == 1, "Erro: A lista apresenta tamanho diferente de 1"
    
    linked_list.remover_membro(davi)
    
    assert linked_list.to_list() == [], "Erro: A lista não está vazia!"
    assert len(linked_list) == 0, "Erro: A lista apresenta tamanho diferente de 0"
    
    try:
        linked_list.remover_membro(abel)
        
        assert False, "Erro: Exceção não lançada para lista vazia."
    except Exception as e:
        assert str(e) == "A lista está vazia!", "Erro: Mensagem de erro inesperada"
    
def test_remove_responsavel():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)
    linked_list.adicionar_membro(carlos)
    linked_list.adicionar_membro(davi)
    
    assert linked_list.responsavel, abel
    
    linked_list.remover_membro(abel)
    
    assert linked_list.responsavel, bia
    
    linked_list.remover_membro(bia)
    
    assert linked_list.responsavel, carlos
    
    linked_list.remover_membro(carlos)
    
    assert linked_list.responsavel, davi
    
    linked_list.remover_membro(davi)
    
    assert not linked_list.responsavel, "Erro: Ainda há algum responsável mesmo com a lista vazia"

def test_adiciona_roda_adiciona():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)

    assert linked_list.to_list(), [abel, bia]

    linked_list.proximo_responsavel()

    assert linked_list.responsavel, bia

    linked_list.adicionar_membro(carlos)

    assert linked_list.responsavel, bia

    linked_list.proximo_responsavel()

    assert linked_list.responsavel, carlos

    linked_list.proximo_responsavel()

    assert linked_list.responsavel, abel

def test():
    test_abel_abel()
    test_abel_bia_abel()
    test_abel_bia_carlos_abel()
    test_abel_bia_carlos_davi_abel()
    test_error_remove()
    test_removes()
    test_remove_responsavel()
    test_adiciona_roda_adiciona()
    
    print("Testes validados com sucesso.")
    
if __name__ == "__main__":
    test()