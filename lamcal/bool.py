def l_true(x):
    return lambda y: x


def l_false(x):
    return lambda y: y


def l_not(bool):
    # return bool(l_false)(l_true)
    return lambda x: (lambda y: bool(y)(x))


def l_or(b1):
    return lambda b2: b1(b1)(b2)


def l_and(b1):
    return lambda b2: b1(b2)(b1)


def l_nor(b1):
    return lambda b2: l_not(l_or(b1)(b2))


def l_xor(b1):
    return lambda b2: l_and(l_nand(b1)(b2))(l_or(b1)(b2))


def l_eqb(b1):
    return lambda b2: l_not(l_xor(b1)(b2))


def l_nand(b1):
    return lambda b2: l_not(l_and(b1)(b2))
