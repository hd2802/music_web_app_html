from lib.album import Album

class AlbumRepository:
    def __init__(self, db_connection):
        self._connection = db_connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM albums;')
        albums = []
        for row in rows:
            albums.append(Album(row['id'], row['title'], row['release_year']))
        return albums
    
    def create(self, title, release_year):
        self._connection.execute('INSERT INTO albums (title, release_year) \
            VALUES (%s, %s);', [title, release_year])
        
    def get_album_by_id(self, id):
        rows = self._connection.execute('SELECT * FROM albums WHERE id = %s', [id])
        for row in rows:
            album = Album(row['id'], row['title'], row['release_year'])
            return album