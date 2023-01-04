tarifa = 2.20
dias = 31

respostaSaldo = input('Você ainda possui saldo no cartão? [S/N]').upper()
if respostaSaldo == 'S':
    saldoRemanescente = float(input('Digite o saldo que resta no seu passe: '))
respostaTarifa = input(f'O valor da tarifa estudantil ainda é R${tarifa}? [S/N]').upper()
if respostaTarifa == 'N':
    tarifa = float(input('Insira o novo valor: '))
valor = float(input('Digite o valor que você recebeu de passagem: '))
viagens = int(input('Quantas viagens você faz por dia? '))
    
viagensMensais = viagens * dias
custoMensal = tarifa * viagensMensais
if saldoRemanescente > 0:
    abastecimentoMes = custoMensal - saldoRemanescente
saldo = valor - abastecimentoMes

print('==========================================================')
print(f'Seu custo mensal com passagens é de: {custoMensal:.2f}')
print(f'Você recebeu R${valor:.2f} em passagens')
if respostaSaldo == 'S':
    print(f'Esse mês você só vai precisar abastecer R${abastecimentoMes:.2f}')
if saldoRemanescente > 0:
    print(f'Você tem R${saldoRemanescente:.2f} no seu cartão referente ao mês passado')
if saldo > 0:
    print(f'Sobrou R${saldo:.2f} para você')
print('==========================================================')
if custoMensal > valor:
    diferenca = custoMensal - valor
    print(f'Você terá que desembolsar R${diferenca:.2f} para ter todas as passagens do mês')
    print('=====================================================================')
