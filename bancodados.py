"""
NOME: César Augusto de Carvalho.
CURSO: Análise e Desenvolvimento de Sistemas.
DISCIPLINA(TURMA): Raciocínio Computacional (11100010563_20231_04)
"""
import json
#Função para escrever/gravar os dados no arquivo .json
def escrever_json(arquivo, data):
    with open(arquivo+'.json', "w") as file: # abre o arquivo com nome correspondente
        json.dump(data, file, indent=2)      # grava os dados no arquivo
        file.close()                         # fecha o arquivo

#Função de para ler/recuperar os dados do arquino .json
def ler_json(arquivo):
    dados = {}
    try:
        with open(arquivo+'.json', "r") as file:
            dados = json.load(file)
            file.close()
            return dados
    except FileNotFoundError:
        #print("Arquivo não encontrado")
        return dados
