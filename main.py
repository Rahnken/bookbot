
def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_list = convert_dict_to_list(chars_dict)
    chars_list.sort(reverse=True,key=sort_On)
    print_report(chars_list,num_words,book_path)


def get_num_words(text):
   return len(text.split())

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_On(dict):
    return dict["count"]

def convert_dict_to_list(dict):
    char_list = []
    for key in dict.keys():
        if(key.isalpha()):
            char_list.append({"char":key,"count":dict[key]})
    return char_list


def print_report(char_list,word_count,path):
    print(f"--- Begin report on {path} --- ")
    print(f"{word_count} words we found in document")

    for item in char_list:
        print(f"The '{item['char']}' character was found {item['count']} times")
    print("---End Report---")

main()