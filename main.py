import json


count_all = 0
with open('StreamingHistory.json', 'r', encoding='utf-8') as x:
    data = json.load(x)
count_all += len(data)
print('you have', count_all, 'tracks on record')

msTotal = 0
for i in range(count_all):
    msTotal += data[i]['msPlayed']
hrsTotal = msTotal // 3600000
print('you have been listening to music for', hrsTotal, 'hours')

favCount = 0
dickt = {}
for i in range(count_all):
    trackName = data[i]['trackName']
    if trackName not in dickt.keys():
        dickt.update({trackName: 1})
    else:
        dickt[trackName] += 1
dicktKeys = sorted(dickt.keys())
for key in dicktKeys:
    if dickt[key] > favCount:
        favCount = dickt[key]
        favSong = key
print('your favorite song is', favSong)
print('it was played', favCount, 'times')