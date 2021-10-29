def lue(tiedosto, rivinumero):
    try:
        with open(tiedosto) as teksti:
            lines = teksti.read().splitlines()
            if len(lines) == 0:
                return "Empty file."
            else:
                return lines[rivinumero]
    except FileNotFoundError:
        return "File not found."
    except IndexError:
        raise IndexError("Väärä index")

