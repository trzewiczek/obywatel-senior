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

DROP TABLE IF EXISTS calendar;
CREATE TABLE calendar(
    id          INTEGER PRIMARY KEY,
    status      TEXT,
    date        TEXT,
    person      TEXT,
    title       TEXT,
    text        TEXT
);

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses(
    id          INTEGER PRIMARY KEY,
    person      TEXT,
    name        TEXT,
    address     TEXT,
    zip         TEXT,
    city        TEXT,
    phone       TEXT,
    email       TEXT,
    newsletter  INTEGER
);

DROP TABLE IF EXISTS newsletter;
CREATE TABLE newsletter(
    id          INTEGER PRIMARY KEY,
    date        TEXT,
    title       TEXT,
    text        TEXT
);
