from database import run, get

# Skriv ut namnen på alla artister
artists = get('''
    SELECT * FROM artists
''')

for row in artists:
   print(row['name'])

 
# Skriv ut det äldsta albumet
albums = get('''
    select distinct
    a.title,
    a.year_released
    from albums AS a
    where a.year_released = (
    select min(year_released) as min_year
    from albums)
''')

for row in albums:
    print(row['title'])

# Skriv ut albumet med längts speltid
songs = get('''
    SELECT a.title, s.album_id, sum(duration) as duration
    FROM songs AS s
    Join albums AS a
    ON s.album_id = a.id
    GROUP BY s.album_id
    ORDER BY duration DESC LIMIT 1
''')

for row in songs:
    print(row['title'])

# Uppdatera albumet som saknar year_released med ett årtal
run('''
    UPDATE albums
    SET year_released = 1999
    WHERE year_released is null
''')

#Lägg till data via inmatning, Kunna skapa en artist, skapa album till en artist, lägga till låtar i ett album

#Kunna ta bort en artist, album eller låt via inmatning
#Tänk på: Om man tar bort en artist, borde dess album och låtar också tas bort då?
#Tips: Kolla upp “Cascade on Delete” i SQLite

# Skriv ut medel-längden på en låt i ett album
song_average = get('''
    SELECT title, AVG(duration) AS avg_duration
    FROM songs AS s
    JOIN albums AS a
    ON s.album_id = a.id
    GROUP BY album_id
''')

for row in song_average:
    print(row['title'], (row['avg_duration']))


# Visa den längsta låten från varje album
s_max_length = get('''
    SELECT title, MAX(duration) AS max_duration
    FROM songs AS s
    JOIN albums AS a
    ON s.album_id = a.id
    GROUP BY album_id
''')

for row in s_max_length:
    print(row['title'], (row['max_duration']))

# Visa antal låtar varje artist har
s_per_artist = get('''
    SELECT COUNT(s.id) AS count_song, artists.name
    FROM songs AS s
    JOIN albums AS a
    ON a.id = s.album_id
    JOIN artists 
    ON artists.id = a.artist_id
    GROUP BY artists.id
''')


for row in s_per_artist:
    print(row['name'], (row['count_song']))

# 14 Kunna visa detaljer om en artist där man även ser artistens alla album
artist_details = get('''
    select 
    ar.name as artist_name
    ,al.title as album_name
    ,ar.description as artist_details
    
    from artists ar
    inner join albums al
    on ar.id = al.artist_id;
''')


for row in artist_details:
    print(row['artist_name'], (row['artist_details']),(row['album_name']))