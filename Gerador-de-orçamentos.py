# -*- coding:utf-8 -*-

# Started at - 21/02/2016               
# Versão     - 1.9             
# Creator    - Victor Consuegra
# Run on python 2.7
# Last commit 27/05/2016 

# Apresentação - Este script foi criado com a ideia de facilitar o cálculo de orçamento de clientes que visitarem o web-site atráves
# do cartão de visitas entregue em reuniões ou networking

#Dúvidas ? sugestões ? feddbacks positivos ou negativos ? me envie um e-mail - consuegra177@gmail.com


# Funções especiais

import os
import sys

from   datetime import datetime
now =  datetime.now()  

# Função HORA ATUAL

def hora():
    print  ( "     %s / %s / %s     " ) % (now.day , now.month , now.year)

# Função  BANNER

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

                          wolfsecurity@protonmail.com
                              www.wolftech.com.br
                        Problemas com seu computador ?
                           FALE com especialistas ! '''
print
print

# Printa o banner na tela assim que o script for iniciado

banner() 

#Início da interatividade do script

def menu():

    print # Espaçador
    
    # Informações iniciais sobre o script

    print  "     [i] Bem-vindo ao gerador de orcamentos WOLF TECHNOLOGIES                    [i] "
    print  "     [i] Escolha o servico desejado digitando numeros de 1 - 7                   [i] "
    print  "     [i] Precisando de suporte mensal ? solicite ja seu orcamento (61) 9580-7967 [i] "
    
    # Informações sobre o menu e como utilizar

    print
    print
    print   "    [1] -Limpeza , Formatacao , Backup , Report completo do sistema   "
    print   "    [2] -Limpeza completa - Desktop & Notebook                        "
    print   "    [3] -Backup de dados                                              "
    print   "    [4] -Analise completa do sistema                                  "
    print   "    [5] -Criacao e hospedagem de sites profissionais                  "
    print   "    [6] -Tecnicas de SEO, criacao de conteudo                         "
    print   "    [7] -Contratos corporativos 3,6 e 12 meses                        "
    print   "    [0] -Sair do programa                                             "
    print
    print  " [ Script iniciado em ]    python 2.7  "

    hora()   # Hora,dia e ano atual em que o script foi executado

    print

menu() # Inicia o menu de opções

print


# Função menu de opções

def menu_opcao():
    
    print  
    print
    print                 "               Para fechar o script digite [0]       "
    print
    opcao = raw_input (   "          [START] - Selecione uma opção [1-7] [!]    ")
    print
    
    # Declarações de variáveis que serão utilizadas dentro dos blocos

    wolf_service = 99.99         # Formatação completa + Backup + Limpeza + Pasta térmica + Report completo do sistema
    clean        = 50
    backup       = 35            # Custo de um backup sem nenhum adicional
    wolf_search  = 75            # Custo de uma análise de sistema em busca de vírus,malwares,trojans etc.
    web_builder  = 600           # Criação de site + Domínio + Hospedagem + Manutenção mensal
    web_seo      = 200           # Manutenção de contéudo + Técnicas de SEO + Marketing cobrado por MÊS

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
    
    # Início dos blocos de decisão

    if opcao ==   '1':
        print
        print                   "    [!]          O valor para cada computador é de R$ 100,00       [!] "
        print                   "    [!] Consultar tabela de preços para atendimentos corporativos  [!] "
        print                   "    [!]                    www.wolftech.com.br                     [!] "
        print
        print                                     "  Digite [0] para fechar o script "
        print
        
        work_pc       =  input ( "    Há quantos computadores no local  ?  " )
        total_pc      =  work_pc * wolf_service
        print                   ("   O VALOR DO SERVIÇO FICOU EM -  [  R$ %.2f   ]" ) % (total_pc)
        print
        print
        
        print                    "        Para mais informaçoes sobre parcelamentos e pagamentos          " 
        print                    "    Consulte nossos planos de suporte corporativo - www.wolftech.com.br "
        print                    "        Preços mais leves de acordo com o número de WORKSTATIONS        " 
        print



    elif opcao == '2':
        
            print
            print                    "    [!]         O valor para cada computador é de R$ 50,00        [!] "
            print                    "    [!] Consultar tabela de preços para atendimentos corporativos [!] "
            print
            print                                     "  Digite [0] para fechar o script "
            print
            
            work_pc2      = input ("    Há quantos computadores no local  ?   ")
            total_pc2     = work_pc2 * clean
            print                   ("    O VALOR DO SERVIÇO FICOU EM -   R$ % .2f    ") % total_pc2
            print


    elif opcao == '3':
                print
                print                    "    [!]         O valor para cada computador é de R$ 35,00        [!] "
                print                    "    [!] Consultar tabela de preços para atendimentos corporativos [!] "
                print
                print                                     "  Digite [0] para fechar o script "
                print
                
                work_pc3      = input   ( "    Há quantos computadores no local  ?   ")
                total_pc3     = work_pc3 * backup
                print                   ("    O VALOR DO SERVIÇO FICOU EM -  R$ %.2f    ") % total_pc3
                print


    elif opcao == '4':
                    print
                    print                    "    [!]         O valor para cada computador é de R$ 75,00        [!] "
                    print                    "    [!] Consultar tabela de preços para atendimentos corporativos [!] "
                    print
                    print                                     "  Digite [0] para fechar o script "
                    print
                    
                    work_pc4      = input   ( "    Há quantos computadores no local  ?   ")
                    total_pc4      = work_pc4 * wolf_search
                    print                   ("    O VALOR DO SERVIÇO FICOU EM -   R$ %.2f    ") % total_pc4
                    print


    elif opcao == '5':
                        print
                        print                    "    [!]    O valor para desenvolvimento é hospedagem é de R$ 600,00  [!] "
                        print                    "    [!]          Site SEGUROS,RESPONSIVOS,RÁPIDOS e BONITOS !        [!] "
                        print                    "    [!] Sites feitos sob medida, e atendendo os criterios do cliente [!] "
                        print
                        print                                     "  Digite [0] para fechar o script "
                        print
                        
                        work_pc5      = input   ( "    Quantos websites serão criados e hospedados ?   ")
                        total_pc5     = work_pc5 * web_builder
                        print                   ("    O VALOR DO SERVIÇO FICOU EM -  R$ %.2f   ") % total_pc5
                        print


    elif opcao == '6':
                            print
                            print                    "    [!]          O valor mensal a ser pago é de R$ 200,00            [!] "
                            print                    "    [!] Consultar tabela de precos para atendimentos corporativos    [!] "
                            print                    "    [!] O valor so será pago se as metas de tráfegos forem atingidas [!] "
                            print
                            print                                     "  Digite [0] para fechar o script "
                            print
                            
                            work_pc6      = input   ( "    Necessita de suporte SEO por quantos meses  ?   ")
                            total_pc6     = work_pc6 * web_seo
                            print                   ("    O VALOR DO SERVIÇO FICOU EM -   R$ %.2f   ") % total_pc6
                            print


    elif opcao == '7':
                                print
                                print                    "    [!] Os serviços prestados via contrato funcionarão da seguinte forma [!]  "
                                print                    "    [!]   2 visitas por mês + diagnóstico de sistema + limpeza completa  [!]  "
                                print
                                print                    "    [!]           O valor para cada  WORKSTATION é de R$ 69,90           [!]  "
                                print
                                print                                     "  Digite [0] para fechar o script "
                                print
                                
                                work_pc7      =  input   ( "    Há quantos computadores na empresa  ?    ")
                                total_pc7     =  work_pc7 * deal_contract
                                print
                                contract      =  input   ( "    Digite o tempo de suporte [3] , [6] , [12]  ")
                                print

                                if   contract  == 3:
                                    print ("    O VALOR TOTAL DO CONTRATO MENSAL É DE R$  %.2f  ") % total_pc7
                                    print
                                elif contract  == 6:
                                    print ("    O VALOR TOTAL DO CONTRATO MENSAL É DE R$  %.2f  ") % total_pc7
                                    print
                                elif contract  == 12:
                                    print ("    O VALOR TOTAL DO CONTRATO MENSAL É DE R$  %.2f  ") % total_pc7
                                print



    # Se a opção escolhida for igual a 0, o script será finalizado
    
    elif opcao == '0':
        sys.exit()

    # Se uma letra,símbolo ou caractere especial for digitado, o script chama o menu novamente
    
    else:
        menu_opcao()

menu_opcao() # Inicia o script antes do loop

# Enquanto a função menu_opcao receber qualquer valor diferente de 0, o script irá continuar perguntando sobre o que deseja fazer.

while menu_opcao != 0:
    
    # Verificação de fluxo

    print      
    
    # Aqui usa-se raw_input por conta de receber dados strings

    verific = raw_input ("    [!]   Deseja fazer outro orçamento [ Sim ] ou [ Não ] ?  [!]  ")

    # Bloco de corte de fluxo
    # Se o usuário digitar 'sim' o código retorna ao menu() e ao menu_opcoes() , com isto a pessoa tem controle total sobre o script
    
    if verific == 'sim':
        menu_opcao()
    
    # Qualquer coisa diferente de 'sim' irá automaticamente fechar o script

    elif verific != 'sim':
        sys.exit()

    # Falta printar o total do orçamento

# Inicia o menu de opções

menu_opcao() 
