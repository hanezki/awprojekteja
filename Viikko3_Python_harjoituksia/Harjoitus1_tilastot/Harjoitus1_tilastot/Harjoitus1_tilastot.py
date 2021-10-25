import statistics

# laske numerolistasta erilaisia tilastoja
def näytä_tilastot(numerot):
    minimi = min(numerot)
    maksimi = max(numerot)
    keskiarvo = statistics.mean(numerot)
    mediaani = statistics.median(numerot)
    moodi = statistics.mode(numerot)
    print(f"Minimi: {minimi}\nmaksimi: {maksimi}\nkeskiarvo: {keskiarvo}\nmediaani: {mediaani}\nmoodi: {moodi}")

try:
    numerot = input("Anna lista numeroita, erota numerot pilkulla (esim. 1, 2, 3, 4)\n>")
except ValueError:
    print("Virheellinen syöte")

# pilko lista "," merkin kohdilla ja muuta string lista numero listaksi
numerot_lista = numerot.split(",")
numerot_lista = [int(i) for i in numerot_lista]

näytä_tilastot(numerot_lista)