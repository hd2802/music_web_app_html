from lib.album import Album

def test_album_creation_is_as_expected():
    album = Album(1, 'Nevermind', 1991)
    assert album.id == 1
    assert album.title == 'Nevermind'
    assert album.release_year == 1991