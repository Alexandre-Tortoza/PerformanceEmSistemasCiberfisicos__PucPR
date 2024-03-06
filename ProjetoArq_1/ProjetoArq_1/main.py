import sys
import os
from MemoriaCache import MemoriaCache
from buscarEDecodificarInstrucao import BuscarEDecodificarInstrucao
from lerOperadoresExecutarInstrucao import lerOperadoresExecutarInstrucao

CPU_DEBUG = True

registrador_cp = 0x01
registrador_ax = 0x02
registrador_bx = 0x03
registrador_cx = 0x04
registrador_dx = 0x05

flag_zero = False

#memoria = MemoriaCache('arquivos_memoria/mov_mov_add.bin')
#memoria = MemoriaCache('arquivos_memoria/inc_dec.bin')
#memoria = MemoriaCache('arquivos_memoria/todas_instrucoes.bin')
#memoria = MemoriaCache('arquivos_memoria/programa_simples.bin')
#memoria = MemoriaCache('arquivos_memoria/fibonacci_10.bin')

def dumpRegistradores():
    if CPU_DEBUG:
        print(f'CP[{registrador_cp:02X}] \
            AX[{registrador_ax:02X}]  \
            BX[{registrador_bx:02X}]  \
            CX[{registrador_cx:02X}]  \
            DX[{registrador_dx:02X}]  \
            ZF[{flag_zero}] ')









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

        #ULA
        ler_operadores = lerOperadoresExecutarInstrucao()  # Instantiate the class
        ler_operadores.lerOperadoresExecutarInstrucao(valores_instrucoes)  # Call the method on the instance

        # dumpRegistradores() 

        #Unidade de Controle
        # calcularProximaInstrucao(idInstrucao)

        #apenas para nao ficar em loop voce pode comentar a linha abaixo =)
        sys.stdin.read(1)
    
