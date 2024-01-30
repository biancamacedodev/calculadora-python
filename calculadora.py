#op = input('Escolha uma operaçao (adiçao, subtraçao, multiplicaçao e divisao): ')

def fabricaOp(operacao):

    def adiçao(*args):
        return sum(args)
    
    def subtraçao(*args):
        resultado = args[0]
        for num in args[1:]:
            resultado -= num
        return resultado
    
    def multiplicaçao(*args):
        resultado = 1
        for num in args:
            resultado *= num
            return resultado
        
    def divisao(*args):
        resultado = args[0]

        for num in args[1:]:
            if num == 0:
                raise ValueError('Divisao por zero nao é permitida.')
            resultado /= num
        return resultado
    
    if operacao == 'adiçao':
        return adiçao
    
    elif operacao == 'subtraçao':
        return subtraçao

    elif operacao == 'multiplicaçao':
        return multiplicaçao

    elif operacao == 'divisao':
        return divisao    

adicionar = fabricaOp('adiçao')
print(adicionar(5, 5, 5, 5))

subtrair = fabricaOp('subtraçao')
print(subtrair(50, 10, 10))

multiplicar = fabricaOp('multiplicaçao')
print(multiplicar(10, 5))

divisao = fabricaOp('divisao')
print(divisao(20, 5))