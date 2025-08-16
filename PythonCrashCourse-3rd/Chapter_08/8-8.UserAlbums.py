# 8-8. User Albums:
# Start with your program from Exercise 8-7.
# Write a while loop that allows users to enter an album’s artist and title.
# Once you have that information, call make_album() with the user’s input
# and print the dictionary that’s created.
# Be sure to include a quit value in the while loop.

def make_album(artist, title, songs_number = None):
    album = {
        'Artist': artist,
        'Title': title,
    }

    if songs_number is not None:
        album['Songs_Number'] = songs_number
    return album

while True:
    print(f"Please enter album information:")
    print(f"Enter 'quit' anytime to quit.")

    artist = input("Artist: ")
    if artist.lower() == 'quit':
        break

    title = input("Title: ")
    if title.lower() == 'quit':
        break

    songs_number = input("Number of songs: ")
    if songs_number == "":
        songs_number = None
    if songs_number == 'quit':
        break

    album = make_album(artist, title, songs_number)
    print(album)




