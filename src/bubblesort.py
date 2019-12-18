from src.abstractsort import AbstractSort

class BubbleSort(AbstractSort):
    def __init__(self):
        super().__init__()
        self.sort_method_name = 'Bubble sort'


    def get_numbers_list(self, numbers: list):
        print('I should get numbers list here ', numbers)
        self.numbers = numbers


    def sort_numbers(self):
        print("I should bubble sort here and return sorted numbers")
        return [x^2 for x in self.numbers]

if __name__ == '__main__':
    sortme = BubbleSort()
    sortme.get_numbers_list([6,5,4])
    sortme.sort_numbers()
    sortme.print_sort_name()