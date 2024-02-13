from guaranteed import get_guaranteed

with open("rows.txt", "r") as f:
    data = f.readlines()
    for line in data:
        tomography = list(map(int, line.strip().split(",")))
        result = get_guaranteed(20, tomography)
        print("".join(map(lambda x: "o" if x else "x", result)))
