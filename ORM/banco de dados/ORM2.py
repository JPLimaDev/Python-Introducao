from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ORM import Pessoa

def RetornaSession():
    USUARIO = "root"
    SENHA = ""
    HOST = "localhost"
    BANCO = "aulapythonfull"
    PORT = "3306"

    CONN = f"mysql+pymysql://{USUARIO}:{SENHA}@{HOST}:{PORT}/{BANCO}"
    #Criação da configuraçãa do banco de dados pela string de conexão

    engine = create_engine(CONN, echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    return session



session = RetornaSession()

x = Pessoa(nome = "joao",
            usuario = "joao123",
            senha = "123456")

y = Pessoa(nome = "joao",
            usuario = "matheus",
            senha = "1234")


'''#Insere dados na Tabela Pessoa
session.add_all([x,y]) #Adiciona vários objetos na sessão
session.rollback() #Desfaz a transação no banco de dados
print(session.new) #Mostra os objetos novos na sessão
session.commit() #Confirma a transação no banco de dados
'''

#Consulta na Tabela Pessoa com filtro
'''x = session.query(Pessoa).filter(Pessoa.nome == "joao").filter(Pessoa.senha == "1234").all()
for pessoa in x:
    print(pessoa.id)'''