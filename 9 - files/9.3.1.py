def my_mp3_playlist(file_path):
    """
    Syntax could be shorter, but it was the easiest way to do everything WHILE thinking of what to do
    """
    file_splitted = open(file_path, 'r').read().split("\n")
    songs = []
    for line in file_splitted:
        songs.append(line.split(';')[:-1])
    returned = ["", 0, ""]
    longest = 0
    count = 0
    most_songs_count = 0
    artists = []
    time = 0

    for song in songs:
        time = (60 * int(song[2].split(':')[0])) + int(song[2].split(':')[1])
        artists.append(song[1])
        count += 1
        if(time > longest):
            returned[0] = song[0]
            longest = time
    returned[1] = count
    for artist in artists:
        if artists.count(artist) > most_songs_count:
            returned[2] = artist
            most_songs_count = artists.count(artist)

    return tuple(returned)


print(my_mp3_playlist("./songs-short.txt"))
print(my_mp3_playlist("./found.txt"))
