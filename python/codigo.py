faturamento = 1000 #tipo int -> numero inteiro
custo = 700.32 #tipo float -> numeor casa decimal
novas_vendas = 100
faturamento = faturamento + novas_vendas
imposto = faturamento * 0.10 
lucro = faturamento-custo - imposto
margem_lucro = lucro / faturamento


print("Faturamento foi de ",faturamento)
print("O custo foi de ",custo)
print("O lucro foi de ",lucro)
print("A margem de lucro foi de ", round(margem_lucro,2))

mensagem = "O faturamento de loja foi de tanto"
email = "emailqualquer@gmail.com"

teve_lucro = True



