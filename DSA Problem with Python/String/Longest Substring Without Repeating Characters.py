s = "aabdcacb "

str_list = list(s)
print(str_list)
empty_str_list = []
len_max = 0
for i in range(len(str_list)):
    while str_list[i] in empty_str_list:
        empty_str_list.pop(0)
    empty_str_list.append(str_list[i])
    len_max = max(len_max, len(empty_str_list))
print(len_max)
