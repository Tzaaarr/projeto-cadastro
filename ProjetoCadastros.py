"""
NOME: César Augusto de Carvalho.
CURSO: Análise e Desenvolvimento de Sistemas.
DISCIPLINA(TURMA): Raciocínio Computacional (11100010563_20231_04)
"""
#===================BIBLIOTECAS_IMPORTADAS:
#importação da funções e classes especificas que serão utilizadas
from operacoes import operacoes_basicas
from bancodados import ler_json
#===================VARIAVEIS_GLOBAIS
#Declaração da lista para cadastro/registro
lista_cadastro_registros = []

#Função para encerrar o programa.
def finalizar_programa():
    print(">>> Finalizando o programa...")
    exit(0)

#Função do Menu Principal, vai exibir as opções, receber qual foi digitada e retornar o valor quando a função for chamada
def menu_principal():
    # Inicia a variavel de opção
    opcao_menu = 0
    while(True):
        print("\n===== [MENU PRINCIPAL] =====\n")
        print("[1]-Estudante \n[2]-Professor \n[3]-Disciplina \n[4]-Turma \n[5]-Matricula \n[6]-Sair \n")
        try:
            opcao_menu = int(input("Digite o número de acordo com a opção desejada: "))
            # verifica se o número digitado está entre os quais foram exibidos nas opções.
            if 1 <= opcao_menu <= 6:
                return opcao_menu
            else:
                print(">>> Opção Inválida!")
        except ValueError:
            print("Valores incorretos! Digite novamente")

# Função do Menu de Operações, vai exibir as opções, receber qual foi digitada e retornar o valor quando a função for chamada
def menu(bd):
    # Inicia a variavel de opção
    opcao_menu = 0

    while(True):
        print("\n>>> [MENU DE OPERAÇÕES] ---(", bd,")<<<\n")
        print("(1) Inserir. \n(2) Listar. \n(3) Atualizar. \n(4) Excluir. \n(5) Pesquisar. \n(6) Voltar - Menu Principal. \n")
        try:
            opcao_menu = int(input("Digite o número de acordo com a opção desejada: "))
            # verifica se o número digitado está entre os quais foram exibidos nas opções.
            if 1 <= opcao_menu <= 6:
                return opcao_menu
            else:
                print(">>> Opção Inválida!")
        except ValueError:
            print("Valores incorretos! Digite novamente")

#Função da estrutura de repetição do Menu de Operações, vai verificar qual opção foi digitada e chamar a função correspondente.
def inicio_registro(arquivo_bd):
    while(True):
        # Lê o banco e atribui o conteúdo a lista
        lista_cadastro_registros = ler_json(arquivo_bd)
        opcao_escolhida = operacoes_basicas(lista_cadastro_registros, arquivo_bd)
        # Atribui a opção escolhida para variavel.
        op = menu(arquivo_bd)
        # Verifica de acordo com o numero a função especifica.
        if op == 1:
            # Variavel já declaração antes que chamou a classe + nome da metodo + parametros
            opcao_escolhida.cadastrar_registro(lista_cadastro_registros,arquivo_bd)
            pass
        elif op == 2:
            opcao_escolhida.listar_registro(lista_cadastro_registros, arquivo_bd)
            pass
        elif op == 3:
            opcao_escolhida.alterar_registro(lista_cadastro_registros,arquivo_bd)
            pass
        elif op == 4:
            opcao_escolhida.excluir_registro(lista_cadastro_registros,arquivo_bd)
            pass
        elif op == 5:
            opcao_escolhida.pesquisar_registro(lista_cadastro_registros,arquivo_bd)
            pass
        else:
            break

# Estrutura de repetido do Menu Principal.
while(True):
   # Atribui a opção escolhida à variavel.
   op_principal = menu_principal()
   # Chama a função da estrutura de repetição dos operadores, passando o como parâmetro o nome do arquivo/opção selecionada
   if op_principal == 1:
        bd = "estudantes"
        inicio_registro(bd)
   elif op_principal == 2:
        bd = "professores"
        inicio_registro(bd)
   elif op_principal == 3:
        bd = "disciplinas"
        inicio_registro(bd)
   elif op_principal == 4:
        bd = "turmas"
        inicio_registro(bd)
   elif op_principal == 5:
        bd = "matriculas"
        inicio_registro(bd)
   elif op_principal == 6:
        finalizar_programa()
