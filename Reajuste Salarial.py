s = float(input('Digite o salário do funcionário: '))

if s < 500:
    a = float(s*0.15)
    sa = float(s+a)
    print('O sálario reajustado corresponde a: {}'.format(sa))
elif s >= 500 and s <= 1000:
    a = float(s*0.10)
    sa = float(s+a)
    print('O sálario reajustado corresponde a: {}'.format(sa))
elif s > 1000:
    a = float(s*0.05)
    sa = float(s+a)
    print('O sálario reajustado corresponde a: {}'.format(sa))