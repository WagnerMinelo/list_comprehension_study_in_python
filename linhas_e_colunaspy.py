# list comprehension
# for x in range(1, 11):
#     for y in range(1, 5):
#         print(x, y)

linha_e_colunas = [
    (x, y)
    if y != 2 else (x, y * 1000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2
]


print(linha_e_colunas)
