def fix_bounds(mins, maxs):
    for i in range(3):
        if mins[i] > maxs[i]:
            temp = maxs[i]
            maxs[i] = mins[i]
            mins[i] = temp


def is_in_box(coords, mins, maxs) -> bool:
    fix_bounds(mins, maxs)

    for i in range(3):
        if coords[i] < mins[i] or coords[i] > maxs[i]:
            return False

    return True


def is_in_box_fuzzy(coords, mins, maxs, percentage=0.01) -> bool:
    return is_in_box(coords, [x * (1.0 + percentage) for x in mins], [x * (1.0 + percentage) for x in maxs])
