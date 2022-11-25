# 3. Напишите программу, в которой пользователь будет задавать две строки,
#  а программа - определять количество вхождений одной строки в другой.

a = ('мама мама')
b = ('ма')
count = 0
for i in range(len(a)):
    # print(i)
    if b == a[i:i+len(b)]:
        count = count+1

print(count)


# a = input()
# b = input()
# count = 0
# for i in range(len(a)):
#     if a[i:i+len(b)] == b:
#         count += 1
# print(count)
# print(a.count(b))
