import requests

def posterPath(movieId):
    url = f"https://api.themoviedb.org/3/movie/{movieId}?language=en-US"

    headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJmYTNiMTlkYWZlYzNlYzA2YzYxYzFkOTM1NjMxYmZmMSIsInN1YiI6IjY2MzQ2NzRjYWY0MzI0MDEyMjU0OGQ4NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.PjOKXPCX59dvn4c_Cgu9Edoa-FMZLTmUQl67MJ7usUk"
    }

    response = requests.get(url, headers=headers)
    
    return response.json()["poster_path"]


