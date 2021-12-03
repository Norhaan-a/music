from database import run, get
import json

# 3 Skriv ut namnen på alla artister
artists = get('''
    SELECT * FROM artists
''')

for row in artists:
   print(row['name'])

 
# 4 Skriv ut det äldsta albumet
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

# 5 Skriv ut albumet med längts speltid
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

# 6 Uppdatera albumet som saknar year_released med ett årtal
run('''
    UPDATE albums
    SET year_released = 1999
    WHERE year_released is null
''')

# 7 Lägg till data via inmatning:
# Kunna skapa en artist,
add_name = input('Add artist name: ')
add_desc = input('Add artist description: ')
add_thumbnail = input('Add url for thumbnail pic: ')

new_artist = [{
    'name': add_name,
    'description': add_desc,
    'thumbnail': add_thumbnail
}]

for f in new_artist:
    new_f = run('INSERT INTO artists values(NULL, :name, :description, :thumbnail)',f)
    print(new_f)

# skapa album till en artist,
add_title = input('Add album title: ')
add_desc = input('Add album description: ')
add_year_released = input('Add year released for album: ')
add_thumbnail = input('Add url for thumbnail pic: ')
add_artist_id = input('Add artist id for album: ')

new_album = [{
    'title': add_title,
    'description': add_desc,
    'year released': add_year_released,
    'thumbnail': add_thumbnail,
    'artist id': add_artist_id
}]

for g in new_album:
    new_g = run('INSERT INTO albums values(NULL, :title, :description, :year released, :thumbnail, :artist id)',f)
    print(new_f)

# lägga till låtar i ett album
add_name = input('Add song name: ')
add_duration = input('Add song duration: ')
add_youtube_id = input('Add youtube id for song: ')
add_album_id = input('Add album id for song: ')

new_song = [{
    'title': add_title,
    'description': add_desc,
    'year released': add_year_released,
    'thumbnail': add_thumbnail,
    'artist id': add_artist_id
}]

for h in new_song:
    new_h = run('INSERT INTO songs values(NULL, :title, :description, :year released, :thumbnail, :artist id)',f)
    print(new_f)
#run(
 #   f'''
  #  INSERT INTO artists VALUES (NULL, :add_name,:add_desc,:add_thumbnail)
   # ''',{'add_name':add_name,'add_desc':add_desc,'add_thumbnail':add_thumbnail}
#)

# 8 Kunna ta bort en artist, album eller låt via inmatning
#Tänk på: Om man tar bort en artist, borde dess album och låtar också tas bort då?
#Tips: Kolla upp “Cascade on Delete” i SQLite

# 9 Skriv ut medel-längden på en låt i ett album
song_average = get('''
    SELECT title, AVG(duration) AS avg_duration
    FROM songs AS s
    JOIN albums AS a
    ON s.album_id = a.id
    GROUP BY album_id
''')

for row in song_average:
    print(row['title'], (row['avg_duration']))


# 10 Visa den längsta låten från varje album
s_max_length = get('''
    SELECT title, MAX(duration) AS max_duration
    FROM songs AS s
    JOIN albums AS a
    ON s.album_id = a.id
    GROUP BY album_id
''')

for row in s_max_length:
    print(row['title'], (row['max_duration']))

# 11 Visa antal låtar varje artist har
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

# 12 Kunna söka på artister via inmatning

# 13 Kunna söka på låtar via inmatning

# 14 Kunna visa detaljer om en artist där man även ser artistens alla album
artist_details = get('''
    SELECT 
    ar.name AS artist_name
    ,ar.description AS artist_details
    ,group_concat(al.title) AS album_name

    FROM artists AS ar
    JOIN albums AS al
    ON ar.id = al.artist_id
    GROUP BY ar.name;
''')


for row in artist_details:
    print('Artist: '+ row['artist_name'] +'\n'+'Details: '+ (row['artist_details'])+'\n'+'Albums: ' +(row['album_name']))

# 15 Kunna visa detaljer om ett album där man även ser albumets låtar

# 16 Detaljsidan för en artist och album visar även,
# hur många låtar varje album har
# och total speltid för ett album

# 17 Gör så att alla listor går att sortera på olika egenskaper,
# som name, year_released eller duration