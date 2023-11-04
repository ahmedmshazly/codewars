def wave(people):
    wave = []
    people = people.lower()
    for l in range(len(people)):
        if people[l] == " ":
            continue
        e = list(people)
        e[l] = e[l].upper()
        wave.append("".join(e))
    return wave

print(wave("  g ap "))