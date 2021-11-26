from database import get, run

run('''
    CREATE TABLE IF NOT EXISTS albums (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title STRING NOT NULL,
        description STRING NOT NULL,
        year_released INTEGER NOT NULL,
        artist_id INTEGER NOT NULL
    )
''')

run('''
    CREATE TABLE IF NOT EXISTS songs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name STRING NOT NULL,
        duration INTEGER NOT NULL,
        album_id INTEGER NOT NULL
    )
''')