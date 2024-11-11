# Receber a lista do usuário
10,20,30,40,50
entrada = input()
# Convertee a string de entrada em uma lista de números
numeros_str = ["10", "20", "30", "40", "50"]
lista = [float(x.strip()) for x in entrada.split(',')]

# Calcula a soma dos números na lista
soma = sum(lista)
# Calcula a quantidade de elementos na lista
quantidade = len(lista)
# TODO: Calcule a média aritmética:
media = soma / quantidade

# Exibir a média com duas casas decimais
print(f'{media:.1f}')