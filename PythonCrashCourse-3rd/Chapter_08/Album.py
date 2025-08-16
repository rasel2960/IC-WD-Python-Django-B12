# 8-7. Album:

# Part-1
# Write a function called make_album() that builds a dictionary describing a music album.
# The function should take in an artist name and an album title, and
# it should return a dictionary containing these two pieces of information.
# Use the function to make three dictionaries representing different albums.
# Print each return value to show that the dictionaries are storing the album information correctly.

# Part-2
# Use None to add an optional parameter to make_album() -
# that allows you to store the number of songs on an album.
# If the calling line includes a value for the number of songs,
# add that value to the album’s dictionary.
# Make at least one new function call that includes the number of songs on an album.

# --- Part 1 --- #
def make_album(artist_name, album_title):
    album_info = {}
    album_info['Artist_Name'] = artist_name.title()
    album_info['Album_Title'] = album_title.title()
    return album_info

album1 = make_album('monir khan', 'tomar kono deosh nei')
print(album1)

album1 = make_album('shakira', "hips don't lie")
print(album1)

album1 = make_album('james', 'dag theke jay')
print(album1)

# --- Part 2 --- #
def make_album(artist_name, album_title, songs_number = None):

    album_info = {}
    album_info['Artist_Name'] = artist_name.title()
    album_info['Album_Title'] = album_title.title()
    if songs_number is not None:
        album_info['Songs_Number'] = songs_number
    return album_info

album1 = make_album('shakira', "hips don't lie")
print(album1)

album2 = make_album(album_title="dag theke jay", songs_number=8, artist_name='james')
print(album2)

album3 = make_album('various artist', 'mayer gaan', 12)
print(album3)