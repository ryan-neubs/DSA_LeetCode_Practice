def romanizer(numbers):
    # Write your code here
    answers = []
    for num in numbers:
        rom_vals = [(1000, 'M'), (900, 'CM'),
                    (500, 'D'), (400, 'CD'),
                    (100, 'C'), (90, 'XC'),
                    (50, 'L'), (40, 'XL'),
                    (10, 'X'), (9, 'IX'),
                    (5, 'V'), (4, 'IV'),
                    (1, 'I')]
        ans = ""
        
        for value, symbol in rom_vals:
            if numbers == 0:
                break
            count, num = divmod(num, value)
            ans += symbol * count
        answers.append(ans)

    return answers