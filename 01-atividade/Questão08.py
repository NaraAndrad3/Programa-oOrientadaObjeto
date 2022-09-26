def ingressos(preco, quant):
    i=1
    max =0
    lucro = preco*quant
    if quant == 0:
        return 0
    else:
        while preco >i:
            print('Preço do ingresso = ', preco,'Quantidade = ', quant,'Lucro = ', lucro-200)
            quant = quant + 26
            preco = preco - 0.50
            lucro = quant*preco
            
        i+=1        
preco = 5.00
quant = 120

ingressos(preco, quant)
