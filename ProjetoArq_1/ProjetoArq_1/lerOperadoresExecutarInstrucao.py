class LerOperadoresExecutarInstrucao:
    def lerOperadoresExecutarInstrucao(self, instrucoes):
        remaining_instructions = len(instrucoes) % 3
        if remaining_instructions != 0:
            instrucoes += [0] * (3 - remaining_instructions)

        grupos = []

        for i in range(0, len(instrucoes), 3):
            grupo = instrucoes[i:i+3]
            grupos.append(grupo)

        print(grupos)
        self.processarGrupo(grupo)
        # for grupo in grupos:
        #     self.processarGrupo(grupo)

    def processarGrupo(self, grupo):

        print("Processando grupos")
