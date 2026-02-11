from lib.artist import Artist 

def test_initialisation():
    artist = Artist(1, 'Nirvana', 'Grunge')
    assert artist.id == 1
    assert artist.name == 'Nirvana'
    assert artist.genre == 'Grunge'

def test_equal():
    artist1 = Artist(1, 'Nirvana', 'Grunge')
    artist2 = Artist(1, 'Nirvana', 'Grunge')
    assert artist1 == artist2

def test_string():
    artist = Artist(1, 'Nirvana', 'Grunge')
    assert str(artist) == "Artist(1, Nirvana, Grunge)"