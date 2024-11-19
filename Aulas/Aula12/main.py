from Pessoa import *
res=0
import os

def pergunta():
    res = int(input("deseja cadastrar uma nova pessoa? 1 - sim ou 0 - nao: "))
    return res

cadastro = []

res = pergunta()
while(res == 1):
    nome = str(input("digite o nome: "))
    idade = int(input("digite a idade: "))
    cargo = str(input("digite o cargo: "))
    salario = float(input("digite o salario: "))

    cadastro.append(Pessoa.Pessoa(nome,idade,cargo,salario))
    res = pergunta()

def mostrar():
    print("{:<4}{:<10}{:<7}{:<10}{:<7}" 
    .format ("N°","nome","idade","cargo","salario"))
for x in cadastro:
    print("{:<4}{:<10}{:<7}{:<10}{:<7}"
      .format(y,
            x.get_cargo(),
            x.get_idade(),
            x.get_nome(),
            x.get_salario(),
    ))
    y =+ 1
def alterar (x,y,z):
    if(y==0): cadastro[x] .set_nome(z)
    if(y==1): cadastro[x] .set_idade(z)
    if(y==2): cadastro[x] .set_cargo(z)
    if(y==3): cadastro[x] .set_salario(z)
mostrar()