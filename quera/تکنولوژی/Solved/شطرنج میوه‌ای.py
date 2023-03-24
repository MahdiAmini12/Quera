def fruits(tuple_of_fruits):
    good_fruits = {}
    for fruit in tuple_of_fruits:
        if fruit['shape'] == 'sphere' and 300 <= fruit['mass'] <= 600 and 100 <= fruit['volume'] <= 500:
            if fruit['name'] in good_fruits:
                good_fruits[fruit['name']] += 1
            else:
                good_fruits[fruit['name']] = 1
    return good_fruits
