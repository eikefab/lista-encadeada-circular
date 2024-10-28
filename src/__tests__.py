from linkedlist import *

abel = Membro("Abel", "abel@email.com")
bia = Membro("Bia", "carlos@email.com")
carlos = Membro("Carlos", "carlos@email.com")
davi = Membro("Davi", "davi@email.com")

def test_abel_abel():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    
    assert linked_list.responsavel == abel, "Erro: Esperado responsável Abel"
    assert linked_list.to_list() == [abel], "Erro: Esperando lista [Abel]"
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel == abel, "Erro: Esperado responsável Abel"

def test_abel_bia_abel():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)
    
    assert linked_list.responsavel == abel, "Erro: Esperado responsável Abel"
    assert linked_list.to_list() == [abel, bia], "Erro: Esperado lista [Abel, Bia]"
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel == bia, "Erro: Esperado responsável Bia"

    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel == abel, "Erro: Esperado responsável Abel"

def test_abel_bia_carlos_abel():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)
    linked_list.adicionar_membro(carlos)
    
    assert linked_list.responsavel == abel, "Erro: Esperado responsável Abel"
    assert linked_list.to_list() == [abel, bia, carlos], "Erro: Esperado lista [Abel, Bia, Carlos]"
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel == bia, "Erro: Esperado responsável Bia"

    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel == carlos, "Erro: Esperado responsável Carlos"
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel == abel, "Erro: Esperado responsável Abel"
    
def test_abel_bia_carlos_davi_abel():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)
    linked_list.adicionar_membro(carlos)
    linked_list.adicionar_membro(davi)
    
    assert linked_list.responsavel == abel, "Erro: Esperado responsável Abel"
    assert linked_list.to_list() == [abel, bia, carlos, davi], "Erro: Esperado lista [Abel, Bia, Carlos, Davi]"
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel == bia, "Erro: Esperado responsável Bia"

    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel == carlos, "Erro: Esperado responsável Carlos"
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel == davi, "Erro: Esperado responsável Davi"
    
    linked_list.proximo_responsavel()
    
    assert linked_list.responsavel == abel, "Erro: Esperado responsável Abel"

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
    
    assert linked_list.to_list() == [abel, bia, carlos, davi], "Erro: A lista deveria ser [Abel, Bia, Carlos, Davi]"
    assert len(linked_list) == 4, "Erro: A lista apresenta tamanho diferente de 4"
    
    linked_list.remover_membro(abel)
    
    assert linked_list.to_list() == [bia, carlos, davi], "Erro: A lista deveria ser [Bia, Carlos, Davi]"
    assert len(linked_list) == 3, "Erro: A lista apresenta tamanho diferente de 3"
    
    linked_list.remover_membro(bia)
    
    assert linked_list.to_list() == [carlos, davi], "Erro: A lista deveria ser [Carlos, Davi]"
    assert len(linked_list) == 2, "Erro: A lista apresenta tamanho diferente de 2"
    
    linked_list.remover_membro(carlos)
    
    assert linked_list.to_list() == [davi], "Erro: A lista deveria ser: [Davi]"
    assert len(linked_list) == 1, "Erro: A lista apresenta tamanho diferente de 1"
    
    linked_list.remover_membro(davi)
    
    assert linked_list.to_list() == [], "Erro: A lista não está vazia!"
    assert len(linked_list) == 0, "Erro: A lista apresenta tamanho diferente de 0"
    
    try:
        linked_list.remover_membro(abel)
        
        assert False, "Erro: Exceção não lançada para lista vazia."
    except Exception as e:
        assert str(e) == "A lista está vazia!", "Erro: Mensagem de erro inesperada"
        
    assert len(linked_list) == 0, "Erro: A lista apresenta tamanho diferente de 0"
    
def test_remove_responsavel():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)
    linked_list.adicionar_membro(carlos)
    linked_list.adicionar_membro(davi)
    
    assert linked_list.responsavel == abel, "Erro, esperado responsável: Abel"
    
    linked_list.remover_membro(abel)
    
    assert linked_list.responsavel == bia, "Erro, esperado responsável: Bia"
    
    linked_list.remover_membro(bia)
    
    assert linked_list.responsavel == carlos, "Erro, esperado responsável: Carlos"
    
    linked_list.remover_membro(carlos)
    
    assert linked_list.responsavel == davi, "Erro, esperado responsável: Davi"
    
    linked_list.remover_membro(davi)
    
    assert not linked_list.responsavel, "Erro: Ainda há algum responsável mesmo com a lista vazia"

def test_adiciona_roda_adiciona():
    linked_list = ListaEncadeadaCircular()
    
    linked_list.adicionar_membro(abel)
    linked_list.adicionar_membro(bia)

    assert linked_list.to_list() == [abel, bia], "Erro, esperado: [Abel, Bia]"

    linked_list.proximo_responsavel()

    assert linked_list.responsavel == bia, "Erro, esperado responsável: Bia"

    linked_list.adicionar_membro(carlos)

    assert linked_list.responsavel == bia, "Erro, esperado responsável: Bia"

    linked_list.proximo_responsavel()

    assert linked_list.responsavel == carlos, "Erro, esperado responsável: Carlos"

    linked_list.proximo_responsavel()

    assert linked_list.responsavel == abel, "Erro, esperado responsável: Abel"

def test_prox_responsavel_vazio():
    linked_list = ListaEncadeadaCircular()
    
    try:
        linked_list.proximo_responsavel()
        
        assert False, "Erro: Exceção não lançada para lista vazia."
    except Exception as e:
        assert str(e) == "A lista está vazia!", "Erro: Mensagem de erro inesperada"

def test():
    test_abel_abel()
    test_abel_bia_abel()
    test_abel_bia_carlos_abel()
    test_abel_bia_carlos_davi_abel()
    test_error_remove()
    test_removes()
    test_remove_responsavel()
    test_adiciona_roda_adiciona()
    test_prox_responsavel_vazio()
    
    print("Testes validados com sucesso.")
    
if __name__ == "__main__":
    test()