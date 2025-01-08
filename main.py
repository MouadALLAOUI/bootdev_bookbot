def file_export():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

    return file_contents


def file_contents_lenght(fc):
    return len(fc.split())


def file_content_letter_itteration(fc):
    letters = []
    for word in fc.split():
        for letter in word.lower():
            found = False
            if not letter.isalpha():
                continue
            for leter in letters:
                if letter == leter["letter"]:
                    leter["num"] += 1
                    found = True
                    break
            if not found:
                letters.append({"letter": letter, "num": 1})
    return letters


def sort_on(dict):
    return dict["num"]


def main():
    file_contents = file_export()
    fcl = file_contents_lenght(file_contents)
    fcli = file_content_letter_itteration(file_contents)

    fcli.sort(reverse=True, key=sort_on)

    #
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{fcl} words found in the document")
    for letter in fcli:
        print(f"The '{letter['letter']}' character was found {letter['num']} times")
    print("--- End report ---")


main()
