from math import sin,cos,tan,radians

ang = float(input('Digite o angulo: '))

print(f'Seno: \033[36m{sin(radians(ang)):.2f}\033[m\nCosseno: \033[35m{cos(radians(ang)):.2f}\033[m\nTangente: \033[33m{tan(radians(ang)):.2f}\033[m')