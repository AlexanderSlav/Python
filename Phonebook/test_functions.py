import functions as func


def test_date_check():
    assert func.date_check('22/11/1986') == 1
    assert func.date_check('100/11/1986') == 0
    assert func.date_check('0/11/1986') == 0
    assert func.date_check('22/0/1986') == 0
    assert func.date_check('28/1/-100') == 0
    assert func.date_check('31/12/1486') == 1
    assert func.date_check('sdfdsfsdfsd') == 0
    assert func.date_check('sdf/dsfs/dfsd') == 0
    assert func.date_check('') == 1
    assert func.date_check('1233452345') == 0
    assert func.date_check('12/123') == 0
    assert func.date_check('ываыва') == 0
    assert func.date_check('0/0/0') == 0


def test_name_check():
    assert func.name_check('Sasha Sllavutin') == 1
    assert func.name_check('sasha sllavutin') == 1
    assert func.name_check('Petr') == 0
    assert func.name_check('Sasd.sdfsdf sdf.sdf.sdfsdf') == 0
    assert func.name_check('123324646463452 12341321234') == 0
    assert func.name_check('_____ asdfasdfsdf _____') == 0
    assert func.name_check('____ _____') == 0
    assert func.name_check('Sasha1 Petrov') == 1
    assert func.name_check('1asha1 2etrov') == 0
    assert func.name_check('1asha1 petrov') == 0


def test_number_check():
    assert func.number_check('89101418456') == 1
    assert func.number_check('8910141845') == 0
    assert func.number_check('+79101418456') == 1
    assert func.number_check('+79101418456123123') == 0
    assert func.number_check('Wrong input') == 0
    assert func.number_check('89101sdffsdf') == 0
    assert func.number_check('+7+7+7+7+7+7+7+7+7+7+7') == 0
    assert func.number_check('8910 123123 123123') == 0
    assert func.number_check('+79101412356') == 1
    assert func.number_check('+7910141845+7') == 0
    assert func.number_check('+7910141845+7') == 0


def test_comparison_number_check():
    assert func.comparison_number_check('123') == 1
    assert func.comparison_number_check('0') == 1
    assert func.comparison_number_check('-123213') == 0
    assert func.comparison_number_check('') == 0
    assert func.comparison_number_check('sdfasf') == 0
    assert func.comparison_number_check('12/5') == 0
    assert func.comparison_number_check('12.5') == 0


def test_date_check_for_search():
    assert func.date_check_for_search('22/11') == 1
    assert func.date_check_for_search('100/11') == 0
    assert func.date_check_for_search('0/11') == 0
    assert func.date_check_for_search('22/0/') == 0
    assert func.date_check_for_search('28/1') == 0
    assert func.date_check_for_search('31/12') == 1
    assert func.date_check_for_search('sdfdsfsdfsd') == 0
    assert func.date_check_for_search('sdf/dsfs') == 0
    assert func.date_check_for_search('') == 0
    assert func.date_check_for_search('1233452345') == 0
    assert func.date_check_for_search('12/123') == 0
    assert func.date_check_for_search('ываыва') == 0
    assert func.date_check_for_search('0/0/0') == 0
    assert func.date_check_for_search('!/01/00') == 0

