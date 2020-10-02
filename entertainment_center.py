import media
import urllib.request
import urllib.parse
import json
import fresh_tomatoes

movies = [] # To store all the instance variables
names = ["forrest gump","Avengers","avatar","inception","fight club","the matrix"] # List that contains names of movies
OMDBapikey = "" # Add your api key that is obtained from omdbapi
youtubeAPIkey = "" # Add your youtube api key



# A function to get the video id of youtube's trailer
def getTrailerID(title):
    url = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/search?part=id&maxResults=1&q="+ urllib.parse.quote(title+" trailer") +"&type=videoId&key="+youtubeAPIkey)
    output = url.read().decode("utf-8")
    loaded_json = json.loads(output)
    id = loaded_json['items'][0]['id']['videoId']
    return id
    # return "https://www.youtube.com/watch?v="+id


# A function to get the IMDB details
def details(title):
    detailsection =  urllib.request.urlopen("http://www.omdbapi.com/?t="+urllib.parse.quote(title)+"&apikey="+OMDBapikey)
    output = detailsection.read().decode("utf-8")
    loaded_json = json.loads(output)
    ID = getTrailerID(title)
    movies.append(media.Movie(loaded_json['Title'],loaded_json['Plot'],loaded_json['Poster'],ID))

with open('movies.json') as movies:
  data = json.load(movies)

print(data['movies'])



#for name in names:
#    details(name)

#fresh_tomatoes.open_movies_page(movies)