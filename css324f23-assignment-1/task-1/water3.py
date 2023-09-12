def initial_state():
    return (8, 0, 0)

def is_goal(s):
    return s[0] == 4 and s[1] == 4

def successors(s):
    a, b, c = s
    successors = []

    # Pour from 8 to 5
    if a > 0 and b < 5:
        pour_amount = min(a, 5 - b)
        new_state = (a - pour_amount, b + pour_amount, c)
        successors.append((new_state, pour_amount))

    # Pour from 8 to 3
    if a > 0 and c < 3:
        pour_amount = min(a, 3 - c)
        new_state = (a - pour_amount, b, c + pour_amount)
        successors.append((new_state, pour_amount))

    # Pour from 5 to 8
    if b > 0 and a < 8:
        pour_amount = min(b, 8 - a)
        new_state = (a + pour_amount, b - pour_amount, c)
        successors.append((new_state, pour_amount))

    # Pour from 5 to 3
    if b > 0 and c < 3:
        pour_amount = min(b, 3 - c)
        new_state = (a, b - pour_amount, c + pour_amount)
        successors.append((new_state, pour_amount))

    # Pour from 3 to 8
    if c > 0 and a < 8:
        pour_amount = min(c, 8 - a)
        new_state = (a + pour_amount, b, c - pour_amount)
        successors.append((new_state, pour_amount))

    # Pour from 3 to 5
    if c > 0 and b < 5:
        pour_amount = min(c, 5 - b)
        new_state = (a, b + pour_amount, c - pour_amount)
        successors.append((new_state, pour_amount))

    return successors





