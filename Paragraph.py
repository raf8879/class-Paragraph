class LeftParagraph:

    def __init__(self, length):
        self.length = length
        self.data = ['']

    def add(self, args):
        words = args.split()
        for word in words:
            if len(self.data[-1] + f' {word}') > self.length:
                self.data.append('')
            self.data[-1] = (self.data[-1] + f' {word}').lstrip()

    def end(self):
        for line in self.data:
            print(line)
        self.data = ['']


class RightParagraph(LeftParagraph):
    def end(self):
        for line in self.data:
            print(line.rjust(self.length))
        self.data = ['']


rightparagraph = RightParagraph(28)

rightparagraph.add('I will not regret the roses')
rightparagraph.add('Withered with a light spring')
rightparagraph.add('I love the grapes on the vines')
rightparagraph.add('Ripened in the hands under the mountain')
rightparagraph.end()

rightparagraph.add('The beauty of my green valley')
rightparagraph.add('Golden joy of autumn')
rightparagraph.add('oblong and transparent')
rightparagraph.add('Like the fingers of a young maiden')
rightparagraph.end()
