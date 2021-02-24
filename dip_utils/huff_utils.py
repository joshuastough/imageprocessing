"""
Huffman Tree/Coding Utility Functions
stough 202-
"""

import matplotlib.pyplot as plt
import numpy as np
from heapq import *
from huffnode import HuffNode

#Build a huffman tree based on some image I, return the tree
#Assuming a uint8 single channel image
def build_huff_tree(I):

    #Now we know I is uint8, single channel
    hist, bins = np.histogram(I.ravel(), np.arange(257))

    lystOfNodes = [HuffNode(freq, intensity) for freq,intensity in zip(hist, bins[:-1])]

    #Now use the heapq functions to build a single tree out of these nodes.
    heapify(lystOfNodes)

    while len(lystOfNodes) > 1:
        first = heappop(lystOfNodes)
        second = heappop(lystOfNodes)
        heappush(lystOfNodes, HuffNode(first.get_freq() + second.get_freq(),
                            -1, second, first))
        #Notice making the left side the more frequent.

    #When there is only one node in the lyst, then that node is the
    #root of the Huffman tree.
    tree = heappop(lystOfNodes)
    #tree.printTree()
    return tree

#A function that recursively constructs the bit sequence leading to
#each leaf node, building a dictionary that goes from leaf node
#symbol to that sequence.
def build_huff_encoder(tree, seq = ''):
    retDict = {}
    if tree.is_leaf():
        retDict[tree.get_symb()] = seq
        return retDict

    #Left is 1, right is 0
    if tree.get_left():
        retDict.update(build_huff_encoder(tree.get_left(), seq + '1'))

    if tree.get_right():
        retDict.update(build_huff_encoder(tree.get_right(), seq + '0'))

    return retDict


def build_huff_pair(I):
    tree = build_huff_tree(I)
    encoder = build_huff_encoder(tree)
    #the following should work because encoder[key] should also be unique.
    decoder = dict((encoder[key], key) for key in encoder)
    return encoder, decoder

def load_huffable_image(I):
    if type(I) == str:
        I = plt.imread(I)

    if (len(I.shape) > 2):
        print("loadHuffableImage: input is multi-channel, using grayscale.")
        Ig = 0.2989 * I[..., 0] + 0.5870 * I[..., 1] + 0.1140 * I[..., 2]
        I = Ig

    if I.ravel().max() <= 1:
        print('loadHuffableImage: Setting range to [0, 255]')
        I = np.round(256*I)

    I[I > 255] = 255
    I = I.copy().astype('uint8')

    return I

def test_tree_making():
    lyst = [HuffNode(np.random.randint(0,1000), chr(ord('A') + x)) for x in range(4)]
    print('Before heapify...')
    print('\n'.join(str(item) for item in lyst))

    heapify(lyst)

    print('\nAfter heapify...')
    print('\n'.join(str(item) for item in lyst))


    #placing the more likely on the left side
    while len(lyst) > 1:
        first = heappop(lyst)
        second = heappop(lyst)
        heappush(lyst, HuffNode(first.get_freq() + second.get_freq(),
                            '*', second, first))

    print('Final Huffman tree:\n')
    myHuff = heappop(lyst)
    myHuff.print_tree()


#test_tree_making()
