from rh.classes.Colaborador import Colaborador
from datetime import date

class Departamento:
    def __init__(self, nome_setor, nome, dia, mes, ano):
        self._nome_setor = nome_setor
        self.informar_responsavel(nome, dia, mes, ano)
        self._colaboradores = []

    @property
    def nome(self):
        return self._nome_setor
    
    @nome.setter
    def nome(self, value):
        self._nome_setor = value

    @property
    def responsavel(self):
        return self._responsavel

    @property
    def colaboradores(self):
        return self._colaboradores

    def informar_responsavel(self, nome, dia, mes, ano):
        self._responsavel = Colaborador(nome, dia, mes, ano)

    def add_colaborador(self, nome, dia, mes, ano):
        self._colaboradores.append(Colaborador(nome, dia, mes, ano))

    def verificar_aniversariantes(self):
        lista = []
        for colaborador in self.colaboradores:
            if colaborador.aniversario_hoje():
                lista.append((colaborador.nome, colaborador.aniversario, self._nome_setor))
        if self.responsavel.aniversario_hoje():
            lista.append((self.responsavel.nome, self.responsavel.aniversario, self._nome_setor))
        return lista

    def __str__(self):
        return self._nome_setor

    def __repr__(self):
        return 'Departamento = ' + self._nome_setor
