
# gets number of words in text
def get_num_words(text):
    words = text.split()
    return len(words)

# takes text from book as a string, and returns the number of times each character appears in the string
def get_num_characters(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars   