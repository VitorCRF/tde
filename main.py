qnt_Moedas_1 = int(input('Digite a quantidade de moedas de 1 real: '))
qnt_Moedas_050 = int(input('Digite a quantidade de moedas de 50 centavos: '))
qnt_Moedas_025 = int(input('Digite a quantidade de moedas de 25 centavos: '))
qnt_Moedas_010 = int(input('Digite a quantidade de moedas de 10 centavos: '))
qnt_Moedas_005 = int(input('Digite a quantidade de moedas de 5 centavos: '))
caixa = ((qnt_Moedas_1 * 1) + (qnt_Moedas_050 * 0.5) + (qnt_Moedas_025 * 0.25)+(qnt_Moedas_010 * 0.10) + (qnt_Moedas_005 * 0.05))

while True:
    troco1 = int(0)
    troco050 = int(0)
    troco025 = int(0)
    troco010 = int(0)
    troco005 = int(0)

    valorGasto = float(input('Digite o valor gasto pelo cliente: '))
    valorPago = float(input('Digite o valor pago pelo cliente: '))
    if valorPago >= valorGasto:
        diferenca = valorPago - valorGasto
        diferenca = round(diferenca,2)
        if caixa >= diferenca:
            while round(diferenca,2) >= 1.0 and qnt_Moedas_1 > 0:
                diferenca = round(diferenca,2) - 1.0
                troco1 = troco1 + 1
                qnt_Moedas_1 = qnt_Moedas_1 - 1.0
            while round(diferenca,2) >= 0.50 and qnt_Moedas_050 > 0:
                diferenca = round(diferenca,2) - 0.50
                troco050 = troco050 + 1
                qnt_Moedas_050 = qnt_Moedas_050 - 1.0
            while round(diferenca,2) >= 0.25 and qnt_Moedas_025 > 0:
                diferenca = round(diferenca,2) - 0.25
                troco025 = troco025 + 1
                qnt_Moedas_025 = qnt_Moedas_025 - 1.0
            while round(diferenca,2) >= 0.10 and qnt_Moedas_010 > 0:
                diferenca = round(diferenca,2) - 0.10
                troco010 = troco010 + 1
                qnt_Moedas_010 = qnt_Moedas_010 - 1.0
            while round(diferenca,2) >= 0.05 and qnt_Moedas_005 > 0.0:
                diferenca = diferenca - 0.05
                troco005 = troco005 + 1
                qnt_Moedas_005 = qnt_Moedas_005 - 1.0
            print('O cliente receberá {} moedas de 1 real, {} moedas de 50 centavos, {} moedas de 25 centavos, {} moedas de 10 centavos e {} moedas de 5 centavos'.format(troco1, troco050, troco025, troco010, troco005))
        else:
            print('Dinheiro do caixa é insuficiente para o troco')
    else:
        print('Dinheiro do cliente é insuficiente para fazer esta compra')