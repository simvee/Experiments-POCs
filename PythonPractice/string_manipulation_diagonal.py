str_a = 'Ansdfsjgsoijgesjgnewoigjewibne'
str_a = list(str_a)
n_rows = 1000
num_chars_per_pattern = n_rows + (n_rows-2)

split_arrs = [str_a[start_ind:start_ind+num_chars_per_pattern] for start_ind in range(0, len(str_a), num_chars_per_pattern)]

delimiter = ' '*(n_rows-2)

split_arrs = [arr[0:n_rows] + list(delimiter) + list(delimiter.join(arr[n_rows:num_chars_per_pattern])) + list(delimiter) for arr in split_arrs]

if len(split_arrs[-1]) < len(split_arrs[0]):
    split_arrs[-1].extend(list(' '*(len(split_arrs[0])-len(split_arrs[-1]))))

complete_str = ""
final_str = ""

for arr in split_arrs:
    complete_str = complete_str + ''.join(arr)

for row in range(n_rows):
    row_letters = [complete_str[ind] for ind in range(row, len(complete_str), n_rows)]

    final_str = final_str + ''.join(row_letters)

final_str = final_str.replace(' ', '')
print(final_str)

# split_arrs = list(zip(*split_arrs))

# print(split_arrs)



# reshaped_arr = [str_a[start_ind:start_ind+3] for start_ind in range(0, len(str_a), 3)]


# print(reshaped_arr)


# PINALSIGYAHRPI