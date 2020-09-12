r1 = float(input('Digite o valor da primeira reta: '))
r2 = float(input('Digite o valor da segunda reta: '))
r3 = float(input('Digite o valor da terceira reta: '))
t = bool(False)

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1+ r2:
    print('As retas acima podem formar um triângulo')
    t = True
else:
    print('As retas acima NÃO podem formar um triângulo')
    t = False
    
if t == True and r1 != r2 and r1 != r3 and r2 != r3:
    print('O triângulo é ESCALENO')
elif t == True and r1 == r2 and r1 != r3 or t == True and r1 == r3 and r1 != r2 or t == True and r2 == r3 and r2 != r1:
    print('O triângulo é ISÓCELES')
elif t == True and r1 == r2 and r1 == r3:
    print('O triângulo é EQUILÁTERO')