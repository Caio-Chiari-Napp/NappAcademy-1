from BancoNapp.contas.Conta import Conta


class ContaPessoaJuridica(Conta):
    def __init__(self, **kwargs):
        super(ContaPessoaJuridica, self).__init__(**kwargs)
        """
        Construtor da classe PessoaFísica.
        Extrai do dicionário kwargs do correntista.
        """
        self.empresa = kwargs.get('empresa', '')
        self.limite = kwargs.get('limite', 1500)
        
        