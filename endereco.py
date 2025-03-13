class Endereco:
    def __init__(self, estado, cidade, endereco, numero, bairro):
        self._estado = estado
        self._cidade = cidade
        self.__endereco = endereco
        self.__numero = numero
        self._bairro = bairro

    def get_estado(self):
        return self._estado

    def get_cidade(self):
        return self._cidade

    def get_endereco(self):
        return self.__endereco

    def get_numero(self):
        return self.__numero

    def get_bairro(self):
        return self._bairro

    def detalhes(self):
        print(f' Estado: {self._estado} \n Cidade: {self._cidade} \n '
              f'Endereco: {self.__endereco} \n Numero: {self.__numero} \n Bairro: {self._bairro}')
        print("-" * 50)

    def confirmar(self):
        if self._estado == 'AC':
            return self._estado
        elif self._estado == 'AL':
            return self._estado
        elif self._estado == 'AM':
            return self._estado
        elif self._estado == 'AP':
            return self._estado
        elif self._estado == 'BA':
            return self._estado
        elif self._estado == 'CE':
            return self._estado
        elif self._estado == 'DF':
            return self._estado
        elif self._estado == 'ES':
            return self._estado
        elif self._estado == 'GO':
            return self._estado
        elif self._estado == 'MA':
            return self._estado
        elif self._estado == 'MG':
            return self._estado
        elif self._estado == 'MS':
            return self._estado
        elif self._estado == 'MT':
            return self._estado
        elif self._estado == 'PA':
            return self._estado
        elif self._estado == 'PB':
            return self._estado
        elif self._estado == 'PE':
            return self._estado
        elif self._estado == 'PI':
            return self._estado
        elif self._estado == 'PR':
            return self._estado
        elif self._estado == 'RJ':
            return self._estado
        elif self._estado == 'RN':
            return self._estado
        elif self._estado == 'RS':
            return self._estado
        elif self._estado == 'RO':
            return self._estado
        elif self._estado == 'RR':
            return self._estado
        elif self._estado == 'SC':
            return self._estado
        elif self._estado == 'SE':
            return self._estado
        elif self._estado == 'SP':
            return self._estado
        elif self._estado == 'TO':
            return self._estado
        else:
            print(" * Escreva o estado como sigla, em letras maiúsculas. EX: SP *")


class Entrega(Endereco):
    def __init__(self, nome, cpf, telefone, estado, cidade, endereco, numero, bairro, cep, status=False):
        super().__init__(estado, cidade, endereco, numero, bairro)
        self.__nome = nome
        self.__cpf = cpf
        self._telefone = telefone
        self.__cep = cep
        self.frete = 1
        self.status = status

    def get_nome(self):
        return self.__nome

    def get_cpf(self):
        return self.__cpf

    def get_telefone(self):
        return self._telefone

    def get_cep(self):
        return self.__cep

    def set_status(self):
        if self.status:
            print("A entrega já foi concluída")
        else:
            self.status = True

    def detalhes(self):
        print(
            f' Nome completo: {self.__nome} \n CPF: {self.__cpf} \n Telefone: {self._telefone} \n Cidade: '
            f'{self.get_cidade()}      Estado: {self.get_estado()} \n Endereço: {self.get_endereco()}, '
            f'{self.get_numero()}\n Bairro: {self.get_bairro()}     CEP: {self.__cep} \n Frete: R${self.frete}'
            f'     Status: {self.status}')
        print("-" * 50)

    def calcular_frete(self):
        if self._estado == 'SP':
            self.frete = self.frete * 9
        elif self._estado == 'MG':
            self.frete = self.frete * 12
        elif self._estado == 'RJ':
            self.frete = self.frete * 12
        elif self._estado == 'ES':
            self.frete = self.frete * 12
        else:
            self.frete = self.frete * 15


end1 = Endereco('SP', 'Guararapes', 'R. Albino Gomes', '60', 'Francisco Antonioli')
end1.confirmar()
end1.detalhes()

end2 = Endereco('SP', 'Guararapes', 'R. Rui Barbosa', '850', 'Industrial')
end2.confirmar()
end2.detalhes()

ent1 = Entrega('Lorena Fernanda', '42026492816', '18981053517', 'SP', 'Guararapes',
               'R.Albino Gomes', '60', 'Francisco Antonioli', '16708-324')
ent1.confirmar()
ent1.calcular_frete()
ent1.detalhes()

ent2 = Entrega('Kalel Nikolai', '12345678910', '92996124567', 'AM', 'Manaus',
               'R. F', '14', 'Armando Mendes', '69089-246')

ent2.confirmar()
ent2.calcular_frete()
ent2.set_status()
ent2.detalhes()
