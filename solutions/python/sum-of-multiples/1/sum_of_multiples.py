def sum_of_multiples(limit, multiples):
    multiples_dict = {}

    for num in multiples:
        if num == 0: continue
        i = 1
        multiples_dict[num] = set()
        while num*i < limit:
            multiples_dict[num].add(num*i)
            i += 1

    combined_set = set()

    for mult in multiples_dict.values():
        combined_set = combined_set | mult

    return sum(combined_set)
