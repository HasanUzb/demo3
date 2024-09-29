def juftlar_yegindisi(list1):
    yigindi = 0
    for son in list1:
        if son % 2 == 0:
            yigindi += son
    return yigindi

sonlar = [1, 2, 3, 4, 5]

natija = juftlar_yegindisi(sonlar)
print(f"Juft sonlarni yigindisi: {natija}")