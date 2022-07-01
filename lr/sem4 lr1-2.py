# Бражкина А.Д., ИВТ2, 2 курс

def gen_bin_tree(height, root):

    tree = {str(root): []}

    if height == 1:
        return tree

    left_leaf = root * 2
    right_leaf = root + 2

    height -= 1
    tree.get(str(root)).append(gen_bin_tree(height, left_leaf))
    tree.get(str(root)).append(gen_bin_tree(height, right_leaf))

    return tree


"""
для функции с рекурсией:

"""


def gen_bin_tree_non_rec(height, root):
    tree = BinaryTree(root)
    currentRoots = []
    previousRoots = []
    for i in range(0, height - 1):
        if (i == 0):
            _root = getRootVal(tree)
            insertLeft(tree, _root * 2)
            insertRight(tree, _root + 2)
            currentRoots.clear()
            currentRoots.append(getLeftChild(tree))
            currentRoots.append(getRightChild(tree))
        else:
            previousRoots = currentRoots[:]
            currentRoots.clear()
            for j in previousRoots:
                _root = getRootVal(j)
                insertLeft(j, _root * 2)
                insertRight(j, _root + 2)
                currentRoots.append(getLeftChild(j))
                currentRoots.append(getRightChild(j))
    return tree


def BinaryTree(r):
    return [r, [], []]


def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])
    return root


def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])
    return root


def getRootVal(root):
    return root[0]


def setRootVal(root, newVal):
    root[0] = newVal


def getLeftChild(root):
    return root[1]


def getRightChild(root):
    return root[2]


def main():

    h = int(input("height = "))
    r = int(input("root = "))

    print("С рекурсией: ", gen_bin_tree(height=h, root=r))
    print("Без рекурсии: ", gen_bin_tree_non_rec(height=h, root=r))


main()
