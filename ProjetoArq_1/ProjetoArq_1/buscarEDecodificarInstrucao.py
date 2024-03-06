import struct

class BuscarEDecodificarInstrucao:
    def buscarEDecodificarInstrucao(self, arquivo):
        instrucoes = self.buscarInstrucao(arquivo)
        return self.decodificarInstrucao(instrucoes)

    def buscarInstrucao(self, arquivo):
        with open(arquivo, 'rb') as f:
            dados = f.read()
        instrucoes = struct.unpack(f'{len(dados)}B', dados)
        return instrucoes

    def decodificarInstrucao(self, instrucoes):
       
        print('=======================================')
        print('= Buscando e Decodificando Instruções =')
        print('=======================================')
        instrucoes_hex = [hex(instrucao) for instrucao in instrucoes]
        print(', '.join(instrucoes_hex))
        print('=======================================')
        return instrucoes_hex
