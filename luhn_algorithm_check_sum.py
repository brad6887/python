for test_case in range(5):
    values = []
    tests = input()
    tests_list = tests.split()
    for this_one in range(5):
        num = (tests_list[this_one])
        odd_num = num[-1::-2]
        even_num = num[-2::-2]
        o_total = 0
        e_total = 0
        for i in odd_num:
            result = 0
            result += int(i) * 2
            for digit in str(result):
                e_total += int(digit)
        for j in even_num:
            o_total += int(j)
        final = o_total + e_total
        digits = list(str(final))
        final_digit = (digits[-1])
        check = 10 - int(final_digit)
        if check == 10:
            check = 0
        values.append(check)
    print(*values, sep="")
