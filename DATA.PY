separates_albums = '#'
Separates_songs = '*'
Separates_data = '::'
FILE = 'DATA.TXT'


def List_of_albums(filename):
    album_name = []
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        if line[0] == '#':
            line = line.replace('#', '').replace('::', '-')
            album_name.append(line)
    return album_name


def list_of_Song_in_album(filename, albumname):
    song_list = ''
    count = 0
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        count = count +1
        if albumname in line:
            for line in lines[count:]:
                if line[0] == '*':
                    song_list = song_list + line
                if line[0] =='#':
                    return song_list


def song_length(filename, songname):
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        if songname in line:
            return (line.replace('*',"").replace('::',' '))


def lyrics_of_a_song(filename, songmame):
    count = 0
    song_lyrics = ''
    song_title = ''
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        count = count +1
        if songmame in line:
            for line in lines[count:]:
                if line[0] == '*' or line[0] == '#':
                    song_title = song_length(FILE, songmame)
                    return song_title + song_lyrics
                else:
                    song_lyrics = song_lyrics + line


def What_album_is_the_song_on(filename, songmane):
    list_of_album = List_of_albums(filename)
    list_of_songs = ''
    for album in list_of_album:
        list_of_songs = list_of_Song_in_album(filename, album.replace('-','::'))
        if songmane in list_of_songs:
            return album


def word_in_song_name(filename, word):
    list_of_song_name_whit_word = []
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        if line[0] == '*' and (word in line or word.upper() in line or word.lower() in line):
            list_of_song_name_whit_word.append(line)
    return list_of_song_name_whit_word


def words_in_the_song(filename, word):
    list_of_song_whit_word = []
    song_name = ''
    count = 0
    f = open(filename, "r")
    lines = f.readlines()
    f.close()
    for line in lines:
        count = count +1
        if line[0] == '*':
            song_name = line
            continue
        elif word in line or word.upper() in line or word.lower() in line:
            if line[0] == '#' :
                continue
            else:
                list_of_song_whit_word.append(song_name)

    list_of_song_whit_word = list(dict.fromkeys(list_of_song_whit_word))
    return list_of_song_whit_word




if __name__ == '__main__':

 print(words_in_the_song(FILE, 'The'))