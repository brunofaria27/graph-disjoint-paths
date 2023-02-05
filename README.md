# Caminhos disjuntos em um grafo

O  problema  de  se  determinar  o  número  máximo  de  caminhos  disjuntos  em  arestas  existentes  em  um grafo  apresenta  várias  aplicações.  Neste repositório  você  encontrará  um  método  de  resolução  deste problema que receba um grafo e um par de vértices (isto é, origem e destino) exiba ao final a quantidade de caminhos  disjuntos  em  arestas  entre  os  dois  vértices  dados,  além  de  listar  cada  um  dos  caminhos encontrados.

--------------------

## Para rodar o código

Para rodar o código basta você criar um arquivo na pasta `Application`, com a seguinte estrutura:

```
número de vértices
x y
x z
.
.
.
z w
```

Vale ressaltar que `x`, `y`, `z` e `w` são números inteiros representando os vértices ligados entre si, criando assim uma aresta. Após criar o arquivo basta executar o código utilizando a seguinte linha de comando, já que você irá passar por parâmetros os valores que deseja para a aplicação funcionar.

```bash
python3 "<nome_arquivo_entre_aspas>" <vertice_origem> <vertice_destino>
```

Comando para testes dos programadores: `python .\application.py "grafo_test.txt" 0 5` 
