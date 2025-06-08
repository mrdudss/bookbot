
def get_num_words(text):
    count = []
    count = text.split()
    total = 0
    for num in count:
        total +=1
    return total

def count_characters(text):
    count = []
    count = text.split()
    char_lib = {}
    for words in text:
        char = list(words)
        for letters in char:
            low_let = letters.lower()
            if low_let in char_lib:
                char_lib[low_let] += 1
            else:
                char_lib[low_let] = 1
    return char_lib




