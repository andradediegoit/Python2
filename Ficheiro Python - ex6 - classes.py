#%% Criação da classe Pessoa

import os

class Pessoa:
    def __init__(self, primeiroNome, ultimoNome, idade, profissao):
        self.primeiroNomeI = primeiroNome
        self.ultimoNomeI = ultimoNome
        self.idadeI = idade
        self.profissaoI = profissao

    def obterNome(self):
        return self.primeiroNomeI, self.ultimoNomeI
    
    def obterIdade(self):
        return self.idadeI

    def obterProfissao(self):
        return self.profissaoI

    def alterarNome(self, newPrimeiroNome, newUltimoNome):
        self.primeiroNomeI = newPrimeiroNome
        self.ultimoNomeI = newUltimoNome
        return self.primeiroNomeI, self.ultimoNomeI

    def alterarIdade(self, newIdade):
        self.idadeI = newIdade
        return self.idadeI

    def alterarProfissao(self, newProfissao):
        self.profissaoI = newProfissao
        return self.profissaoI
# Criação da lista de objetos referenciados pela classe Pessoa
objPessoas = []
'''
pes = Pessoa('jk','dfg12',22,'eng')
objPessoas[0] = Pessoa('joao','araujo',39,'formador')
objPessoas[1] = Pessoa('asdas','sdffsdf',5616,'Tecnico')
'''


def listaPessoas(objPessoas):
    for i in range(len(objPessoas)):
        print('---------------Opção ' + str(i) + '------------------')
        print('Primeiro Nome:' + str(objPessoas[i].obterNome()[0]) +
        '\n' + 'Ultimo Nome:' + str(objPessoas[i].obterNome()[1]) + '\n' + 
        'Idade:' + str(objPessoas[i].obterIdade()) + '\n' +
        'Profissão:' + str(objPessoas[i].obterProfissao()))
    opcaoNome = input('Introduza o numero correspondente à pessoa que quer alterar:')
    try:
        iOpcaoNome = int(opcaoNome)
        if iOpcaoNome >= len(objPessoas):
            print('Introduza um numero dentro das opções disponíveis')
            # Código de erro -1
            iOpcaoNome = -1
    except:
        # Código de erro -1: código de inserir opções erradamente
        iOpcaoNome = -1
        print('Introduza o numero correto.')
    finally:
        return iOpcaoNome

while True:
    print('****************************************')
    print('*************User interface*************')
    print('****************************************')
    print('C - Consultar pessoas')
    print('T - Adicionar pessoas')
    print('A - Alterar Nome')
    print('I - Alterar Idade')
    print('P - Alterar Profissão')
    print('E - Eliminar Pessoa')
    print('X - Sair')
    opcao = input('Escolha uma opção:')

    if opcao == 'C' or opcao == 'c':
        if len(objPessoas) == 0:
            print('Não existem pessoas adicionadas')
        else:
            print('----------Consulta de pessoas--------------')
            for i in range(len(objPessoas)):
                print('Primeiro Nome:' +objPessoas[i].obterNome()[0])
                print('Ultimo Nome:' + objPessoas[i].obterNome()[1])
                print('Idade:' + objPessoas[i].obterIdade())
                print('Profissão:' + objPessoas[i].obterProfissao())
                print('-------------------------------------------')
        input('Pressione Enter para continuar...')
        clear = lambda: os.system('cls')
        clear()

    elif opcao == 'T' or opcao == 't':
        print('-----------Introduzir pessoas--------------')
        pNome = input('Introduza o primeiro nome:')
        uNome = input('Introduza o ultimo nome:')
        idade = input('Introduza a idade:')
        profissao = input('Introduza a profissao:')
        objPessoas.append(Pessoa(pNome, uNome, idade, profissao))
        #objPessoas[0] = Pessoa(pNome, uNome, idade, profissao))
        print('Pessoa nova introduzida.')
        input('Pressione Enter para continuar...')
        # Funciona apenas no terminal Python
        clear = lambda: os.system('cls')
        clear()
    elif opcao == 'A' or opcao == 'a':
        if len(objPessoas) == 0:
            print('Não existem pessoas adicionadas')
            input('Pressione Enter para continuar...')
            # Funciona apenas no terminal Python. Limpa o terminal
            clear = lambda: os.system('cls')
            clear()
        else:
            iOpcaoNome = listaPessoas(objPessoas)
            if iOpcaoNome >= 0:
                pNome = input('introduza o novo primeiro nome:')
                uNome = input('Indroduza o novo ultimo nome:')
                objPessoas[iOpcaoNome].alterarNome(pNome,uNome)
                print('Nome da pessoa alterado.')
                input('Pressione Enter para continuar...')
                clear = lambda: os.system('cls')
                clear()
            input('Pressione Enter para continuar...')
            clear()

    elif opcao == 'I' or opcao == 'i':
        if len(objPessoas) == 0:
            print('Não existem pessoas adicionadas')
            input('Pressione Enter para continuar...')
            clear = lambda: os.system('cls')
            clear()
        else:
            iOpcaoNome = listaPessoas(objPessoas)
            if iOpcaoNome >= 0:
                idade = input('Introduza a nova idade:')
                objPessoas[iOpcaoNome].alterarIdade(idade)
                
                print('Idade da pessoa alterada.')
                input('Pressione Enter para continuar...')
                clear = lambda: os.system('cls')
                clear()
    elif opcao == 'P' or opcao == 'p':
        if len(objPessoas) == 0:
            print('Não existem pessoas adicionadas')
            input('Pressione Enter para continuar...')
            clear = lambda: os.system('cls')
            clear()
        else:
            iOpcaoNome = listaPessoas(objPessoas)
            if iOpcaoNome >= 0:
                profissao = input('Introduza a nova profissao:')
                objPessoas[iOpcaoNome].alterarProfissao(profissao)
                print('Profissão da pessoa alterada.')
                input('Pressione Enter para continuar...')
                clear = lambda: os.system('cls')
                clear()
    
    elif opcao.upper() == 'E':
        if len(objPessoas) == 0:
            print('Não existem pessoas adicionadas')
            input('Pressione Enter para continuar...')
            clear = lambda: os.system('cls')
            clear()
        else:
            iOpcaoNome = listaPessoas(objPessoas)
            if iOpcaoNome >= 0:
                objPessoas.pop(iOpcaoNome)
                print('Pessoa eliminada.')
                input('Pressione Enter para continuar...')
                clear = lambda: os.system('cls')
                clear()


    elif opcao == 'X' or opcao == 'x':
        break



# %%
