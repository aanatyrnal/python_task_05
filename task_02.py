#2 *(вместо 1) Решить задачу генерации нечётных чисел от 1 до n (включительно),
# не используя ключевое слово yield.
MAX_NUM = 15


fun_gen = (num for num in range(1, MAX_NUM + 1, 2))


odd_nums = fun_gen
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))