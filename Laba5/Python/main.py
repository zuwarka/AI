L = [1, 2, 3, 4, 5, 6, 7, 8]
input_index = input('Input index: ')
input_number = input('Input number to sum: ')

input_index = int(input_index)
input_number = int(input_number)

if input_index > len(L) or input_index < 0:
    print('Error index!')
    exit()

L[input_index] = L[input_index] + input_number
print(L)
