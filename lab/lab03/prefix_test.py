from prefix import prefix_search

def test_documentation():
    assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "a") == { "ac": 1, "ab": 3}

def test_exact_match():
    assert prefix_search({"category": "math", "cat": "animal"}, "cat") == {"category": "math", "cat": "animal"}

def test_empty():
    assert prefix_search({}, "a") == {}

def test_noresult():
    assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "c") == {}

def test_number():
    assert prefix_search({"ac": 1, "ba": 2, "ab": 3}, "3") == {}

def test_rough_match():
    assert prefix_search({"hicatty": "math", "cat": "animal"}, "cat") == {"cat": "animal"}
