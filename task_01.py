#1 Написать генератор нечётных чисел от 1 до n (включительно), используя ключевое слово yield, например:
# >>> odd_to_15 = odd_nums(15)
# >>> next(odd_to_15)
# 1
# >>> next(odd_to_15)
# 3
# ...
# >>> next(odd_to_15)
# 15
# >>> next(odd_to_15)
# ...StopIteration...
MAX_NUM = 15


def fun_gen():
    for num in range(1, MAX_NUM + 1):
        if num % 2 == 1:
            yield num


odd_nums = fun_gen()
print(next(odd_nums))
print(next(odd_nums))
print(next(odd_nums))