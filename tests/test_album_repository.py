from lib.album_repository import AlbumRepository
from lib.album import Album 

def test_all(db_connection):
    db_connection.seed("seeds/music_test.sql")
    repository = AlbumRepository(db_connection)
    
    albums = repository.all()
    assert albums == [
        Album(1, 'Nevermind', 1991),
        Album(2, 'GNX', 2024)
    ]

def test_creating_new_album(db_connection):
    db_connection.seed("seeds/music_test.sql")
    repository = AlbumRepository(db_connection)

    repository.create('Bleach', 1989)

    albums = repository.all()

    assert albums == [
        Album(1, 'Nevermind', 1991),
        Album(2, 'GNX', 2024),
        Album(3, 'Bleach', 1989)
    ]