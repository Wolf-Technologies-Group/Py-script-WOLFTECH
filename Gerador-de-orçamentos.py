#!/usr/bin/python2.7
# -*- coding: utf-8 -*-


#######        Tabela de serviços WT 2016       ########
########      Creator - Victor Consuegra       ########
##########           21/02/2016               #########
###########         Versão  1.6             ###########

# Executar o script na versão python2.7
# Em breve teremos na versão 3 do python


#Declaração de variáveis / Operacional

wolf_service = 99.99         # Formatação completa + Backup + Limpeza + Pasta térmica + Report completo do sistema
clean        = 40            # Custo de uma limpeza completa
backup       = 35            # Custo de um backup sem nenhum adicional
wolf_search  = 75            # Custo de uma análise de sistema em busca de vírus,malwares,trojans etc.
web_builder  = 600           # Criação de site + Domínio + Hospedagem + Manutenção mensal
web_seo      = 200           # Manutenção de contéudo + Técnicas de SEO + Marketing cobrado por MÊS

# Custo de necessidades durante o atendimento

food = 10             # Comida consumida durante o atendimento
trip = 8              # Custo da passagem de ida e volta
hora_extra = 30       # Custo da hora extra trabalhada

# Sistemas de descontos e pacotes promocionais para empresas

pacote_3_pc  = 280  #  3 WORKSTATIONS R$ 20,00  em descontos
pacote_5_pc  = 430  #  5 WORKSTATIONS R$ 70,00  em descontos
pacote_10_pc = 900  # 10 WORKSTATIONS R$ 100,00 em descontos
pacote_15_pc = 1350 # 15 WORKSTATIONS R$ 150,00 em descontos
pacote_20_pc = 1800 # 20 WORKSTATIONS R$ 200,00 em descontos
pacote_25_pc = 2250 # 25 WORKSTATIONS R$ 250,00 em descontos
pacote_30_pc = 2700 # 30 WORKSTATIONS R$ 300,00 em descontos

# Sistemas de contratos empresariais de 3,6 e 12 meses
# Taxa fixa de R$ 69,90 por WORKSTATION

deal_contract  = 69.90 # 2 visitas por mês + Manutenção + Diagnóstico de sistema + Limpeza


# Funções extras

import os  
import sys

#Hora atual

from   datetime import datetime
now =  datetime.now()   # Principal variável para exibir a hora atual do script

# Função HORA ATUAL

def hora():
    print " Brasília , %s / %s/ %i  at  %.2f  " %(now.day , now.month , now.year, now.hour)

# Função WOLF BANNER

def banner():
    print  '''
              __        _____  _     _____
              \ \      / / _ \| |   |  ___|
               \ /\ / / | | | | |   |_
                \ V  V /| |_| | |___|  _|
                 \_/\_/  \___/|_____|_|
                           _____ _____ ____ _   _
                          |_   _| ____/ ___| | | |
                            | | |  _|| |   | |_| |
                            | | | |__| |___|  _  |
                            |_| |_____\____|_| |_|

                   Contato -  wolfsecurity@protonmail.com
                              www.wolftech.com.br
                        Problemas com seu computador ?
                           FALE com especialistas ! '''
print
print

#Início da interatividade do script

def menu():
    os.system('clear')


banner()
print '##' * 79
print "     [i] Bem-vindo ao gerador de orçamentos WOLF TECHNOLOGIES                    [i] "
print "     [i] Escolha o serviço desejado digitando números de 1 - 7                   [i] "
print "     [i] Precisando de suporte mensal ? solicite já seu orçamento (61) 9580-7967 [i] "
print "     [i] Digite 0 para fechar o programa                                         [i] "
print '--' * 81
print
print "     [1] -Limpeza , Formatação , Backup , Report completo do sistema -  [+] "
print "     [2] -Limpeza completa - Desktop & Notebook                      -  [+] "
print "     [3] -Backup de dados                                            -  [+] "
print "     [4] -Análise completa do sistema                                -  [+] "
print "     [5] -Criação e hospedagem de sites profissionais                -  [+] "
print "     [6] -Técnicas de SEO, criação de contéudo                       -  [+] "
print "     [7] -Contratos corporativos 3,6 e 12 meses                      -  [+] "
print "     [0] -Sair do programa                                           -  [-] "
print

print " Start script at "

hora()                     # Hora,dia e ano atual

print

# Função menu , principal função desta atualização

def menu_opcao():

    opcao = raw_input ("[START] - Selecione uma opção [0-7] [!]    ")
    if opcao ==   '1':
        print
        print                  " [!] O valor para cada computador é de R$ 100,00               [!] "
        print                  " [!] Consultar tabela de preços para atendimentos corporativos [!] "
        print                  " [!]                    www.wolftech.com.br                    [!] "
        print
        work_pc       =  input ( " Há quantos computadores no local  ?  " )
        total_pc      = work_pc * wolf_service
        print                  ( " O VALOR DO SERVIÇO FICOU EM -  [  R$ %.2f   ]" ) % total_pc
        print                  ( " Para mais informações sobre parcelamentos e pagamentos ")
        print '--' * 81
        print                  ( " Consulte nossos planos de suporte corporativo - www.wolftech.com.br ")
        print                  ( " Preços mais leves de acordo com o número de WORKSTATIONS ")
        print




    elif opcao == '2':
        print
        print                   " [!] O valor para cada computador é de R$ 40,00                [!] "
        print                   " [!] Consultar tabela de preços para atendimentos corporativos [!] "
        print
        work_pc2      = input  ( " Há quantos computadores no local  ?   ")
        total_pc2     = work_pc2 * clean
        print                  (" O VALOR DO SERVIÇO FICOU EM -   R$ %.2f    ") % total_pc2
        print


    elif opcao == '3':
        print
        print                   " [!] O valor para cada computador é de R$ 35,00                [!] "
        print                   " [!] Consultar tabela de preços para atendimentos corporativos [!] "
        print
        work_pc3      = input  ( " Há quantos computadores no local  ?   ")
        total_pc3     = work_pc3 * backup
        print                  (" O VALOR DO SERVIÇO FICOU EM -  R$ %.2f    ") % total_pc3
        print


    elif opcao == '4':
        print
        print                   " [!] O valor para cada computador é de R$ 75,00                [!] "
        print                   " [!] Consultar tabela de preços para atendimentos corporativos [!] "
        print
        work_pc4      = input  ( " Há quantos computadores no local  ?   ")
        total_pc4     = work_pc4 * wolf_search
        print                  (" O VALOR DO SERVIÇO FICOU EM -   R$ %.2f    ") % total_pc4
        print


    elif opcao == '5':
        print
        print                   " [!] O valor para desenvolvimento e hospedagem é de R$ 600,00     [!] "
        print                   " [!] Site seguros,responsivos,rapidos e bonitos !                 [!] "
        print                   " [!] Sites feitos sob medida, e atendendo os critérios do cliente [!] "
        print
        work_pc5      = input  ( " Quantos websites serão criados e hospedados ?   ")
        total_pc5     = work_pc5 * web_builder
        print                  (" O VALOR DO SERVIÇO FICOU EM -  R$ %.2f   ") % total_pc5
        print


    elif opcao == '6':
        print
        print                   " [!] O valor mensal a ser pago é de R$ 200,00                     [!] "
        print                   " [!] Consultar tabela de preços para atendimentos corporativos    [!] "
        print                   " [!] O valor só será pago se as metas de tráfegos forem atingidas [!] "
        print
        work_pc6      = input  ( " Necessita de suporte SEO por quantos meses  ?   ")
        total_pc6     = work_pc6 * web_seo
        print                  (" O VALOR DO SERVIÇO FICOU EM -   R$ %.2f   ") % total_pc6
        print


    elif opcao == '7':
        print '--' * 81
        print                   "  [!] Os serviços prestados via contrato funcionarão da seguinte forma [!]  "
        print                   "  [!] 2 visitas por mês + diagnóstico de sistema + limpeza completa    [!]  "
        print
        print                   "  [!] O valor para cada  WORKSTATION é de R$ 69,90                     [!]  "
        print
        work_pc7      = input  ( " Há quantos computadores na empresa  ?       ")
        total_pc7     = (work_pc7 * deal_contract)
        print
        contract      = input  ( " Digite o tempo de suporte [3] , [6] , [12]  ")
        print

        if   contract  == 3:
            print " O VALOR TOTAL DO CONTRATO MENSAL É DE -  R$ %.2f    " % total_pc7
            print
        elif contract  == 6:
            print " O valor total do contrato mensal é de R$ %.2f   " % total_pc7
            print
        elif contract  == 12:
            print " O valo total do contrato  mensal é de R$ %.2f    " % total_pc7
            print

    elif opcao == '0':
        sys.exit()


    else:
        menu_opcao() # Evita erros caso o usuário digite um valor diferente do solicitado

menu_opcao()  # Begin

# Loop para o script
# Com este loop, o script sempre irá perguntar no final de cada orçamento se deseja fazer outro cálculo ou se deseja fechar o programa

while menu_opcao()!= 0:
    print " Deseja fazer um novo orçamento ?
    verific = raw_input (" [Sim] ou [Não] " )
    if verific == 'sim':
        menu()
        menu_opcoes()
    else:
        sys.exit()


