from models import Pessoas

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='JPai', idade=60)
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():
    pessoas = Pessoas.query.all()
    print(pessoas)
    pessoa = Pessoas.query.filter_by(nome='JPai').first()
    print(pessoa.idade)

# Altera dados na tabela pessoa
def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome='Antonio').first()
    pessoa.nome = 'Bryan'
    pessoa.save()

# Exclui dados na tabela pessoa
def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome='JPai').first()
    pessoa.delete()


if __name__ == '__main__':
    # insere_pessoas()
    # altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
