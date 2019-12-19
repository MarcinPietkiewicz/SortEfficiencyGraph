from src.abstractsort import AbstractSort

class BubbleSort(AbstractSort):
    def __init__(self):
        super().__init__()
        self.sort_method_name = 'Bubble sort'


    def get_numbers_list(self, numbers: list):
        print('I should get numbers list here ', numbers)
        self.numbers = numbers


    def sort_numbers(self):
        print("Sorting (bubble sort method ...")
        flag = True
        a = 1
        p = 1
        while flag:
            flag = False
            for i in range(0, len(self.numbers) - a):
                # print('przebieg', p)
                p += 1
                if self.numbers[i] > self.numbers[i + 1]:
                    self.numbers[i + 1], self.numbers[i] = self.numbers[i], self.numbers[i + 1]
                    flag = True
            if flag == True:
                a += 1

if __name__ == '__main__':
    sortme = BubbleSort()
    sortme.get_numbers_list([6,5,4,3,12,1])
    sortme.sort_numbers()
    sortme.print_sort_name()