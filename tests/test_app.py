from playwright.sync_api import Page, expect
import re

# Tests for your routes go here

# Routes testing
def test_get_albums(page: Page, db_connection):
    db_connection.seed("seeds/music_test.sql")
    page.goto('http://localhost:5001/albums')
    expect(page).to_have_title(re.compile('Albums'))
    
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        "Title: Nevermind Released: 1991",
        "Title: GNX Released: 2024"
    ])

def test_get_single_album(page: Page, db_connection):
    db_connection.seed("seeds/music_test.sql")
    page.goto('http://localhost:5001/albums/2')
    expect(page).to_have_title(re.compile('Albums'))
    
    div_tags = page.locator('div')
    expect(div_tags).to_have_text([
        "Title: GNX Released: 2024"
    ])

def test_post_album(web_client, db_connection):
    db_connection.seed("seeds/music_test.sql")
    response = web_client.post('/albums', data={'title': 'Bleach', 'release_year': 1989})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == f"Successfully created album with title 'Bleach' and release year 1989"

# Tests for the artist routes
def test_get_artists(web_client, db_connection):
    db_connection.seed("seeds/music_test.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Nirvana, Kendrick Lamar"

def test_create_new_artists(web_client, db_connection):
    db_connection.seed("seeds/music_test.sql")
    response = web_client.post('/artists', data={'name': 'Wild Nothing', 'genre': 'Indie'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Successfully created artist Wild Nothing whose genre is Indie"
    
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Nirvana, Kendrick Lamar, Wild Nothing"