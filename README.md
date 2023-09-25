# Notas-Fiscais
Acessa PDF de notas fiscais de serviço e de venda, retira informações, exporta na forma de planilha. As notas fiscais devem estar separadas em pastas dferentes, a separação utilizada, foi pelo tipo de nota (serviço ou venda) e por situação, isto é, se a nota foi paga, cancelada, ou a receber. Destina-se a notar emitidas pela empresa (notas de crédito).
# Ferramenta utilizada
A ferramenta utilizada para obtenção dos dados foi a biblioteca 'pdfplumber' obtendo os dados usando como referência, palavras e caracteres etruturais no documento.
# Modelos de NF utilizados
O modelo de NF de serviço utilizado está exemplificado a seguir:
![NFS](https://github.com/AbnerEFI/Notas-Fiscais/assets/145677273/110f8183-1374-4079-b987-c480be48cab7)

O modelo de NF de vanda utilizado esta exemplificado a seguir:
![NF venda](https://github.com/AbnerEFI/Notas-Fiscais/assets/145677273/3610fb12-4fba-4228-a4f5-8369f70fe83c)
# Porque PDF?
O PDF é a extenção mais utilizada na empresa, seria possível trabalhar com XML, porém, para isso seria necessário gerir mais um arquivo, isto é, toda movimentação relacionada a notas ficas usa o modelo PDF, sendo inviável por enquato a utilização de XML. Outro fator é que o volume de notas emitidas é baixo em comparação as notas recebidas. Para notas recebidas é utilizado o arquivo XML.
