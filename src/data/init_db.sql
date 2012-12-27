DROP TABLE IF EXISTS blog;
CREATE TABLE blog(
    id          INTEGER PRIMARY KEY,
    date        TEXT,
    author      TEXT,
    title       TEXT,
    text        TEXT
);

DROP TABLE IF EXISTS notepad;
CREATE TABLE notepad(
    id          INTEGER PRIMARY KEY,
    date        TEXT,
    author      TEXT,
    title       TEXT,
    text        TEXT
);

