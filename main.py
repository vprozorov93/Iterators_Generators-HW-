class FlatIterator:

    def __init__(self, lists_in_list):
        self.lists_in_list = lists_in_list

    def __iter__(self):
        self.cursor = -1
        self.sub_cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.lists_in_list):
            raise StopIteration
        item = self.lists_in_list[self.cursor]

        if isinstance(item, list):
            self.cursor -= 1
            sub_iter = FlatIterator(item)
            sub_iter.__iter__()
            sub_iter.cursor = self.sub_cursor

            if sub_iter.cursor != len(sub_iter.lists_in_list)-2:
                self.sub_cursor += 1
                item2 = sub_iter.__next__()
            else:
                self.sub_cursor += 1
                item2 = sub_iter.__next__()
                self.cursor += 1
                self.sub_cursor = -1

            return item2
        else:
            return item


def my_generator(lists_of_list):
    for list_ in lists_of_list:
        for element in list_:
            if isinstance(element, list):
                for el in my_generator(element):
                    yield el
            else:
                yield element


if __name__ == "__main__":
    print('Task 1 and 3:')
    nested_list = [
        ['a', 'b', ['c'], [['d']]],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]
    print([x for x in FlatIterator(nested_list)])

    print('Task 2 and 4:')
    nested_list = [
        ['a', 'b', [['c']]],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]
    print([x for x in my_generator(nested_list)])

