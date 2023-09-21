stats_1 = [] # [health, damage, speed]

MaxLevel = 12

for h in range(0,MaxLevel):
    for d in range(0,MaxLevel):
        s = MaxLevel - 1 - d - h
        if s < 0:
            break
        stats_1.append([h, d, s])

print(len(stats_1))


for stat in stats_1:
    stat[0] = 100 + stat[0] * 100
    stat[1] = 10 + stat[1] * 10
    stat[2] = 0.1 + stat[2] * 0.1

winCount = []
for stat1 in stats_1:
    winCount.append(0)
    for stat2 in stats_1:
        ttk1 = stat2[0] / (stat1[1] * stat1[2])
        ttk2 = stat1[0] / (stat2[1] * stat2[2])
        if ttk1 < ttk2: # Win or tie is <=
            winCount[len(winCount) - 1] += 1

print(winCount)
print(max(winCount))

for i in range(len(winCount)):
    if winCount[i] == max(winCount):
        print(stats_1[i])
