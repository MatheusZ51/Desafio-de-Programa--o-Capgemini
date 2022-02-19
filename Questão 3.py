palavra = input('Digite uma palavra: ')
pares = []

for i in range(len(palavra)):
    for j in range(len(palavra)):
        L = len(palavra[i:j])
        if j > i:
            x = i + 1
            while x < len(palavra):
                subpalavra_1 = palavra[i:j]
                subpalavra_2 = palavra[x:x+L]
                if len(subpalavra_1) == len(subpalavra_2):  
                    dict_sub_1 = {i: subpalavra_1.count(i) for i in subpalavra_1}
                    dict_sub_2 = {i: subpalavra_1.count(i) for i in subpalavra_2}
                    if dict_sub_1 == dict_sub_2:
                        pares.append(tuple([subpalavra_1, subpalavra_2]))

                x = x + 1

print(*pares, sep=' ')
print(len(pares))