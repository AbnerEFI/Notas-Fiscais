import os
import pdfplumber
import pandas as pd

os.chdir('\\\DESKTOP-NV8NNKF\\Compartilhada\\Obras')
obras= os.listdir()
NOTAS=[]

for j in range(len(obras)):
    
    #####################################
    ##                                 ##
    ##        NOTAS DE SERVIÇO         ##
    ##                                 ##
    #####################################
    
        #NOTAS SERVIÇO A RECEBER
        print(obras[j])
        path='\\\DESKTOP-NV8NNKF\\Compartilhada\\Obras\\'+ obras[j]+ '\\NOTAS DE SERVIÇO\\NOTAS A RECEBER'
        try:
            os.chdir(path)
            notas=os.listdir()
            for i in range(len(notas)):
                try:
                    pdf=pdfplumber.open(notas[i])
                    paginas=pdf.pages
                    texto=paginas[0].extract_text()
                    lines=texto.count('\n')
                    numero= texto.split('\n')[2]
                    emissao= texto.split('\n')[4]
                    cliente= texto.split('\n')[15].split(':')[1]
                    liquido= 'Total Líquido (R$)'
                    for k in range(lines):
                        info = texto.split('\n')[k]
                        if liquido in info:
                            valor= info.split(' ')[3]
                    situacao= 'a receber'
                    obra= obras[j]
                    situacao_obra= 'em andamento'
                    tipo='serviço'
                    dados=[numero, tipo, cliente, obra, situacao_obra, situacao, valor, emissao]
                    NOTAS.append(dados)
                except:
                    print('nota com problema')
                    continue
        except:
            print('Problemas com NOTAS DE SERVIÇO A RECEBER')


        #NOTAS SERVIÇO RECEBIDAS
        try:
            path='\\\DESKTOP-NV8NNKF\\Compartilhada\\Obras\\'+ obras[j]+ '\\NOTAS DE SERVIÇO\\NOTAS RECEBIDAS'
            os.chdir(path)
            notas=os.listdir()
            for i in range(len(notas)):
                try:
                    pdf=pdfplumber.open(notas[i])
                    paginas=pdf.pages
                    texto=paginas[0].extract_text()
                    lines=texto.count('\n')
                    numero= texto.split('\n')[2]
                    emissao= texto.split('\n')[4]
                    cliente= texto.split('\n')[15].split(':')[1]
                    liquido= 'Total Líquido (R$)'
                    for k in range(lines):
                        info = texto.split('\n')[k]
                        if liquido in info:
                            valor= info.split(' ')[3]
                    situacao= 'recebida'
                    obra= obras[j]
                    situacao_obra= 'em andamento'
                    tipo='serviço'
                    dados=[numero, tipo, cliente, obra, situacao_obra, situacao, valor, emissao]
                    NOTAS.append(dados)
                except:
                     print('nota com problema')
                     continue
        except:
            print('Problemas com NOTAS DE SERVIÇO RECEBIDAS')
    
        #NOTAS SERVIÇO CANCELADAS
        try:
            path='\\\DESKTOP-NV8NNKF\\Compartilhada\\Obras\\'+ obras[j]+ '\\NOTAS DE SERVIÇO\\NOTAS CANCELADAS'
            os.chdir(path)
            notas=os.listdir()
            for i in range(len(notas)):
                try:
                    pdf=pdfplumber.open(notas[i])
                    paginas=pdf.pages
                    texto=paginas[0].extract_text()
                    lines=texto.count('\n')
                    numero= texto.split('\n')[2]
                    emissao= texto.split('\n')[4]
                    cliente= texto.split('\n')[15].split(':')[1]
                    liquido= 'Total Líquido (R$)'
                    for k in range(lines):
                        info = texto.split('\n')[k]
                        if liquido in info:
                            valor= info.split(' ')[3]
                    situacao= 'cancelada'
                    obra= obras[j]
                    situacao_obra= 'em andamento'
                    tipo= 'serviço'
                    dados=[numero, tipo, cliente, obra, situacao_obra, situacao, valor, emissao]
                    NOTAS.append(dados)
                except:
                    print('nota com problema')
                    continue
        except:
            print('Problemas com NOTAS DE SERVIÇO CANCELADAS')

    #####################################
    ##                                 ##
    ##       NOTAS DE MATERIAL         ##
    ##                                 ##
    #####################################
    
    
        #NOTAS MATERIAL A RECEBER
        print(obras[j])
        try:
            path='\\\DESKTOP-NV8NNKF\\Compartilhada\\Obras\\'+ obras[j]+ '\\NOTAS DE MATERIAL\\NOTAS A RECEBER'
            os.chdir(path)
            notas=os.listdir()
            for i in range(len(notas)):
                try:
                    pdf=pdfplumber.open(notas[i])
                    paginas=pdf.pages
                    texto=paginas[0].extract_text()
                    numero= texto.split('\n')[2]
                    emissao= texto.split('\n')[21].split(' ')[-1]
                    cliente= texto.split('\n')[21].split(' ')[0] 
                    valor = texto.split('\n')[31].split(' ')[-1]
                    situacao= 'a receber'
                    tipo= 'material'
                    obra= obras[j]
                    situacao_obra= 'em andamento'
                    dados=[numero, tipo, cliente, obra, situacao_obra, situacao, valor, emissao]
                    NOTAS.append(dados)
                except:
                    print('nota com problema')
                    continue
        except:
            print('Problemas com NOTAS DE MATERIAL A RECEBER')
                

  
        #NOTAS MATERIAL RECEBIDAS
        path='\\\DESKTOP-NV8NNKF\\Compartilhada\\Obras\\'+ obras[j]+ '\\NOTAS DE MATERIAL\\NOTAS RECEBIDAS'
        try:
            os.chdir(path)
            notas=os.listdir()
            for i in range(len(notas)):
                try:
                    pdf=pdfplumber.open(notas[i])
                    paginas=pdf.pages
                    texto=paginas[0].extract_text()
                    numero= texto.split('\n')[2]
                    emissao= texto.split('\n')[21].split(' ')[-1]
                    cliente= texto.split('\n')[21].split(' ')[0] 
                    valor = texto.split('\n')[31].split(' ')[-1]
                    situacao= 'a receber'
                    tipo= 'material'
                    obra= obras[j]
                    situacao_obra= 'em andamento'
                    dados=[numero, tipo, cliente, obra, situacao_obra, situacao, valor, emissao]
                    NOTAS.append(dados)
                except:
                    print('nota com problema')
        except:
            print('Problemas com NOTAS DE MATERIAL RECEBIDAS')

    
        #NOTAS MATERIAL CANCELADAS
        path='\\\DESKTOP-NV8NNKF\\Compartilhada\\Obras\\'+ obras[j]+ '\\NOTAS DE MATERIAL\\NOTAS CANCELADAS'
        try:
            os.chdir(path)
            notas=os.listdir()
            for i in range(len(notas)):
                try:
                    pdf=pdfplumber.open(notas[i])
                    paginas=pdf.pages
                    texto=paginas[0].extract_text()
                    numero= texto.split('\n')[2]
                    emissao= texto.split('\n')[21].split(' ')[-1]
                    cliente= texto.split('\n')[21].split(' ')[0] 
                    valor = texto.split('\n')[31].split(' ')[-1]
                    situacao= 'a receber'
                    tipo= 'material'
                    obra= obras[j]
                    situacao_obra= 'em andamento'
                    dados=[numero, tipo, cliente, obra, situacao_obra, situacao, valor, emissao]
                    NOTAS.append(dados)
                except:
                    print('nota com problema')
                    continue
        except:
            print('Problemas com NOTAS DE MATERIAL CANCELADAS')
                
    


dataframe=pd.DataFrame(NOTAS, columns=['N°', 'TIPO', 'CLIENTE', 'OBRA', 'SITUAÇÃO OBRA', 'SITUAÇÃO NOTA', 'VALOR', 'EMISSÃO'])
print(dataframe)
#SALVA DATAFRAME COMO PLANILHA NA PASTA ABNER#
os.chdir('C:\\Users\\Julio\\Desktop\\Abner\\planilhas')
dataframe.to_excel('NOTAS.xlsx')


