"""
"""

from models import Pessoas


def insere_pessoas():
    """Insere dados na tabela pessoa"""
    pessoa = Pessoas(nome='Felipe', idade='40')
    pessoa.save()


def consulta_pessoas():
    """Consulta os dados da tabela"""
    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    print(pessoa.idade)


def altera_pessoa():
    """Altera os dados na tabela"""
    pessoa = Pessoas.query.filter_by(nome='Douglas').first()
    pessoa.idade = 21
    pessoa.save()


def exclui_pessoa():
    """Exclui a pessoa da tabela"""
    pessoa = Pessoas.query.filter_by(nome='Felipe').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
    
    