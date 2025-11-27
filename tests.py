from main import search

def test_simple_words():
    assert search("папа мама коко") == ['папа','мама', 'коко']


def test_mixed_case():
    assert search("Папа МАМА КОКО") == ['папа','мама', 'коко']


def test_punctuation():
    assert search("папа, мама! коко? лололол;") == ['папа','мама', 'коко']


def test_no_matches():
    assert search("дом машина кот документы") == []


def test_long_repetition():
    assert search("тесттест") == ['тесттест']


def test_multiple_in_text():
    text = "папа лололол абвабв тесттест блабла"
    assert search(text) == ['папа', 'абвабв', 'тесттест', 'блабла']


def test_empty_string():
    assert search("") == []


def test_numbers():
    assert search("1212 123123") == ['1212', '123123']


def test_non_repeating_numbers():
    assert search("1234 56789") == []


if __name__ == "__main__":
    test_simple_words()
    test_mixed_case()
    test_punctuation()
    test_no_matches()
    test_long_repetition()
    test_multiple_in_text()
    test_empty_string()
    test_numbers()
    test_non_repeating_numbers()
    print("Все тесты прошли успешно!")