from logic_utils import check_guess, parse_guess

def test_winning_guess():
    # Bug 1: Fixed swapped hints - test win condition
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message

def test_guess_too_high():
    # Bug 1: Fixed swapped hints - test too high with correct message
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "Go LOWER" in message

def test_guess_too_low():
    # Bug 1: Fixed swapped hints - test too low with correct message
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "Go HIGHER" in message

def test_parse_guess_valid():
    # Test valid input
    ok, val, err = parse_guess("50", 1, 100)
    assert ok
    assert val == 50
    assert err is None

def test_parse_guess_too_low():
    # Bug 3: Fixed bound checking - test below low
    ok, val, err = parse_guess("0", 1, 100)
    assert not ok
    assert val is None
    assert "between 1 and 100" in err

def test_parse_guess_too_high():
    # Bug 3: Fixed bound checking - test above high
    ok, val, err = parse_guess("101", 1, 100)
    assert not ok
    assert val is None
    assert "between 1 and 100" in err

def test_parse_guess_not_number():
    # Test invalid input
    ok, val, err = parse_guess("abc", 1, 100)
    assert not ok
    assert val is None
    assert "not a number" in err

def test_parse_guess_empty():
    # Test empty input
    ok, val, err = parse_guess("", 1, 100)
    assert not ok
    assert val is None
    assert "Enter a guess" in err

# For bug 2: New game reset - this is hard to test with pytest as it involves Streamlit state
# Perhaps test that parse_guess works with different ranges (related to difficulty)
def test_parse_guess_different_range():
    ok, val, err = parse_guess("5", 1, 20)  # Easy range
    assert ok
    assert val == 5

    ok, val, err = parse_guess("25", 1, 20)
    assert not ok
    assert "between 1 and 20" in err
