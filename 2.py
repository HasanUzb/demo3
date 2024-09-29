def unli_harflar(list1):

    unlilar = "aouie"
    total = 0

    for harf in list1:
        if harf.lower() in unlilar:
            total += 1

    return total

natija = unli_harflar("Xasan va Xusan")
print(f"Unli harfla: {natija}")
