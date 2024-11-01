def getOneBits(n):
    binary = []
    results = [0]
    cur_num = n
    while cur_num != 1:
        if cur_num % 2 == 1:
            binary.append(1)
            results[0] = results[0] + 1
        else:
            binary.append(0)
        cur_num = cur_num // 2

    if cur_num == 1:
        binary.append(1)
        results[0] = results[0] + 1

    counter = 0
    binary.reverse()
    while counter != len(binary):
        if binary[counter] == 1:
            results.append(counter + 1)
        counter += 1
            

    return results


print(getOneBits(112312))