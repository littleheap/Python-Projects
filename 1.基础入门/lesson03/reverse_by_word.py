# 字符串按单词反转
def reverse(str_list, start, end):
    while start < end:
        str_list[start], str_list[end] = str_list[end], str_list[start]
        start += 1
        end -= 1


setence = ' Hello, how are you?   Fine.   '
str_list = list(setence)
i = 0
while i < len(str_list):
    if str_list[i] != ' ':
        start = i
        end = start + 1
        while (end < len(str_list)) and str_list[end] != ' ':
            end += 1
        reverse(str_list, start, end - 1)
        i = end
    else:
        i += 1
str_list.reverse()
print(''.join(str_list))
