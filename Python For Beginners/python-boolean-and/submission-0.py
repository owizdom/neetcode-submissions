a, b, c, d = False, False, True, True

groups = [

    ("firstAND" , [a, b]),
    ("secondAND", [b, c]),
    ("thirdAND", [c, d]),
    ("finalAND", [a, b, c, d])
]

for name, values in groups:
    print(all(values))