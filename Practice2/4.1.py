def get_groups(group_count, year):
    res = {}
    for spec, count in group_count.items():
        res[spec] = [f'{spec}-{i:02}-{year}' for i in range(1, count + 1)]
    return res


def print_groups(groups):
    for spec, group in groups.items():
        print(spec)
        print(' '.join(group), end='\n\n')


GROUPS_COUNT = {'ИВБО': 9, 'ИКБО': 37, 'ИМБО': 2, 'ИНБО': 12}
YEAR = 22
group = get_groups(GROUPS_COUNT, YEAR)
print_groups(group)