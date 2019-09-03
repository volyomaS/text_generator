import random


class Generate:
    def __init__(self):
        self.filename = 'data.txt'

    def action(self):
        words_count = random.randrange(10, 20)
        data = eval(open(self.filename, 'r', encoding='utf-8').readline())
        prev = ''
        for i in range(words_count):
            try:
                if prev == '':
                    keys = []
                    keys[:] = data.keys()
                    prev = random.choice(keys)
                else:
                    prev = random.choice(data[prev])
                print(prev, end=' ')
            except KeyError:
                keys = []
                keys[:] = data.keys()
                prev = random.choice(keys)
                print(prev, end=' ')
