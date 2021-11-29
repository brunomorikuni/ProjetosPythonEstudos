lista = ["roupa","calça", "sapato", "camisa", "meia", "bone" ]

i = 0 

item_procurado = input("escolha um item")

achou = False

while i < len[i]:
    if lista[i] == item_procurado:
        print("esntramos esse item %s" % item_procurado)
        achou = True
    i = i + 1
if achou == False:
    print("na chou o item %s" % item_procurado)