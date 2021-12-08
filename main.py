from database import run, get
import json

#3 Skriv ut namnen på alla artister
# artists = get('''
#     SELECT * FROM artists
# ''')

# for row in artists:
#    print(row['name'])

 
# 4 Skriv ut det äldsta albumet
# albums = get('''
#     select distinct
#     a.title,
#     a.year_released
#     from albums AS a
#     where a.year_released = (
#     select min(year_released) as min_year
#     from albums)
# ''')

# for row in albums:
#     print(row['title'])

# 5 Skriv ut albumet med längts speltid
# songs = get('''
#     SELECT a.title, s.album_id, sum(duration) as duration
#     FROM songs AS s
#     Join albums AS a
#     ON s.album_id = a.id
#     GROUP BY s.album_id
#     ORDER BY duration DESC LIMIT 1
# ''')

# for row in songs:
#     print(row['title'])

# 6 Uppdatera albumet som saknar year_released med ett årtal
# run('''
#     UPDATE albums
#     SET year_released = 1999
#     WHERE year_released is null
# ''')

# 7 Lägg till data via inmatning:
# Kunna skapa en artist,
# add_name = input('Add artist name: ')
# add_desc = input('Add artist description: ')
# add_thumbnail = input('Add url for thumbnail pic: ')

# new_artist = [{
#     'name': add_name,
#     'description': add_desc,
#     'thumbnail': add_thumbnail
# }]

# for f in new_artist:
#     new_f = run('INSERT INTO artists values(NULL, :name, :description, :thumbnail)',f)
#     print(new_f)

# # skapa album till en artist,
# add_title = input('Add album title: ')
# add_desc = input('Add album description: ')
# add_year_released = input('Add year released for album: ')
# add_thumbnail = input('Add url for thumbnail pic: ')
# add_artist_id = int(input('Add artist id for album: '))

# new_album = [{
#     'title': add_title,
#     'description': add_desc,
#     'year_released': add_year_released,
#     'thumbnail': add_thumbnail,
#     'artist_id': add_artist_id
# }]

# for g in new_album:
#     new_g = run('INSERT INTO albums values(NULL, :title, :description, :year_released, :thumbnail, :artist_id)',g)
#     print(new_g)

# # lägga till låtar i ett album
# add_name = input('Add song name: ')
# add_duration = input('Add song duration in seconds: ')
# add_youtube_id = input('Add youtube id for song: ')
# add_album_id = input('Add album id for song: ')

# new_song = [{
#     'name': add_name,
#     'duration': add_duration,
#     'youtube_id': add_youtube_id,
#     'album_id': add_album_id
# }]

# for h in new_song:
#     new_h = run('INSERT INTO songs values(NULL, :name, :duration, :youtube_id, :album_id)',h)
#     print(new_h)
#run(
 #   f'''
  #  INSERT INTO artists VALUES (NULL, :add_name,:add_desc,:add_thumbnail)
   # ''',{'add_name':add_name,'add_desc':add_desc,'add_thumbnail':add_thumbnail}
#)

# 8 Kunna ta bort en artist, album eller låt via inmatning
#Tänk på: Om man tar bort en artist, borde dess album och låtar också tas bort då?
#Tips: Kolla upp “Cascade on Delete” i SQLite

#delete_artist = run('DELETE FROM artists WHERE id = 4')

# 9 Skriv ut medel-längden på en låt i ett album
# song_average = get('''
#     SELECT title, AVG(duration) AS avg_song_duration_seconds
#     FROM songs AS s
#     JOIN albums AS a
#     ON s.album_id = a.id
#     GROUP BY album_id
# ''')

# for row in song_average:
#     print(row['title'], (row['avg_song_duration_seconds']))


# # 10 Visa den längsta låten från varje album
# s_max_length = get('''
#     SELECT title, MAX(duration) AS max_duration
#     FROM songs AS s
#     JOIN albums AS a
#     ON s.album_id = a.id
#     GROUP BY album_id
# ''')

# for row in s_max_length:
#     print(row['title'], (row['max_duration']))

# # 11 Visa antal låtar varje artist har
# s_per_artist = get('''
#     SELECT COUNT(s.id) AS count_song, artists.name
#     FROM songs AS s
#     JOIN albums AS a
#     ON a.id = s.album_id
#     JOIN artists 
#     ON artists.id = a.artist_id
#     GROUP BY artists.id
# ''')


# for row in s_per_artist:
#     print(row['name'], (row['count_song']))

# 12 Kunna söka på artister via inmatning
# artist_name = input('find an artist by name: ')

# find_artist = get('''
#     SELECT * FROM artists WHERE name LIKE :search''',
#         {'search' : f'%{artist_name}%'})

# for artist in find_artist:
#     print(artist['name'])

# 13 Kunna söka på låtar via inmatning
# song_name = input('find a song by name: ')

# find_song = get('''
#     SELECT songs.id, songs.name FROM songs WHERE name LIKE :search
#     ''',
#         {'search': f'%{song_name}%'}
#     )

# for song in find_song:
#         print(song[0], song[1])

# # 14 Kunna visa detaljer om en artist där man även ser artistens alla album
#artist_details = get(
'''
     SELECT 
     ar.name AS artist_name
     ,ar.description AS artist_details
     ,group_concat(al.title) AS album_name

     FROM artists AS ar
     JOIN albums AS al
     ON ar.id = al.artist_id
     GROUP BY ar.name;
'''
 #)


# for row in artist_details:
#     print('Artist: '+ row['artist_name'] +'\n'+'Details: '+ (row['artist_details'])+'\n'+'Albums: ' +(row['album_name']))

# 15 Kunna visa detaljer om ett album där man även ser albumets låtar
#album_details = get(
#   '''
#      SELECT 
#      al.title AS album_name
#      ,al.description AS album_details
#      ,group_concat(s.name) AS song_name

#      FROM albums AS al
#      JOIN songs AS s
#      on al.id = s.album_id

#      GROUP BY al.title;
#   ''')
#for row in album_details:
   #added str conversion to allow NULL to pass through as string
#   print('Album: '+ row['album_name'] +'\n'+'Details: '+ str(row['album_details'])+'\n'+'Songs: ' +(row['song_name']))

# 16 Detaljsidan för en artist och album visar även,
# hur många låtar varje album har
# och total speltid för ett album
#artist_album_details = get(
#   '''
#      SELECT 
#      ar.name AS Artist_Name
#      ,al.title AS Album_Name
#      ,ar.description AS Artist_Details
#      ,al.description AS Album_Details
#      ,COUNT(s.name) AS Nr_of_songs
#      ,SUM(s.duration) AS Total_duration_in_seconds
#      ,SUM(s.duration)/60 AS Total_duration_in_min

#      FROM artists AS ar
#      JOIN albums AS al
#      ON ar.id = al.artist_id
#      JOIN songs AS s
#      ON al.id= s.album_id

#      group by al.id   
#   ''')
#for row in artist_album_details:
#   print('ARTIST: '+ row['Artist_Name'] +'\n \n'+ 'ARTIST INFO: '+ row['Artist_Details']+'\n'+ '**END OF ARTIST TEXT*' +'\n \n'
#   +'ALBUM: '+ row['Album_Name'] +'\n \n'+'ALBUM INFO: '+ str(row['Album_Details']) +'\n'+ '**END OF ALBUM TEXT*' +'\n \n'
#   +'NR OF SONGS IN ALBUM: ' +str((row['Nr_of_songs'])) + '\n \n' + 'Album length in min: ' + str((row['Total_duration_in_min'])) )
#   print('------END------''\n')

# 17 Gör så att alla listor går att sortera på olika egenskaper,
# som name, year_released eller duration

sorts = get('''
   SELECT * FROM albums
   ORDER BY title DESC
    ''')

for row in sorts:
   print(row['title'])