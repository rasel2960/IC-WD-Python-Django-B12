# 8-16. Imports:
# Using a program you wrote that has one function in it,
# store that function in a separate file.
# Import the function into your main program file,
# and call the function using each of these approaches:
''' ----------------------------------------
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
------------------------------------------- '''

import Album
album = Album.make_album(artist_name='radiohead', album_title='Ok Computer')
print(album)

album = Album.make_album(album_title='Revolver', artist_name='The Beatles')
print(album)

from Album import make_album
album = make_album(artist_name='oasis', album_title="What's The Story Morning Glory")
print(album)

from Album import make_album as ma
album = ma('royston club', 'songs for the spine', 10)
print(album)

import Album as abm
album = abm.make_album(songs_number=10, album_title="You'll be alright kid (chapter 1)", artist_name='alex warren')
print(album)

from Album import *
album = make_album(album_title="50 years-don't stop", songs_number=None, artist_name='fleetwood mac')
print(album)
