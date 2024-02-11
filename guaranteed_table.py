from guaranteed import get_guaranteed

with open("table.txt", "r") as f:
    data = f.readlines()
    rows, cols = list(map(int, data[0].split(" ")))
    table = [[False for i in range(cols)] for j in range(rows)]
    for i in range(1, 1 + rows):
        tomography = list(map(int, data[i].strip().split(",")))
        row_result = get_guaranteed(cols, tomography)
        for index, value in enumerate(row_result):
            table[i - 1][index] = value
    for j in range(1 + rows, 1 + rows + cols):
        tomography = list(map(int, data[j].strip().split(",")))
        cols_result = get_guaranteed(rows, tomography)
        for index, value in enumerate(cols_result):
            table[index][j - 1 - rows] = value

    for row in table:
        print("".join(map(lambda x: "█" if x else "<", row)))
