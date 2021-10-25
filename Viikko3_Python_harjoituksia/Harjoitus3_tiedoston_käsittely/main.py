def organize_text():
    try:
        with open("teksti.txt") as teksti:
            lines = teksti.read().splitlines()
        lines.sort(key=lambda x: (len(x), x))
        new_text = open("teksti2.txt", "w+")
        for line in lines:
            new_text.write(f"{line}\n")
        new_text.close()
    except FileNotFoundError:
        print("Tiedostoa ei löytynyt")


organize_text()

