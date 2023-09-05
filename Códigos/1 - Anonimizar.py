import pandas as pd
import random

nomes_brasileiros = ["Ana", "José", "Maria", "Paulo", "Fernanda", "Carlos", "Mariana", "Luiz", "Camila", "Ricardo",
                     "Amanda", "Marcos", "Beatriz", "Pedro", "Isabela", "Rodrigo", "Giovanna", "Felipe", "Juliana",
                     "Lucas", "Larissa", "Gabriel", "Luisa", "Rafael", "Gabriela", "Bruno", "Carolina", "Thiago",
                     "Natália", "André", "Tatiana", "Diego", "Raquel", "Leandro", "Laura", "Raul", "Clara", "Renato",
                     "Vitória", "Vinícius", "Monica", "Cesar", "Mara", "Renan", "Luana", "Luciano", "Bianca",
                     "Eduardo", "Cristina", "Feliciano", "Patrícia", "Davi", "Flávia", "Tiago", "Suzana", "Gustavo",
                     "Teresa", "Luan", "Júlia", "Roberto", "Elaine", "Marcelo", "Mônica", "Thales", "Aline", "Henrique",
                     "Aurora", "Vitor", "Vanessa", "Glauber", "Cláudia", "Renan", "Rafaela", "João", "Renata", "Leonardo",
                     "Carla", "Fábio", "Silvana", "Lucas", "Simone", "Caio", "Letícia", "Rogério", "Tainá", "Emanuel",
                     "Bruna", "Gustavo", "Andressa", "Alexandre", "Lívia", "Ricardo", "Mirella", "Felipe", "Patrícia"]

sobrenomes_brasileiros = ["Silva", "Santos", "Oliveira", "Souza", "Pereira", "Ferreira", "Alves", "Ribeiro", "Carvalho",
                         "Gomes", "Martins", "Rodrigues", "Lima", "Costa", "Sousa", "Barbosa", "Pinto", "Araújo", "Melo",
                         "Azevedo", "Cavalcanti", "Fernandes", "Monteiro", "Teixeira", "Correia", "Mendes", "Nascimento",
                         "Freitas", "Moura", "Borges", "Vieira", "Cardoso", "Lopes", "Marques", "Dias", "Castro", "Cunha",
                         "Meireles", "Rocha", "Nunes", "Saraiva", "Farias", "Peixoto", "Machado", "Bezerra", "Siqueira",
                         "Moraes", "Gonçalves", "Duarte", "Campos", "Tavares", "Guerreiro", "Reis", "Vasconcelos", "Aragão",
                         "Cordeiro", "Leal", "Figueiredo", "Barros", "Aguiar", "Xavier", "Lacerda", "Cavalcante", "Bittencourt",
                         "Fonseca", "Araujo", "Pires", "Paiva", "Macedo", "Peixoto", "Cordeiro", "Leal", "Figueiredo", "Barros",
                         "Aguiar", "Xavier", "Lacerda", "Cavalcante", "Bittencourt", "Fonseca", "Araujo", "Pires", "Paiva",
                         "Macedo"]

global dicionarioPaciente
dicionarioPaciente = {}
global dicionarioCirurgiao
dicionarioCirurgiao = {}
global dicionarioAnestesista
dicionarioAnestesista = {}


# ... (seu código anterior) ...

def anonimizarPaciente(df):
    global dicionarioPaciente
    novoDicionario = {}

    # Criar um dicionário apenas com valores não vazios em 'ATENDIMENTO'
    for i in df['Ocorrencia'].unique():
        if not pd.isna(i) and i not in dicionarioPaciente:
            novoDicionario[i] = ""

    for i in novoDicionario:
        nomeCompleto = ""
        do = 0
        while nomeCompleto in novoDicionario.values() or do == 0:
            do = 1
            nomeCompleto = ""
            nome1 = random.choice(nomes_brasileiros)
            nomeCompleto += nome1 + " "

            if random.randrange(100) < 24:
                nome2 = random.choice(nomes_brasileiros)
                while nome2 == nome1:
                    nome2 = random.choice(nomes_brasileiros)
                nomeCompleto += nome2 + " "

            sobrenome1 = random.choice(sobrenomes_brasileiros)
            nomeCompleto += sobrenome1 + " "

            sobrenome2 = random.choice(sobrenomes_brasileiros)
            while sobrenome2 == sobrenome1:
                sobrenome2 = random.choice(sobrenomes_brasileiros)
            nomeCompleto += sobrenome2
        novoDicionario[i] = nomeCompleto
    dicionarioPaciente.update(novoDicionario)

    for index, row in df.iterrows():
        if not pd.isna(row['Ocorrencia']):
            df.at[index, 'Nome do paciente'] = dicionarioPaciente[
                row['Ocorrencia']]  # TROCAR 'NOME' E 'ID' PELAS COLUNAS NA DB

    return df


def anonimizarCirurgiao(df):
    global dicionarioCirurgiao
    novoDicionario = {}

    # Criar um dicionário apenas com valores não vazios em 'CIRURGIAO'
    for i in df['Nome do cirurgiao'].unique():
        if not pd.isna(i) and i not in dicionarioCirurgiao:
            novoDicionario[i] = ""

    for i in novoDicionario:
        nomeCompleto = ""
        do = 0
        while nomeCompleto in novoDicionario.values() or do == 0:
            do = 1
            nomeCompleto = ""
            nome1 = random.choice(nomes_brasileiros)
            nomeCompleto += nome1 + " "

            if random.randrange(100) < 24:
                nome2 = random.choice(nomes_brasileiros)
                while nome2 == nome1:
                    nome2 = random.choice(nomes_brasileiros)
                nomeCompleto += nome2 + " "

            sobrenome1 = random.choice(sobrenomes_brasileiros)
            nomeCompleto += sobrenome1 + " "

            sobrenome2 = random.choice(sobrenomes_brasileiros)
            while sobrenome2 == sobrenome1:
                sobrenome2 = random.choice(sobrenomes_brasileiros)
            nomeCompleto += sobrenome2
        novoDicionario[i] = nomeCompleto
    dicionarioCirurgiao.update(novoDicionario)

    for index, row in df.iterrows():
        if not pd.isna(row['Nome do cirurgiao']):
            df.at[index, 'Nome do cirurgiao'] = dicionarioCirurgiao[
                row['Nome do cirurgiao']]  # TROCAR 'NOME' E 'ID' PELAS COLUNAS NA DB

    return df


def anonimizarAnestesista(df):
    global dicionarioAnestesista
    novoDicionario = {}

    # Criar um dicionário apenas com valores não vazios em 'ANESTESISTA'
    for i in df['Nome do anestesista'].unique():
        if not pd.isna(i) and i not in dicionarioAnestesista:
            novoDicionario[i] = ""

    for i in novoDicionario:
        nomeCompleto = ""
        do = 0
        while nomeCompleto in novoDicionario.values() or do == 0:
            do = 1
            nomeCompleto = ""
            nome1 = random.choice(nomes_brasileiros)
            nomeCompleto += nome1 + " "

            if random.randrange(100) < 24:
                nome2 = random.choice(nomes_brasileiros)
                while nome2 == nome1:
                    nome2 = random.choice(nomes_brasileiros)
                nomeCompleto += nome2 + " "

            sobrenome1 = random.choice(sobrenomes_brasileiros)
            nomeCompleto += sobrenome1 + " "

            sobrenome2 = random.choice(sobrenomes_brasileiros)
            while sobrenome2 == sobrenome1:
                sobrenome2 = random.choice(sobrenomes_brasileiros)
            nomeCompleto += sobrenome2
        novoDicionario[i] = nomeCompleto
    dicionarioAnestesista.update(novoDicionario)

    for index, row in df.iterrows():
        if not pd.isna(row['Nome do anestesista']):
            df.at[index, 'Nome do anestesista'] = dicionarioAnestesista[
                row['Nome do anestesista']]  # TROCAR 'NOME' E 'ID' PELAS COLUNAS NA DB

    return df


def anonimizar(excel):
    excel = anonimizarPaciente(excel)
    excel = anonimizarCirurgiao(excel)
    return anonimizarAnestesista(excel)

# 2020

db15_19 = "C:/Users/agentes/Documents/Projeto HUC/dataset/datasets merged/jan2015_nov2019/dataset_final.xlsx"
df = pd.read_excel(db15_19)
df_anonimizado = anonimizar(df)
df_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/dataset_final_anonimizado.xlsx", index=False)
#
# db21 = "C:/Users/agentes/Documents/Projeto HUC/dataset/bds_2020_a_2022/db_2021.xlsx"
# df21 = pd.read_excel(db21)
# df21_anonimizado = anonimizar(df21)
# df21_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2021/bd2021_anonimizada.xlsx", index=False)
#
# db22 = "C:/Users/agentes/Documents/Projeto HUC/dataset/bds_2020_a_2022/db_2022.xlsx"
# df22 = pd.read_excel(db22)
# df22_anonimizado = anonimizar(df22)
# df22_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2022/bd2022_anonimizada.xlsx", index=False)
#


# 2015
# dbj15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Janeiro.csv"
# dbf15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Fevereiro.csv"
# dbm15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Março.csv"
# dba15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Abril.csv"
# dbma15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Maio.csv"
# dbjn15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Junho.csv"
# dbjl15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Julho.csv"
# dbag15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Agosto.csv"
# dbs15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Setembro.csv"
# dbo15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Outubro.csv"
# dbn15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Novembro.csv"
# dbd15 = "C:/Users/agentes/Documents/Projeto HUC/dataset/Cirurgias Realizadas - Hospitalar/2015/1.Dezembro.csv"
#
# dfj15 = pd.read_csv(dbj15)
# dff15 = pd.read_csv(dbf15)
# dfm15 = pd.read_csv(dbm15)
# dfa15 = pd.read_csv(dba15)
# dfma15 = pd.read_csv(dbma15)
# dfjn15 = pd.read_csv(dbjn15)
# dfjl15 = pd.read_csv(dbjl15)
# dfag15 = pd.read_csv(dbag15)
# dfs15 = pd.read_csv(dbs15)
# dfo15 = pd.read_csv(dbo15)
# dfn15 = pd.read_csv(dbn15)
# dfd15 = pd.read_csv(dbd15)
#
# dfj15_anonimizado = anonimizar(dfj15)
# dff15_anonimizado = anonimizar(dff15)
# dfm15_anonimizado = anonimizar(dfm15)
# dfa15_anonimizado = anonimizar(dfa15)
# dfma15_anonimizado = anonimizar(dfma15)
# dfjn15_anonimizado = anonimizar(dfjn15)
# dfjl15_anonimizado = anonimizar(dfjl15)
# dfag15_anonimizado = anonimizar(dfag15)
# dfs15_anonimizado = anonimizar(dfs15)
# dfo15_anonimizado = anonimizar(dfo15)
# dfn15_anonimizado = anonimizar(dfn15)
# dfd15_anonimizado = anonimizar(dfd15)
#
# dfj15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Janeiro_2015.xlsx")
# dff15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Fevereiro_2015.xlsx")
# dfm15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Março_2015.xlsx")
# dfa15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Abril_2015.xlsx")
# dfma15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Maio_2015.xlsx")
# dfjn15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Junho_2015.xlsx")
# dfjl15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Julho_2015.xlsx")
# dfag15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Agosto_2015.xlsx")
# dfs15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Setembro_2015.xlsx")
# dfo15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Outubro_2015.xlsx")
# dfn15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Novembro_2015.xlsx")
# dfd15_anonimizado.to_excel("C:/Users/agentes/Documents/Projeto HUC/dataset/dbs_anonimas/2015/Dezembro_2015.xlsx")

# dfj15 = pd.read_csv(dbj15, encoding='latin-1')
# dff15 = pd.read_csv(dbf15, encoding='latin-1')
# dfm15 = pd.read_csv(dbm15, encoding='latin-1')
# dfa15 = pd.read_csv(dba15, encoding='latin-1')
# dfma15 = pd.read_csv(dbma15, encoding='latin-1')
# dfjn15 = pd.read_csv(dbjn15, encoding='latin-1')
# dfjl15 = pd.read_csv(dbjl15, encoding='latin-1')
# dfag15 = pd.read_csv(dbag15, encoding='latin-1')
# dfs15 = pd.read_csv(dbs15, encoding='latin-1')
# dfo15 = pd.read_csv(dbo15, encoding='latin-1')
# dfn15 = pd.read_csv(dbn15, encoding='latin-1')
# dfd15 = pd.read_csv(dbd15, encoding='latin-1')

