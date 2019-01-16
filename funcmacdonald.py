# funcmacdonald.py
# 1/15/19
# Phoenix Iserman
# sings "Old MacDonald Had a Farm"

def main():
    animal1, sound1 = input("Name an animal and the noise it makes, seperated by a comma: ").split()
    animal2, sound2 = input("Name another animal and the noise it makes, seperated by a comma: ").split()
    animal3, sound3 = input("Name another animal and the noise it makes, seperated by a comma: ").split()
    animal4, sound4 = input("Name another animal and the noise it makes, seperated by a comma: ").split()
    animal5, sound5 = input("Name a final animal and the noise it makes, seperated by a comma: ").split()
    lyricBookends = "Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!"
    lyric2p1 = "And on that farm he had a"
    lyric2p2 = "Ee-igh, Ee-igh, Oh!"
    lyric3p1, lyric3p2, lyric3p3 = "with a", "here and a", "there"
    lyric4p1, lyric4p2, lyric4p3 = "here a", "there a", "everywhere a"
    #structure of the song
    print(lyricBookends)
    print(lyric2p1, animal1, lyric2p2)
    print(lyric3p1, sound1, sound1, lyric3p2, sound1, sound1, lyric3p3)
    print(lyric4p1, sound1, lyric4p2, sound1, lyric4p3, sound1, sound1)
    print(lyricBookends)
    print("")
    print(lyricBookends)
    print(lyric2p1, animal2, lyric2p2)
    print(lyric3p1, sound2, sound2, lyric3p2, sound2, sound2, lyric3p3)
    print(lyric4p1, sound2, lyric4p2, sound2, lyric4p3, sound2, sound2)
    print(lyricBookends)
    print("")
    print(lyricBookends)
    print(lyric2p1, animal3, lyric2p2)
    print(lyric3p1, sound3, sound3, lyric3p2, sound3, sound3, lyric3p3)
    print(lyric4p1, sound3, lyric4p2, sound3, lyric4p3, sound3, sound3)
    print(lyricBookends)
    print("")
    print(lyricBookends)
    print(lyric2p1, animal4, lyric2p2)
    print(lyric3p1, sound4, sound4, lyric3p2, sound4, sound4, lyric3p3)
    print(lyric4p1, sound4, lyric4p2, sound4, lyric4p3, sound4, sound4)
    print(lyricBookends)
    print("")
    print(lyricBookends)
    print(lyric2p1, animal5, lyric2p2)
    print(lyric3p1, sound5, sound5, lyric3p2, sound5, sound5, lyric3p3)
    print(lyric4p1, sound5, lyric4p2, sound5, lyric4p3, sound5, sound5)
    print(lyricBookends)



main()
