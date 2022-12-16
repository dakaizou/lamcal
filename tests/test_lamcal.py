from lamcal import bool
from lamcal.util import translate_bool


def test_true():
    assert bool.l_true(True)(False) == True
    assert bool.l_true(True)(False) != False


def test_false():
    assert bool.l_false(True)(False) == False
    assert bool.l_false(True)(False) != True


def test_not():
    assert bool.l_not(bool.l_true)(True)(False) == False
    assert bool.l_not(bool.l_false)(True)(False) == True


def test_or():
    assert bool.l_or(bool.l_true)(bool.l_true)(True)(False) == True
    assert bool.l_or(bool.l_true)(bool.l_false)(True)(False) == True
    assert bool.l_or(bool.l_false)(bool.l_true)(True)(False) == True
    assert bool.l_or(bool.l_false)(bool.l_false)(True)(False) == False


def test_and():
    assert bool.l_and(bool.l_true)(bool.l_true)(True)(False) == True
    assert bool.l_and(bool.l_true)(bool.l_false)(True)(False) == False
    assert bool.l_and(bool.l_false)(bool.l_true)(True)(False) == False
    assert bool.l_and(bool.l_false)(bool.l_false)(True)(False) == False


def test_nor():
    assert bool.l_nor(bool.l_true)(bool.l_true)(True)(False) == False
    assert bool.l_nor(bool.l_true)(bool.l_false)(True)(False) == False
    assert bool.l_nor(bool.l_false)(bool.l_true)(True)(False) == False
    assert bool.l_nor(bool.l_false)(bool.l_false)(True)(False) == True


def test_xor():
    assert bool.l_xor(bool.l_true)(bool.l_true)(True)(False) == False
    assert bool.l_xor(bool.l_true)(bool.l_false)(True)(False) == True
    assert bool.l_xor(bool.l_false)(bool.l_true)(True)(False) == True
    assert bool.l_xor(bool.l_false)(bool.l_false)(True)(False) == False


def test_eqb():
    assert bool.l_eqb(bool.l_true)(bool.l_true)(True)(False) == True
    assert bool.l_eqb(bool.l_true)(bool.l_false)(True)(False) == False
    assert bool.l_eqb(bool.l_false)(bool.l_true)(True)(False) == False
    assert bool.l_eqb(bool.l_false)(bool.l_false)(True)(False) == True


def test_nand():
    assert bool.l_nand(bool.l_true)(bool.l_true)(True)(False) == False
    assert bool.l_nand(bool.l_true)(bool.l_false)(True)(False) == True
    assert bool.l_nand(bool.l_false)(bool.l_true)(True)(False) == True
    assert bool.l_nand(bool.l_false)(bool.l_false)(True)(False) == True
