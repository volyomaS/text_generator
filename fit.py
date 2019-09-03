class Fit:
    def __init__(self, filename):
        self.filename = filename

    def action(self):
        fin = open(self.filename, 'r', encoding='utf-8')
        data = {}
        prev = ''
        for line in fin:
            line = line.strip()
            line = line.replace('.', '')
            line = line.replace(',', '')
            line = line.replace('?', '')
            line = line.replace('!', '')
            line = line.replace('(', '')
            line = line.replace(')', '')
            line = line.replace('+', '')
            line = line.replace('-', '')
            line = line.replace('—', '')
            line = line.replace('*', '')
            line = line.replace('/', '')
            line = line.replace(':', '')
            line = line.replace(';', '')
            line = line.replace('', '')
            line = line.lower()
            line = line.split()
            if prev in data and prev != '' and len(line) > 0:
                data[prev].append(line[0])
            elif prev != '' and len(line) > 0:
                data[prev] = []
                data[prev].append(line[0])
            for i in range(len(line)-1):
                if line[i] in data:
                    data[line[i]].append(line[i+1])
                else:
                    data[line[i]] = []
                    data[line[i]].append(line[i+1])
            if len(line) > 0:
                prev = line[-1]
        return data

    def rewrite(self, data):
        old_data = eval(open('data.txt', 'r', encoding='utf-8').readline())
        for key in data.keys():
            if key in old_data:
                old_data[key] += data[key]
            else:
                old_data[key] = data[key]
        open('data.txt', 'w', encoding='utf-8').write(str(old_data))
