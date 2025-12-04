file = open("6.2/spotify.csv", encoding="utf-8")
junk = file.readline()

drake_data = []

for line in file:
	items = line.strip().split(",")
	artist = str(items[-1])
	songtitle = str(items[-2])
	danceability = float(items[1])
	
	if artist == "Drake":
		drake_data.append([danceability, songtitle, artist])
  
for spot in range(len(drake_data)):
    lowScore = spot
    i = spot+1
    for i in range(len(drake_data)):
        if drake_data[i][1] <= drake_data[lowScore][1]:
            lowScore = i
    drake_data[spot], drake_data[lowScore] = drake_data[lowScore], drake_data[spot]

print("Dance score \tSong")
for item in drake_data:
	print(str(item[0]) + "\t\t" + item[1] + " by " + item[2])