def teskari_dictionary(dict1):

    teskari_dict = {}

    for key, value in dict1.items():
       teskari_dict[value] = key

    return teskari_dict


haqiqiy_dict = {1: "a", 2: "b"}
result = teskari_dictionary(haqiqiy_dict)
print(result)
