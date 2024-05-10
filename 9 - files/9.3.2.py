def my_mp4_playlist(file_path, new_song):
    file_copy = open(file_path, 'r').read()
    file_copy = file_copy.split('\n')
    songs = []
    new_data = ""
    for line in file_copy:
        songs.append(line.split(';')[:-1])
    if len(songs) < 3:
        while len(songs) < 2:
            songs.append([])
        songs.append([new_song])
    elif str(songs[2]) != '[]':
        songs[2][0] = new_song
    else:
        songs[2] = [new_song]
    for song in songs:
        new_data += ';'.join(song)
        if song != []:
            new_data += ';\n'
        else:
            new_data += '\n'
    open(file_path, 'w').write(new_data)
    print(new_data)
    return None

print(my_mp4_playlist("./songs-short.txt", "Hello"))