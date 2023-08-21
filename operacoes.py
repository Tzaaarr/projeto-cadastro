"""
NOME: César Augusto de Carvalho.
CURSO: Análise e Desenvolvimento de Sistemas.
DISCIPLINA(TURMA): Raciocínio Computacional (11100010563_20231_04)
"""
# Importa as funçoes do arquivo "bancodados" para ler e escrever.
import bancodados
# Função que retorna o codigo caso seja igual ao pesquisado no respectivo arquivo .json.
def pesquisa_cod(codigo,banco):
    lista_registros = bancodados.ler_json(banco)
    tam = len(lista_registros)
    if tam != 0:
        for c in range(0, tam):
            if codigo == lista_registros[c]['cod']:
                return codigo
    else:
        # Caso o arquivo .json esteja vazio, retorna o próprio tam da lista, que seria zero.
        return tam

# Função que tem como parâmetro o arquivo especifico e retorna a bibioteca com os dados preenchidos
def dicionario_registro(banco):
    registro_cadastro = {}

    if banco != "matriculas":
        while (True):
            try:
                cod_registro = int(input("Digite o código: "))
                cod_retorno = pesquisa_cod(cod_registro, banco)
                if cod_retorno == cod_registro:
                    print("Código já existente!")
                    continue
                else:
                    break
            except ValueError:
                print("Preencha corretamente!")
        registro_cadastro['cod'] = cod_registro

    if banco == "estudantes" or banco == "professores" or banco == "disciplinas":
        while (True):
            nome_registro = input("Digite o nome: ").lower()
            if len(nome_registro) != 0:
                registro_cadastro['nome'] = nome_registro
                break
            else:
                print("Campo vazio!")
                continue

    if banco == "estudantes" or banco == "professores":
        while (True):
            cpf_registro = input("Digite o CPF: ")
            if len(cpf_registro) != 0:
                # Grava apenas os primeiros 15 caracteres
                registro_cadastro['cpf'] = cpf_registro[0:15]
                break
            else:
                print("Campo vazio!")
                continue

    if banco == "turmas":
        while (True):
            try:
                cod_turma_professor = int(input("Digite o codigo do professor cadastrado: "))
                cod_retorno = pesquisa_cod(cod_turma_professor, "professores")
                if cod_retorno == 0:
                    print("Lista professor vazia - Cód.Professor cadastrado!")
                    break
                elif cod_retorno != cod_turma_professor:
                    print("Professor não cadastrado!")
                    continue
                else:
                    break
            except ValueError:
                print("Preencha corretamente!")
        registro_cadastro['cod_prof'] = cod_turma_professor

        while (True):
            try:
                cod_turma_disciplina = int(input("Digite o codigo da disciplina cadastrada: "))
                cod_retorno = pesquisa_cod(cod_turma_disciplina, "disciplinas")
                if cod_retorno == 0:
                    print("Lista disciplina vazia - Cód.Disciplina cadastrada!")
                    break
                elif cod_retorno != cod_turma_disciplina:
                    print("Disciplina não cadastrado!")
                    continue
                else:
                    break
            except ValueError:
                print("Preencha corretamente!")
        registro_cadastro['cod_disc'] = cod_turma_disciplina

    if banco == "matriculas":
        while (True):
            try:
                cod_matricula_turma = int(input("Digite o codigo da turma cadastrada: "))
                cod_retorno = pesquisa_cod(cod_matricula_turma, "turmas")
                if cod_retorno == 0:
                    print("Lista turma vazia - Cód.Turma cadastrado!")
                    break
                elif cod_retorno != cod_matricula_turma:
                    print("Turma não cadastrada!")
                    continue
                else:
                    break
            except ValueError:
                print("Preencha corretamente!")
        registro_cadastro['cod_turma'] = cod_matricula_turma

        while (True):
            try:
                cod_matricula_estudante = int(input("Digite o codigo do estudante cadastrado: "))
                cod_retorno = pesquisa_cod(cod_matricula_estudante, "estudantes")
                if cod_retorno == 0:
                    print("Lista estudantes vazia - Cód.Estudante cadastrado!")
                    break
                elif cod_retorno != cod_matricula_estudante:
                    print("Estudante não cadastrado!")
                    continue
                else:
                    break
            except ValueError:
                print("Preencha corretamente!")
        registro_cadastro['cod_estudante'] = cod_matricula_estudante

    # Retorna os dados preenchidos como uma biblioteca
    return registro_cadastro


# Classe com as 4 operações basicas (incluir, listar, alterar e excluir)
class operacoes_basicas:

    # Metodo construtor
    def __init__(self, lista_cliente, banco):
        self.lista = lista_cliente
        self.banco = banco

    def cadastrar_registro(self, lista_cliente, banco):
        print("\n===== CADASTRO NOVO REGISTRO ==== ", banco)
        # chama a função dicionario_registro e tem como retorno a biblioteca como os dados
        dados_registro = dicionario_registro(banco)

        # verifica o tam da lista, caso esteja vazia será criada
        tam = len((self.lista))
        if tam == 0:
            lista_cliente = []
        # atribui o conteúdo da biblioteca para a lista
        lista_cliente.append(dados_registro)
        # Chamada da função que passa como parametro o nome do arquivo e a lista atual
        bancodados.escrever_json(banco, lista_cliente)

    def listar_registro(self, lista_cliente, banco):
        print("===== LISTA DE REGISTROS ==== ", banco)
        tam = len(self.lista)
        if tam == 0:
                print(">>> Não há registros cadastrados.")
        else:
            for c in range(0, tam):
                if banco == "estudantes" or banco == "professores":
                    print("Código:", lista_cliente[c]['cod'], "Nome:", lista_cliente[c]['nome'], "CPF:", lista_cliente[c]['cpf'])
                elif banco == "disciplinas":
                    print("Código:", lista_cliente[c]['cod'], "Disciplina:", lista_cliente[c]['nome'])
                elif banco == "turmas":
                    print("Turma:", lista_cliente[c]['cod'], "Cód.Professor:", lista_cliente[c]['cod_prof'], "Cód.Disciplina:", lista_cliente[c]['cod_disc'])
                elif banco == "matriculas":
                    print("Cód.Turma:", lista_cliente[c]['cod_turma'], "Cód.Estudante:", lista_cliente[c]['cod_estudante'])
            print("======================")
            print(">>> Registros encontrados:", len(lista_cliente))

    def alterar_registro(self, lista_cliente, banco):
        print("\n===== ALTERAÇÃO DE REGISTRO ==== ")
        tam = len(self.lista)
        if tam == 0:
            print(">>> Não há registros cadastrados.")
        else:
            try:
                codigo_alteracao = int(input("Digite o código do registro que deseja alterar: "))
                for c in range(0, tam):
                    if banco == "matriculas":
                        codigo_registro = lista_cliente[c]['cod_estudante']
                    else:
                        codigo_registro = lista_cliente[c]['cod']
                    if codigo_alteracao == codigo_registro:
                        print("Alteração do código:", codigo_alteracao)

                        # Chama a função para inserir novos dados
                        # Atribui o retorno da função à varivel com o cod correspondente
                        lista_cliente[c] = dicionario_registro(banco)
                        # Agora a atual lista é passada como parâmetro chamando a função para gravar os dados no arquivo .json
                        bancodados.escrever_json(banco, lista_cliente)

                        print("Registro atualizado!")
                        break
                    # contador começa em zero, por isso tam(total) -1.
                    elif c == (tam - 1):
                        print("Código não encontrado.")
                        break
                    else:
                        pass
            except ValueError:
                print("Valor incorreto! Digite novamente.")

    def excluir_registro(self, lista_cliente, banco):
        print("\n===== REMOÇÃO DE REGISTRO ==== ")
        tam = len(self.lista)
        if tam == 0:
            print(">>> Não há registros cadastrados.")
        else:
            try:
                # Para exclusão de dados da lista de matriculas, foi utilizado o cod do estudante com referência/busca.
                codigo_remocao = int(input("Digite o código do registro que deseja remover: "))
                for c in range(0, tam):
                    if banco == "matriculas":
                        codigo_registro = lista_cliente[c]['cod_estudante']
                    else:
                        codigo_registro = lista_cliente[c]['cod']
                    if codigo_remocao == codigo_registro:
                        print("Cadastro removido: ", codigo_remocao)
                        del lista_cliente[c]
                        # chama a função para gravar a lista no arquivo .json
                        bancodados.escrever_json(banco, lista_cliente)
                        break
                    # contador começa em zero, por isso tam(total) -1.
                    elif c == (tam - 1):
                        print("Código não encontrado.")
                        break
                    else:
                        pass
            except ValueError:
                print("Valor incorreto! Digite novamente.")


    def pesquisar_registro(self, lista_cliente, banco):
        print("\n===== PESQUISA DE REGISTRO ==== ")
        tam = len(self.lista)
        if tam == 0:
            print(">>> Não há registros cadastrados.")
        else:
            try:
                codigo_pesquisa = int(input("Digite o código do registro que deseja pesquisar: "))
                for c in range(0, tam):
                    if banco == "matriculas":
                        codigo_registro = lista_cliente[c]['cod_estudante']
                    else:
                        codigo_registro = lista_cliente[c]['cod']
                    if codigo_pesquisa == codigo_registro:
                        # Verifica qual arquivo e assim mostrar os dados correspondentes
                        if banco == "estudantes" or banco == "professores":
                            print("Código:", lista_cliente[c]['cod'], "Nome:", lista_cliente[c]['nome'], "CPF:",
                                  lista_cliente[c]['cpf'])
                        elif banco == "disciplinas":
                            print("Código:", lista_cliente[c]['cod'], "Disciplina:", lista_cliente[c]['nome'])
                        elif banco == "turmas":
                            print("Turma:", lista_cliente[c]['cod'], "Cód.Professor:", lista_cliente[c]['cod_prof'],
                                  "Cód.Disciplina:", lista_cliente[c]['cod_disc'])
                        elif banco == "matriculas":
                            print("Cód.Turma:", lista_cliente[c]['cod_turma'], "Cód.Estudante:",
                                  lista_cliente[c]['cod_estudante'])
                        break
                    # contador começa em zero, por isso tam(total) -1.
                    elif c == (tam - 1):
                        print("Código não encontrado.")
                        break
                    else:
                        pass
            except ValueError:
                print("Valor incorreto! Digite novamente.")



