'''
Challenge: Desenvolvedor Python
Desafio:

Lucro da ação

O senhor e-Deployer gostaria de comprar uma ação e vendê-la em um curto espaço de tempo, mas apenas se esta operação dê lucro. Para isso, é passado um array K com os valores das ações nos determinados dias, onde ele poderá escolher onde comprar e vender.

Determine o maior lucro dado esse array K de preços.

Exemplo 1:

Input: [7,1,5,3,6,4]

Output: 5

Explicação: Este valor acontece quando compramos a ação no 2o dia e a vendemos no 5o dia (6 - 1)
Exemplo 2:

Input: [7,6,4,3,1]

Output: 0

Explicação: Neste caso, não há nenhuma operação que possa ser feita que dê lucro.
'''

def calc_lucro(K):
    result = []
    for value in enumerate(K):
        if value[0]+1 < len(K):
            result.append(max(list(map(lambda x: x - value[1] , K[value[0]+1:]))))
    if max(result) < 0:
        return 0
    return max(result)

print(calc_lucro([7,1,5,3,6,4]))
print(calc_lucro([7,6,4,3,1]))