import spotipy
from spotipy.oauth2 import SpotifyOAuth
# spotipy 2.23.0

# Встановіть свої дані з Spotify Developer Dashboard
CLIENT_ID = 'id'
CLIENT_SECRET = 'secret'
REDIRECT_URI = 'http://localhost:8888/callback/'

# Створення об'єкта авторизації для доступу до плейлистів
sp_playlists = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                                         client_secret=CLIENT_SECRET,
                                                         redirect_uri=REDIRECT_URI,
                                                         scope='playlist-read-private'))


# Ім'я файлу для зберігання назв треків з плейлистів
playlist_output_file = 'playlist_tracks.txt'

# Отримання списку плейлистів користувача
playlists = sp_playlists.current_user_playlists()

# Запис назв треків з плейлистів у файл
with open(playlist_output_file, 'w', encoding='utf-8') as file:
    for playlist in playlists['items']:
        file.write(f"NAME PLAYLIST: {playlist['name']}\n")
        playlist_id = playlist['id']
        tracks = sp_playlists.playlist_tracks(playlist_id)
        for track in tracks['items']:
            if track and track['track']:
                track_info = track['track']
                track_name = track_info['name']
                artists = ', '.join([artist['name'] for artist in track_info['artists']])
                file.write(f"{track_name} - {artists}\n")
            else:
                file.write("none information\n")
        file.write('\n')  # Додатковий рядок між плейлистами


print(f"Name saved in : {playlist_output_file}")
