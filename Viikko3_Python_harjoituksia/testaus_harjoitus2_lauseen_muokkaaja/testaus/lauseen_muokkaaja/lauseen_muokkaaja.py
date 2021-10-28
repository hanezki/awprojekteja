def muokkaa(lause):
    sanat = lause.split(" ")
    muokattu_lause = ""
    for i in range(len(sanat)):
        # reverse words of 5 or longer
        if len(sanat[i]) >= 5:
            sanat[i] = sanat[i][::-1]
        # make words of 2 uppercase
        elif len(sanat[i]) == 2:
            sanat[i] = sanat[i].upper()
        sanat[0] = sanat[0].title()

        muokattu_lause = " ".join(sanat)
        if muokattu_lause[-1] == "." or muokattu_lause[-1] == "?" or muokattu_lause[-1] == "!":
            pass
        else:
            muokattu_lause += "."

    return muokattu_lause

