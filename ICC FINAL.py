 # coding=utf-8
from datetime import date
from datetime import datetime

dataehora = datetime.now()
dataehora = dataehora.strftime('%d/%m/%Y')
data_atual = date.today()

listautores = []
listlivros = []

def linha():
    print('='*65)

def linhap():
    print('==================================================================\n')

def apagar():
    listlivro = []
    listautores = []
    count = 0
    count2 = 0
    numref = 0

    livroapag = input('DIGITE O LIVRO QUE DESEJA APAGAR: ')
    listlivros = open('listlivros.txt', 'r')
    for linha in listlivros.readlines():
        count = count + 1
        if linha != (livroapag.upper() + ' \n'):
            listlivro.append(linha)
        else:
            numref = count
    listlivros.close()
    listlivros = open('listlivros.txt', 'w')
    listautor = open('listautor.txt', 'r')
    for i in range(count - 1):
        listlivros.write('{} \n'.format(listlivro[i]))
    for linha2 in listautor.readlines():
        count2 = count2 + 1
        if numref != count:
            listautores.append(linha2)
    listlivros.close()
    listautor.close()
    listautor = open('listautor.txt', 'w')
    for j in range(count2 - 1):
        listautor.write('{} \n'.format(listautores[j]))
    listautor.close()
    print('LIVRO APAGADO COM SUCESSO!')
    print('==================================================================\n')

def cadastrar():
    recebelivro = input('NOME DO LIVRO: \n')
    recebeautor = input('NOME DO AUTOR: \n')

    listlivros = open('listlivros.txt', 'a')
    listlivros.write('{} \n'.format(recebelivro.upper()))
    listlivros.close()

    listautor = open('listautor.txt', 'a')
    listautor.write('{} \n'.format(recebeautor.upper()))
    listautor.close()


def editar():
        listalivro = []
        listaautor = []
        count = 0
        count1 = 0
        numref = 0

        print('==================================================================\n')
        print('EDITAR UM LIVRO')
        print('==================================================================\n')
        recebelivro = input('DIGITE O NOME DO LIVRO: \n')
        procurar = ('{} \n'.format(recebelivro.upper()))
        listlivro = open('listlivros.txt', 'r')
        for line in listlivro.readlines():
            count = count + 1
            if line == procurar:
                novo = input('DIGITE O NOVO NOME DO LIVRO: \n')
                numref = count
                listalivro.append(
                    '{} \n'.format(novo.upper()))
                
            else:
                listalivro.append(line)

        listlivro.close()

        listlivro = open('listlivros.txt', 'w')
        for i in range(count):
            listlivro.write('{} \n'.format(listalivro[i]))
        listlivro.close()

        listautor = open('listautor.txt', 'r')
        for line1 in listautor.readlines():
            count1 = count1 + 1
            if count1 == numref:
                novo1 = input('DIGITE O NOVO NOME DO AUTOR: \n')
                listaautor.append(novo1.upper())
            else:
                listaautor.append(line1)
        listautor.close()

        listautor = open('listautor.txt', 'w')
        for j in range(count1):
            listautor.write('{} \n'.format(listaautor[j]))
        listautor.close()
        print('LIVRO EDITADO COM SUCESSO')
        print('==================================================================\n')
                

            
def cadastrar():
    recebelivro = input('NOME DO LIVRO: \n')
    recebeautor = input('NOME DO AUTOR: \n')

    listlivros = open('listlivros.txt', 'a')
    listlivros.write('{} \n'.format(recebelivro.upper()))
    listlivros.close()

    listautor = open('listautor.txt', 'a')
    listautor.write('{} \n'.format(recebeautor.upper()))
    listautor.close()
    


def pesquisar():
    tem = 0
    aut_liv = 0
    jaexec = 0
    entrada = int(input("ÁREA DE PESQUISA\n1) PESQUISAR POR AUTOR\n2)PESQUISAR POR LIVRO\n0) SAIR\nR: \n"))
    if entrada == 1:
        i = input("DIGITE O NOME DO AUTOR: \n")
        aut_liv = 1
        for line in open('listautor.txt'):
            if i.upper() in line:
                tem = 1
                if jaexec == 0:
                    print("O AUTOR {} CONSTA NA NOSSA BIBLIOTECA!\n".format(i))
                    print('==================================================================\n')
                jaexec = 1
            

    elif entrada == 2:
        i = input("DIGITE O NOME DO LIVRO: \n")
        aut_liv = 2
        for line in open('listlivros.txt'):
            if i.upper() in line:
                tem = 1
                print("O LIVRO {} CONSTA NA NOSSA BIBLITECA!\n".format(i))
                
    else:
        print('OPÇÃO INVÁLIDA! VOCÊ RETORNARÁ AO MENU.')
        print('==================================================================\n')

    if tem == 0:
        if aut_liv == 2:
            print('NÃO TEMOS AINDA ESSE LIVRO NA NOSSA BIBLIOTECA!')
            print('==================================================================\n')    
        else:
            print('NÃO HÁ NENHUMA CORRESPONDÊNCIA DE LIVRO DESSE AUTOR!')
            print('==================================================================\n')
            


def alugar():
    print('==================================================================\n')
    print('DESEJA ALUGAR UM LIVRO? AGRADECEMOS A PREFÊRENCIA!\n'
          'PARA CONTINUAR, NOS INFORME SEU NOME E O LIVRO DESEJADO!\n')
    recebenome = input('DIGITE SEU NOME: \n')
    recebelivro = input('DIGITE O NOME DO LIVRO: \n')
    for line in open('listlivros.txt'):
        if recebelivro.upper() in line:
            resposta = input("VOCÊ, {}, DESEJA ALUGAR O LIVRO {}?\n1) SIM\n2)NÃO\nR: ".format(recebenome, recebelivro))
            if resposta == '1':
                listaluguel = open('listaluguel.txt', 'a')
                listaluguel.write(
                    '{} - {} - {} - STATUS: ALUGADO \n'.format(recebenome.upper(), recebelivro.upper(), dataehora))
                listaluguel.close()
                print("LIVRO ALUGADO! VOCÊ TEM ATÉ UMA SEMANA PARA DEVOLVÊ-LO!\n"
                      "CASO QUEIRA ALUGAR PELA SEGUNDA VEZ, PRIMEIRAMENTE DEVOLVA-O E DEPOIS ALUGUE-O NOVAMENTE!\n")
                print('==================================================================\n')
                break

            elif resposta == '2':
                break

            else:
                print('NÃO TEMOS AINDA ESSE LIVRO NA NOSSA BIBLIOTECA!')
    


def devolucao():
    listaluguel1 = []
    count = 0
    tem = 0

    print('==================================================================\n')
    print('DEVOLUÇÃO DE LIVRO')
    print('==================================================================\n')
    recebenome = input('DIGITE SEU NOME: \n')
    recebelivro = input('DIGITE O NOME DO LIVRO: \n')
    recebedata = input('DIGITE A DATA DO ALUGUEL: \n')
    procurar = ('{} - {} - {} - STATUS: ALUGADO \n'.format(recebenome.upper(), recebelivro.upper(), recebedata))
    print(procurar)
    listaluguel = open('listaluguel.txt', 'r')
    for line in listaluguel.readlines():
        count = count + 1
        if line == procurar:
            tem = 1
            listaluguel1.append(
                '{} - {} - {} - STATUS: DEVOLVIDO \n'.format(recebenome.upper(), recebelivro.upper(), dataehora))
            print('==================================================================\n')

        else:
            listaluguel1.append(line)
    if tem > 0:
        print('DEVOLUÇÃO RECEBIDA!\n')
    else:
        print('ESTE LIVRO NÃO CONSTA NO SISTEMA')
    listaluguel = open('listaluguel.txt', 'w')
    for i in range(count):
        listaluguel.write('{} \n'.format(listaluguel1[i]))
    listaluguel.close()
    


print('='*65)
print('==================================================================\n')
r = int(input('DESEJA ENTRAR NA BIBLIOTECA?\nDIGITE 1 PARA ENTRAR.\nDIGITE 0 PARA SAIR\n'))
print('='*65)
print('==================================================================\n')
while r == 1:
    print('=====  ==  =====  ==      ==   =====  ======  ====  =====     =\n'
          '=   =      =   =  ==           =   =  ======  =     =        =  =\n'
          '=   =  ==  =   =  ==      ==   =   =    ==    =     =       =   =\n'
          '====   ==  ====   ==      ==   =   =    ==    ====  =      =======\n'
          '=   =  ==  =   =  ==      ==   =   =    ==    =     =      =     =\n'
          '=   =  ==  =   =  ======  ==   =   =    ==    =     =      =     =\n'
          '====   ==  ====   ======  ==   =====    ==    ====  =====  =     =\n')

    print('='*65)
    print('==================================================================\n')
    print("DATA ATUAL: ", dataehora, "\n"
                                     "1) CADASTRAR LIVRO\n"
                                     "2) PESQUISAR LIVRO OU AUTOR\n"
                                     "3) ALUGAR LIVRO\n"
                                     "4) EXCLUIR LIVROS\n"
                                     "5) EDITAR LIVROS\n"
                                     "6) DEVOLVER LIVROS\n"
                                     "0) SAIR\n")
    print('='*65)
    print('==================================================================\n')

    res = input("ESCOLHA UMA OPÇÃO: \n")
    if res == '1':
        cadastrar()

    elif res == '2':
        pesquisar()

    elif res == '0':
        print('='*65)
        print("OBRIGADO PELA VISITA!")
        break

    elif res == '3':
        alugar()

    elif res == '6':
        devolucao()

    elif res == '4':
        apagar()

    elif res == '5':
        editar()

                

    else:
        print('==================================================================\n')
        print('OPÇÃO INVÁLIDA!\n')
        print('==================================================================\n')
        r = int(input('DESEJA CONTINUAR NA BIBLIOTECA?\nDIGITE 0 PARA SAIR E 1 PARA CONTINUAR.\n'))
