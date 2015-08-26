class ToDoList_1(object):

    def __init__(self):
        self._list = []

    def add_item(self, item):
        self._list.append(item)

    def delete_item(self, item):
        try:
            self._list.remove(item)
        except ValueError:
            print('No such item:', item)

    def view_list(self):
        for item in self._list:
            print('- ' + item)


class ToDoList_2(object):
    def __init__(self, filename=None):
        self._list = {}
        if filename:
            for row in open(filename, 'r').readlines():
                item, cats = row.split(':')
                cats = cats.split(',')
                self._list[item] = cats
    
    def add_item(self, item, *categories):
        if not categories:
            categories = ('uncategorized')
        self._list[item] = [c.upper() for c in categories]
    
    def delete_item(self, item):
        del self._list[item]
    
    def update_item(self, item, new_value):
        self._list[new_value] = self._list[item]
        self.delete_item(item)
    
    def view_list(self, *categories):
        if not categories:
            for category in set([item for sublist in list(self._list.values()) for item in sublist]):
                self.view_list(category)
                print()
            return
        categories = [c.upper() for c in categories]
        print('-----{}-----'.format(' & '.join(categories)))
        for item, cats in self._list.items():
            if set(categories) <= set(cats):
                print('- ' + item)
    
    def save(self, filename):
        with open(filename, 'w') as f:
            for item, cats in self._list.items():
                f.write('{}: {}\n'.format(item, ','.join(cats)))
        

if __name__ == '__main__':
    todo = ToDoList_2()
    todo.add_item('A pixel is not a pixel is not a pixel', 'programming')
    todo.add_item('The Scheme Programming language', 'programming')
    todo.add_item('Memory in C', 'programming')
    todo.add_item("Haskell's School of Music", 'programming', 'music')
    todo.add_item('Algorithmic Symphonies from one row of code', 'programming', 'music')
    todo.add_item('Modes in Folk Music', 'music')
    todo.add_item('The use of the Meloddic Minor Scale', 'music')
    
    todo.update_item('The use of the Meloddic Minor Scale', 'The use of the Melodic Minor Scale')
    todo.view_list('programming')
    print()
    todo.view_list('music')
    print()
    todo.view_list('music', 'programming')
    
    todo.save('todo.txt')
    todo2 = ToDoList_2('todo.txt')
    todo.view_list()
