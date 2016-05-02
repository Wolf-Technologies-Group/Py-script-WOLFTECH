# -*- coding: utf-8 -*-
#######        Tabela de serviços WT 2016       ########
########      Creator - Victor Consuegra       ########
##########           21/02/2016               ########
###########           Versão  1.3          #########


#Declaração de variáveis / Operacional

wolf_service = 100         # Formatação completa + Backup + Limpeza + Pasta térmica + Report completo do sistema
clean        = 40          # Custo de uma limpeza completa
backup       = 35          # Custo de um backup sem nenhum adicional
wolf_search  = 75          # Custo de uma análise de sistema em busca de vírus,malwares,trojans etc.
web_builder  = 600         # Criação de site + Domínio + Hospedagem + Manutenção mensal
web_seo      = 200         # Manutenção de contéudo + Técnicas de SEO + Marketing cobrado por MÊS

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
# Taxa fixa de R$ 40,00 por WORKSTATION

deal_3_mouths  = 40 # 2 visitas por mês durante 3 meses ,  Manutenção + Diagnóstico de sistema + Limpeza
deal_6_mouths  = 40 # 2 visitas por mês durante 6 meses ,  Manutenção + Diagnóstico de sistema + Limpeza
deal_12_mouths = 40 # 2 visitas por mês durante 12 meses , Manutenção + Diagnóstico de sistema + Limpeza

#Início da interatividade do script

print '##' * 80
print
print "     [1] Limpeza + Formatação + Backup + Report completo do sistema "
print "     [2] Limpeza completa "
print "     [3] Backup de dados"
print "     [4] Análise de sistema + remoção de vírus,trojan, malware etc. "
print "     [5] Criação de sites pessoais ou profissionais "
print "     [6] Impulso de web SEO + Marketing digital "
print
print '##' * 80
service = input (" Escolha o plano desejado ")
print
print '--' * 80

# Início dos cálculos baseados na escolha de serviço

# Opção [1] Limpeza + Formatação + Backup + Report de sistema
# Informativo sobre os descontos promocionais de acordo com o número de computadores

if service == 1 :
    pc = input (" Quantos computadores serão atendidos  ?  ")
    print
    total_pc = wolf_service * pc
    print       " O Custo total do serviço é de: R$ %.2f  " % total_pc
    if pc == 3 :
        print   " O Valor do pacote de 3 WORKSTATIONS é de : R$ %.2f    "  % pacote_3_pc
        print '--' *  80
        print
    if pc == 5 :
        print   " O Valor do pacote de 5 WORKSTATIONS é de : R$ %.2f    "  % pacote_5_pc
        print '--'  * 80
        print
    if pc == 10 :
        print   " O valor do pacote de 10 WORKSTATIONS é de : R$ %.2f   "  % pacote_10_pc
        print '--' *  80
        print
    if pc == 15 :
        print   " O valor do pacote de 15 WORKSTATIONS é de : R$ %.2f   "  % pacote_15_pc
        print '--' *  80
        print
    if pc == 20 :
        print   " O valor do pacote de 20 WORKSTATIONS é  de : R$ %.2f    " % pacote_20_pc
        print '--' *  80
        print
    if pc == 25 :
        print   " O valor do pacote de 25 WORKSTATIONS é de  : R$ %.2f    " % pacote_25_pc
        print '--' *  80
        print
    if pc == 30 :
        print   " O valor do pacote de 30 WORKSTATIONS é de  : R$ %.2f    " % pacote_30_pc
print '==' * 80


#Opção [2] Limpeza completa

if service == 2 :
    pc_2      = input (" Quantos computadores serão atendidos ?  ")
    total_pc2 = clean * pc_2
    print              "O Custo total do serviço é de: R$ %.2f  " % total_pc2
    print '==' * 80



#Opção [3] Backup de dados


if service == 3 :
    pc_3      = input (" Quantos computadores serão atendidos ?  ")
    total_pc3 = backup * pc_3
    print              " O custo total do serviço é de : R$ %.2f  " % total_pc3
    print '==' * 80



#Opção [4] Análise e diagnóstico de sistema para possivéis ameaças


if service == 4 :
    pc_4      = input  (" Quantos computadores serão atendidos ?  ")
    total_pc4 = wolf_search * pc_4
    print               " O custo total do serviço é de : R$ %.2f  " % total_pc4
    print '==' * 80



#Opção [5] Criação de web sites pessoais e profissionais


if service == 5 :
    web       = input     (" Quantos websites serão criados  ? ")
    total_web = web_builder * web
    print                  " O custo total do web site é de : R$ %.2f   " % total_web
    print '==' * 80


#Opção [6] Impulso de WEB SEO + Marketing digital


if service  == 6 :
    seo        = input     (" Por quantos meses irá precisar de suporte SEO ?   ")
    total_web2 = web_seo * seo
    print                 " O custo total do impulso de SEO será de : R$ %.2f   " %total_web2
    print '==' * 80


