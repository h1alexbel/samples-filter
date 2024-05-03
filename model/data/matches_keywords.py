import pandas

keywords = ["example", "tutorial", "sample", "examples", "samples", "tutorials"]


def matches(input):
    if pandas.notna(input):
        words = input.lower().split()
        return any(keyword in words for keyword in keywords)
    return False
