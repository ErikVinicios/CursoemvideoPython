aluno = {}
aluno['Nome'] = str(input('Nome: ')).strip().title()
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 7:
    aluno['Resultado'] = '\033[1:32mAPROVADO\033[m'
elif aluno['Média'] >= 5:
    aluno['Resultado'] = '\033[1:36mRECUPERAÇÃO\033[m'
else:
    aluno['Resultado'] = '\033[1:31mREPROVADO\033[m'
print('-='*30)
for k,v in aluno.items():
    print(f'{k}: {v}')
print('-='*30)
