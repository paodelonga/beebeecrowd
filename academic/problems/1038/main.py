"""
### Sobre
Com base na tabela abaixo, escreva um programa que leia o
código de um item e a quantidade deste item.
A seguir, calcule e mostre o valor da conta a pagar.

| CODIGO |  PRECO  |
| :----: | :-----: |
| 1      | R$ 4.00 |
| 2      | R$ 4.50 |
| 3      | R$ 5.00 |
| 4      | R$ 2.00 |
| 5      | R$ 1.50 |


### Entrada
O arquivo de entrada contém dois valores inteiros correspondentes ao código e à quantidade de um item conforme tabela acima.

### Saída
O arquivo de saída deve conter a mensagem "Total: R$ " seguido pelo valor a ser pago, com 2 casas após o ponto decimal.
"""



items = {
    1: 1.50,
    2: 2.00,
    3: 4.00,
    4: 4.50,
    5: 5.00
}


idx = int(input())
qtd = int(input())

print(f"Total: R$ {(items[idx] * qtd):.2f}")
