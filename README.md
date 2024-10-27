# Integrantes

João Henrique Barbosa Fernandes Alencar</br>
Eike Fabrício da Silva

# Conteúdo Consultado

* [RealPython](https://realpython.com/linked-lists-python/)
* [GeeksForGeeks](https://www.geeksforgeeks.org/python-linked-list/)

# Comentário da Equipe sobre realização

Tudo que foi requisitado foi feito.

# Possíveis problemas, dificuldades encontradas ou funcionalidades que deveriam ser implementadas

* Lidar com a lista circular de fato, uma vez que na inserção, por exemplo, usar um loop "até que o próximo nó seja nulo" seria infinito, vez que sempre esbarraria no ponteiro do primeiro, depois segundo e assim por diante, voltando para o primeiro. Mas uma vez que isso foi solucionado, o resto foi mais simples.
* Lidar com a remoção do *primeiro* nó, vez que teria de, além de removê-lo da rotação, fazer com que o item presente no 2o nó fosse o novo primeiro, e para isso, no último item, haveria de apontar pro segundo, não mais pro primeiro nó.
* A implementação acabou sendo **O(n)** ao adicionar e remover nós, caso necessário numa implementação futura, um "contém" também teria de ser O(n), sendo *n* o número de nós presentes.
