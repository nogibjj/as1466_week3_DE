from main import basic_two_calculation

def test_main():
    assert basic_two_calculation(1,2) == 3
    assert basic_two_calculation(10,10) == 20

test_main()
