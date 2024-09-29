def tuple_funksiya(tuple1):
    if not tuple1:
        raise ValueError("Tupleni ichi bosh")

    max_value = tuple1[0]
    for numbers in tuple1:
        if numbers > max_value:
            max_value = numbers
    return max_value

tuple2 = (33, 1, 4, 1, 5, 9, 2, 6)
natija = tuple_funksiya(tuple2)
print(f"Tupledagi eng kotta qiymat: {natija}")
