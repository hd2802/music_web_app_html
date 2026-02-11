CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title text,
    release_year int
);

CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name text,
    genre text
);

INSERT INTO albums (title, release_year) VALUES ('Nevermind', 1991), ('GNX', 2024);

INSERT INTO artists (name, genre) VALUES ('Nirvana', 'Grunge'), ('Kendrick Lamar', 'Hip-Hop');