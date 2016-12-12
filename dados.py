__author__ = 'julio'
#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''Funcoes auxiliares:'''


def print_matriz(m):
    for l in range(len(m)):

        for c in range(len(m[l])):
            item = ""
            if m[l][c] == None:
                item += "B\t"
            else:
                item += str(m[l][c]) + "\t"
            if c == len(m[l]) - 1:
                item += "\n"
            print item,


'''
N-Rainhas - ANALISE DE DOMINIO

Num tabuleiro de xadres, temos uma matriz 8x8
com 8 LINHAS, 8 COLUNAS, VARIAS DIAGONAIS, Vamos chamar as LINHAS, COLUNAS e DIAGONAIS de Unidades,
pois a ideia do N-Rainhas eh prencher posições no tabuleiro dentro das unidades
de modo que nao quebre a restricao de nao repetir a rainha em cada
unidade. Portanto, teremos 27 Unidades no total (8 LINHAS, 8 COLUNAS e VARIAS DIAGONAIS)
'''

'''
DEFINICAO DOS DADOS:
----
Rainha eh Natural[1,8]
----

----
Tabuleiro eh uma Matriz[0..7, 0..7] de (Valor ou None)
interp. uma matriz 8x8 que representa um tabuleiro de xadrtes.
Cada posicao da lista pode conter um valor ou None caso ainda nao haja Rainha
na mesma unidade.
Uma matriz nada mais eh que uma lista de listas (ou vetor de vetores).

----

----
Posicao eh uma Tupla(0..7, 0..7)
interp. representa uma posicao no tabuleiro
----

----
Unidade eh uma Lista de Posicao de tamanho 8
interp. representa a posicao de cada quadrado em uma Unidade.
Ha 8 linhas, 8 colunas e varias diagonais
----

'''

''' Constantes e Exemplos: '''

# Definicao das Unidades e suas Posicões:

LINHAS = [[(l,c) for c in range(8)] for l in range(8)]
COLUNAS = [[(l,c) for l in range(8)] for c in range(9)]

UNIDADES = LINHAS + COLUNAS

#Exemplos de tabuleiros

N = None
TAB_VAZIO = [[None for _ in range(8)] for _ in range(8)]

'''

Rainha_um [0, 0]
========================================================================================================================

    0  1  2  3  4  5  6  7

 0  R  N  N  N  N  N  N  N
 1  N  N
 2  N     N
 3  N        N
 4  N           N
 5  N              N
 6  N                 N
 7  N                    N

 Rainha_resolvida
========================================================================================================================

     0   1   2   3   4   5   6   7

 0 | R | N | N | N | N | N | N | N
 1 | N | N | N | N | N | R | N | N
 2 | N | N | N | N | N | N | N | R
 3 | N | R | N | N | N | N | N | N
 4 | N | N | N | R | N | N | N | N
 5 | N | N | N | N | N | N | R | N
 6 | N | N | R | N | N | N | N | N
 7 | N | N | N | N | R | N | N | N

     '''