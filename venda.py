def Venda(nomeprod,qtd,produtos):
    qtdest=int(0)
    for obj in produtos:
        if(obj.nomeProduto == nomeprod):
            qtdest+=1
    if qtdest==0:
        print("Produto não localizado/sem estoque!")
        return False
    elif qtd>qtdest:
        print("Quantidade excede o estoque!")
        return False
    else:
        x=int(0)
        while qtd > 0:
            print(x)
            if(produtos[x].nomeProduto == nomeprod):
                del(produtos[x])
                x-=1
                qtd-=1
            x+=1
        return True