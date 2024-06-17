def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_contents = file_contents.lower()

        print("-- -- Begin report of books/frankenstein.txt -- --")

        words = file_contents.split()
        
        print(f"{len(words)} words found in this document")

        count = {}

        for word in words:
            for character in word:
                if character in count:
                    count[character] += 1
                else:
                    count[character] = 1
        
        count = [{'character': character, 'count': value} for character, value in count.items()]
        count.sort(reverse = True, key = lambda x: x['count'])

        for character in count:
            if character['character'].isalpha() == True:
                print(f"The {character['character']} character was found {character['count']} times")

if __name__ == "__main__":
    main()