



CREATE TABLE Episode (
    EID             INTEGER PRIMARY KEY,
    tconst          TEXT,
    seasonNumber    INTEGER,
    episodeNumber   INTEGER,
    title           TEXT,
    averageRating   REAL,
    numVotes        INTEGER,
    duration        INTEGER
);

CREATE TABLE Cast (
    CID             INTEGER PRIMARY KEY,
    slug            TEXT,
    nconst          TEXT,
    firstName       TEXT,
    lastName        TEXT,
    gender          BOOLEAN,
    culture         TEXT,
    isMarried       BOOLEAN,
    isNoble         BOOLEAN,
    age             INTEGER
);

CREATE TABLE EpisodeCast (
    UID             INTEGER PRIMARY KEY,
    EID             INTEGER REFERENCES Episode(EID),
    CID             INTEGER REFERENCES Cast(CID)
);