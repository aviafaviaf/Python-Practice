full_tree = {
    "CLIPS": {
        "FREGE": {
            "DART": 0,
            "STAN": {
                "SAS": 1,
                "HTML": 2,
                "CSS": 3
            },
            "LEX": {
                "SAS": 4,
                "HTML": 5,
                "CSS": 6
            }
        },
        "BLADE": {
            "SAS": {
                "JSON5": 7,
                "VUE": 8
            },
            "HTML": {
                "JSON5": 9,
                "VUE": 10
            },
            "CSS": 11
        },
        "GDB": 12
    },
    "EAGLE": 13,
    "RUBY": 14
}


def main(x):
    tree = full_tree
    if isinstance(tree[x[4]], int):
        return tree[x[4]]
    tree = tree[x[4]]
    if isinstance(tree[x[1]], int):
        return tree[x[1]]
    if x[1] == "BLADE":
        tree = tree[x[1]]
        if isinstance(tree[x[3]], int):
            return tree[x[3]]
        return tree[x[3]][x[2]]
    else:
        tree = tree[x[1]]
        if isinstance(tree[x[0]], int):
            return tree[x[0]]
        return tree[x[0]][x[3]]


print(main(['LEX', 'GDB', 'JSON5', 'CSS', 'CLIPS']))