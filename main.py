def kbig(nums, k):
    try:
        nums = list(map(int, nums.split()))
        k = int(k)
        if k <= len(nums):
            print(f'Получена последовательность чисел {nums}, в которой нужно найти {k} элемент по убываю')
            for i in range(k - 1):
                nums.remove(max(nums))
            print(f'{k} элемент по убываю = {max(nums)}')
            return max(nums)
    except:
        print("Не верно веденны данные, попробуйте еще раз ...")
        main()


def main():
    ls = input()
    id_of_elem = input()
    print(kbig(ls, id_of_elem))
    return

main()
