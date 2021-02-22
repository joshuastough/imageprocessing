"""
Joshua Stough
DIP

Simple binary tree class for huffman coding demo.
"""

class HuffNode(object):
    def __init__(self):
        self.l = self.r = None
        self.f = -1 #frequency
        self.s = 'a' #symbol, or intensity

    def __init__(self, freq, symbol ='a', left = None, right = None):
        self.f = freq
        self.s = symbol
        self.l = left
        self.r = right

    def get_freq(self):
        return self.f

    def get_symb(self):
        return self.s

    def get_left(self):
        return self.l

    def get_right(self):
        return self.r

    def is_leaf(self):
        return (self.l is None) and (self.r is None)

    def __str__(self):
        return '[node: freq %d: %s]' % \
                (self.f, ['', str(self.s)][self.is_leaf()])

    def __cmp__(self, other):
        return self.f - other.f

    def __eq__(self, other):
        return self.f == other.f

    def __ne__(self, other):
        return self.f != other.f

    def __lt__(self, other):
        return self.f < other.f

    def print_tree(self, level = 0):
        thisnodestr = '  ' * level + '--'+ str(self)
        if self.is_leaf():
            print(thisnodestr)
        else:
            #backwards in-order traversal
            #so left and right is still
            #left and right when you twist your head.
            if self.r is not None:
                self.r.print_tree(level + 1)
            print(thisnodestr)
            if self.l is not None:
                self.l.print_tree(level + 1)
