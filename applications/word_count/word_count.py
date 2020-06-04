import re


def word_count(s):
    # Your code here
    word_count = {}
    arr = re.split(r"[\.\s | ,\s | \s]+", s)
    for word in arr:
        low = word.lower()
        if low in word_count:
            word_count[low] += 1
        else:
            word_count[low] = 1
    if "" in word_count:
        del word_count[""]
    return word_count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
