from analysis import get_priority

def test_priority():
    assert get_priority(3) == "High"
    assert get_priority(2) == "Medium"
    assert get_priority(1) == "Low"
    print("Priority tests passed!")

test_priority()