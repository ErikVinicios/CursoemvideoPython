def area(largura,comprimento):
    a = largura * comprimento
    print(f'A area do terreno {largura}m X {comprimento}m é {a}m²')


l = float(input('Largura: '))
c = float(input('Comprimento: '))
area(l,c)