import area

def test_square_area():
    #setup
    length = 8
    expected = 64

    #invoke
    actual = area.square_area(length)

    #analyze
    assert expected == actual