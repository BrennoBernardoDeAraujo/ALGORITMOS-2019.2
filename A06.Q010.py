# Imprimir as n primeiras linhas do triângulo de Pascal:

def trianguloPascal(n):
  lista = [[1],[1,1]]
  for i in range(1,n):
    linha = [1]
    for j in range(0,len(lista[i])-1):
      linha += [ lista[i][j] + lista[i][j+1] ]
    linha += [1]
    lista += [linha]
  return lista

n = int(input("Digite o número de linhas para o triângulo de Pascal: "))
resultado = trianguloPascal(n-1)

for i in range(len(resultado)):
  print(resultado[i])

# Observacoes 
# 1 - Todo primeiro e ultimo elemento x da linha e = 1;
# 2 - O elemento x2 de cada linha e a soma do x1 + x2 dos elementos da linha anterior
# 3 - O elemento x3 de cada linha e a soma do x2 + x3 dos elementos da linha anterior
# 4 - O elemento x4 de cada linha e a soma do x3 + x4 dos elementos da linha anterior  