def maior(* tupla_num):
    maior_num = ct = 0
    for numero in tupla_num:
        if ct == 0:
            maior_num = numero
        else:
            if numero > maior_num:
                maior_num = numero
        ct += 1
    print(maior_num)

maior(1, 3, 5, 8, 12, 65, 23, 12, 95, 34, 7)
maior(3, 4, 5, 1, 8, 9, 4)
maior(2)
maior()
