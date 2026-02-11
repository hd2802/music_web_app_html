from lib.artist_repository import ArtistRepository
from lib.artist import Artist 

def test_all(db_connection):
    db_connection.seed("seeds/music_test.sql")
    repository = ArtistRepository(db_connection)

    artists = repository.all()

    assert artists == [
        Artist(1, "Nirvana", "Grunge"),
        Artist(2, 'Kendrick Lamar', 'Hip-Hop')
    ]

def test_create(db_connection):
    db_connection.seed("seeds/music_test.sql")
    repository = ArtistRepository(db_connection)

    repository.create('Wild Nothing', 'Indie')

    artists = repository.all()

    assert artists == [
        Artist(1, "Nirvana", "Grunge"),
        Artist(2, 'Kendrick Lamar', 'Hip-Hop'),
        Artist(3, 'Wild Nothing', 'Indie')
    ]