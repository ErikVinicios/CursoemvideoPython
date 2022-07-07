times = ('Atlético-MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino','Fluminense','América-MG',
         'Atlético-GO', 'Santos','Ceará-SC','Internacional','São Paulo','Athlético-PR','Cuiabá','Juventude','Grêmio',
         'Bahia','Sport Recife','Chapecoense')
print('')
print('-='* 1000)
print(f'Lista do \033[1:37mBRASILEIRÃO\033[m: \033[1:37m{times}\033[m')
print('-='* 100)
print(f'Os CINCO \033[1:32mPRIMEIROS COLOCADOS\033[m são: \033[1:32m{times[:5]}\033[m')
print('-='* 100)
print(f'Os \033[1:31mÚLTIMOS QUATRO COLOCADOS\033[m são: \033[1:31m{times[-4:]}\033[m')
print('-='* 100)
print(f'O time da \033[1:32mCHAPECOENSE\033[m, atualmente, está na \033[1:32m{times.index("Chapecoense")+1}ª posição\033[m')