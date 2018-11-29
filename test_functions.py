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
    assert func.name_check('Sasha Sllavutin') == 'Sasha Sllavutin'
    assert func.name_check('Sasha sllavutin') == 'Sasha Sllavutin'
    assert func.name_check('sasha sllavutin') == 'Sasha Sllavutin'
    assert func.name_check('Petr') == 0
    assert func.name_check('Sasd.sdfsdf sdf.sdf.sdfsdf') == 0
    assert func.name_check('123324646463452 12341321234') == 0
    assert func.name_check('_____ asdfasdfsdf _____') == 0
    assert func.name_check('____ _____') == 0
    assert func.name_check('Sasha1 Petrov') == 'Sasha1 Petrov'


def test_number_check():
    assert func.number_check('89101418456') == '89101418456'
    assert func.number_check('8910141845') == 0
    assert func.number_check('+79101418456') == '89101418456'
    assert func.number_check('+79101418456123123') == 0
    assert func.number_check('Wrong input') == 0
    assert func.number_check('89101sdffsdf') == 0
    assert func.number_check('+7+7+7+7+7+7+7+7+7+7+7') == 0
    assert func.number_check('8910 123123 123123') == 0
    assert func.number_check('+79101412356') == '89101412356'
    assert func.number_check('+7910141845+7') == 0




