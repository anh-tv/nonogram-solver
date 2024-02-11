from guaranteed import get_guaranteed

with open("rows.txt", "r") as f:
    data = f.readlines()
    for line in data:
        tomography = list(map(int, line.strip().split(",")))
        print("".join(map(lambda x: "o" if x else "x", get_guaranteed(20, tomography))))

