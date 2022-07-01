import calculate


def test_all():
    test_packed_calc_sum()
    test_packed_calc_subtraction()
    test_packed_calc_mult()
    test_packed_calc_division()
    test_packed_calc_log()
    test_loading_params()


def test_packed_calc_sum():
    inp1, action = [1, 2, 3, 4, 5, 6, 7, 8, 9], "+"
    assert calculate.calculate(*inp1, action, **calculate.PARAMS) == 45.0, 'sum doesn\'t work correctly '


def test_packed_calc_subtraction():
    inp1, action = [1, 2], "-"
    assert calculate.calculate(*inp1, action, **calculate.PARAMS) == -1.0, 'subtraction doesn\'t work correctly '


def test_packed_calc_mult():
    inp1, action = [1, 2, 3], "*"
    assert calculate.calculate(*inp1, action, **calculate.PARAMS) == 6.0, 'multiplication doesn\'t work correctly '


def test_packed_calc_division():
    inp1, action = [1, 0, 3, 6, 0], "/"
    assert calculate.calculate(*inp1, action, **calculate.PARAMS) == 'can\'t divide by a zero'


def test_packed_calc_log():
    inp1, action = [16, 2], "log"
    assert calculate.calculate(*inp1, action,
                               **calculate.PARAMS) == 4.0, 'something went wrong and the program couldn\'t calculate ' \
                                                           'the logarithm '


def test_loading_params():
    calculate.load_params()
    assert calculate.PARAMS.get(
        'dest') == 'output.txt', "the name of the file has to be output.txt"
