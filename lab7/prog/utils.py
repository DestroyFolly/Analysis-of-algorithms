from avl import *
from binary import *
from time import process_time

def generate_n(tree, n):
    for i in range(n):
        tree.Insert(i)

def measure():
    experiments = [259, 1027, 4099, 16387, 65539]

    print("Количество элементов, худший случай AVL, лучший случай AVL, худший случай BST, лучший случай BST", "Время: ")
    for n in experiments:
        start = process_time()
        avlTree = AVLTree()
        tree = Tree()

        generate_n(avlTree, n)
        generate_n(tree, n)
        result = process_time() - start

        print(n, avlTree.SearchCount(n + 1), avlTree.SearchCount(avlTree.root.key), tree.SearchCount(n + 1), tree.SearchCount(tree.root.key), result, sep = ',')

    result = process_time() - start