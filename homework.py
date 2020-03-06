def odd_even(given_list):
    odd = 0
    even = 0
    result = {"Odd Numbers:": [],"Even Numbers:": [],"Even_nums": even,"Odd_nums": odd}

    for x in given_list:
        if x % 2 == 0:
            result["Even Numbers:"].append(x)
            even += 1
            result.update({"Even_nums": even})

        else:
            result["Odd Numbers:"].append(x)
            odd += 1
            result.update({"Odd_nums": odd})



    return result


#test
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(odd_even(list2))
