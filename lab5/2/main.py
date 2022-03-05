
def getTime(ora):
    h, m = ora.split(":")
    return int(h) * 60 + int(m)

def getTimestampString(timestamp):
    m = timestamp % 60
    h = timestamp / 60
    return "%02d:%02d" % (h, m)

with open("spectacole.txt", "r") as f:
    spectacole = []
    for line in f:
        tok = line.split(" ")
        ore = tok[0].split("-")
        spectacole.append((getTime(ore[0]), getTime(ore[1]), " ".join(tok[1:])))
        

    spectacole_sortate = sorted(spectacole, key=lambda x: x[1])
    
    out = open("programare.txt", "w")
    ultim = 0
    for spectacol in spectacole_sortate:
        if spectacol[0] >= ultim:
            ultim = spectacol[0]
            out.write("%s-%s %s" % (getTimestampString(spectacol[0]), getTimestampString(spectacol[1]), spectacol[2]))

    out.close()
