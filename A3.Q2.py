# 2.Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
# mostrando uma mensagem de erro e voltando a pedir as informações.

Usuario = str (input("informe o usuario:"))
Senha = str (input("informe a senha:"))
while Usuario == Senha:
  Senha = str (input("A senha tem que ser diferente do usuario,informe outra senha: "))
print ("Usuario:" , Usuario )
print ("Senha:" , Senha)