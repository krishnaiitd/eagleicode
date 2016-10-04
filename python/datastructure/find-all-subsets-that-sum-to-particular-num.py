def total_subsets_matching_sum(numbers, sum):
    array = [1] + [0] * (sum)
    for current_number in numbers:
        for num in xrange(sum, current_number - 1, -1):
            if array[num-current_number]:
                array[num] += array[num-current_number]
         	#print(array)
        print('for the current_number', current_number)
        print(array)

    print('final array')    
    print(array)

    return array[sum]


assert(total_subsets_matching_sum(range(1, 10), 9) == 8)

print('Second part')
assert(total_subsets_matching_sum({1, 3, 2, 5, 4, 9}, 9) == 4)

