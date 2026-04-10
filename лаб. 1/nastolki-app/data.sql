CREATE TABLE IF NOT EXISTS games (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    min_players INTEGER,
    max_players INTEGER,
    min_play_time INTEGER,
    max_play_time INTEGER,
    UPDT INTEGER
);