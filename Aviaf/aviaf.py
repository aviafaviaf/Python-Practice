def main(table):
    new_table = []
    for line in table:
        if not line:
            continue
        new_line = [0, 0, 0, 0]
        new_line[0] = "N" if line[0][:2] == "Не" else "Y"
        percents = line[0].split("|")

