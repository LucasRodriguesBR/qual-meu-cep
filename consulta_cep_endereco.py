import requests
import json

validacao = False

while validacao == False:

    uf = str(input('Digite a sua UF')).upper().strip()
    cidade = str(input('Digite a sua cidade')).title().strip()
    endereco = str(input('Digite o seu endereco')).title().strip()


    if len(uf) < 2:
        print('UF invalida. Tente novamente')
    elif len(cidade) < 3:
        print('Cidade inválida. Tente novamente')
    elif len(endereco) < 3:
        print('Endereço inválido. Tente novamente')
    else:
        validacao = True

print('PESQUISANDO. Aguarde um momento...')

requisicao = requests.get('https://viacep.com.br/ws/{}/{}/{}/json'.format(uf, cidade, endereco))
dic_requisicao = requisicao.json()

for c in dic_requisicao:
    dicionario = (dic_requisicao[0])

#Tratamento de dados
if endereco in dicionario['logradouro']:
    print('O seu CEP é:{}'.format(dicionario['cep']))
    print('''O endereço é:\nLogradouro: {}, Complemento:{}, Bairro: {}'''
      .format(dicionario['logradouro'],dicionario['complemento'], dicionario['bairro']))
else:
    print('CEP/ENDEREÇO DESCONHECIDO. Tente novamente!')

print('***'*30)
print('Com orgulho, desenvolvido por Lucas Rodrigues enquanto ainda estuda Python')
print('***'*30)

