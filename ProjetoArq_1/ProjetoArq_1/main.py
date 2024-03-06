import sys
import os
from MemoriaCache import MemoriaCache
from buscarEDecodificarInstrucao import BuscarEDecodificarInstrucao
from lerOperadoresExecutarInstrucao import LerOperadoresExecutarInstrucao



if __name__ == '__main__':
    while (True):
        os.system('cls')
        print('============================')
        print('=  Qual Arquivo desesja ?  =')
        print('=--------------------------=')
        print('= [1] Mov Mov Add          =')
        print('= [2] fibonacci            =')
        print('= [3] Inc Dec              =')
        print('= [4] Programa Simples     =')
        print('= [5] Todas Instrucoes     =')
        print('= [6] Inserir Comandos     =')
        print('============================')
        
        while True:
            arquivo = input("opção: ")
            if arquivo == '1':
                arquivo = 'arquivos_memoria/mov_mov_add.bin'
                break
            elif arquivo == '2':
                arquivo = 'arquivos_memoria/fibonacci_10.bin' 
                break
            elif arquivo == '3':
                arquivo = 'arquivos_memoria/inc_dec.bin'  
                break
            elif arquivo == '4':
                arquivo = 'arquivos_memoria/programa_simples.bin'  
                break
            elif arquivo == '5':
                arquivo = 'arquivos_memoria/todas_instrucoes.bin'  
                break
            elif arquivo == '6':
                print('Desculpe, em Desenvolvimento, escolha outra opção:')
            else: 
                print()
                print('Escolha uma opção valida')
        os.system('cls')    

        #Unidade de Controle
        decoder = BuscarEDecodificarInstrucao()
        valores_instrucoes = decoder.buscarEDecodificarInstrucao(arquivo)

        #ULA e Unidade de Controle
        ler_operadores = LerOperadoresExecutarInstrucao()
        ler_operadores.lerOperadoresExecutarInstrucao(valores_instrucoes)

        #apenas para nao ficar em loop voce pode comentar a linha abaixo =)
        sys.stdin.read(1)
    
