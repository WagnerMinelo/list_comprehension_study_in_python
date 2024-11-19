# list comprehension
nomes = ['wagner', 'bruno', 'soares', 'vitor']
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]

print(novos_nomes)
