def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        strings = file_contents.lower()

        word_dict = {}

        for s in strings:
            if s.isalpha():
                if s in word_dict:
                    word_dict[s] += 1
                else:
                    word_dict[s] = 1
        
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{len(words)} words found in the document")
        print()

        for wd in word_dict:
            print(f"The '{wd}' character was found {word_dict[wd]} times")

        print("--- End report ---")

main()