from fastapi import FastAPI, Body
from data.movies import MOVIES

app = FastAPI()

@app.get("/api/v1/movies")
async def read_all_movies(genre: str | None = None, director: str | None = None) -> list:
    filtered_movies : list = []

    if genre is not None and director is not None:
        for movie in MOVIES:
            if movie.get("genre").lower() == genre.lower() and movie.get("director").lower() == director.lower():
                filtered_movies.append(movie)

        return filtered_movies
    
    if genre is not None:
        for movie in MOVIES:
            if movie["genre"].lower() == genre.lower():
                filtered_movies.append(movie)
                
    if director is not None:
        for movie in MOVIES:
            if movie["director"].lower() == director.lower():
                filtered_movies.append(movie)


    if len(filtered_movies) != 0:
        return filtered_movies
    return MOVIES

@app.get("/api/v1/movies/{movie_id}")
async def read_movie(movie_id : int) -> dict:
    for movie in MOVIES:
        if movie.get("id") == movie_id:
            return movie
        
    return { "detail": "Movie not found"}

@app.post("/api/v1/movies")
async def create_movie(new_movie: dict = Body(...)) -> list:
    new_movie["id"] = len(MOVIES)
    MOVIES.append(new_movie)
    return MOVIES

@app.put("/api/v1/movies/{movie_id}")
async def update_movie_put(movie_id: int, movie: dict = Body(...)) -> dict:
    if movie_id < 0 or movie_id > len(MOVIES) - 1:
        return { "detail": "Movie not found" }
    movie_to_update: dict = MOVIES[movie_id]
    movie_to_update.update(movie)
    return movie_to_update

@app.patch("/api/v1/movies/{movie_id}")
async def update_movie_patch(movie_id: int, movie: dict = Body(...)) -> dict:
    if movie_id < 0 or movie_id > len(MOVIES) - 1:
        return { "detail": "Movie not found" }
    movie_to_update: dict = MOVIES[movie_id]
    movie_to_update.update(movie)
    return movie_to_update

@app.delete("/api/v1/movies/{movie_id}")
async def delete_movie(movie_id: int) -> list:
    if movie_id < 0 or movie_id > len(MOVIES) - 1:
        return { "detail": "Movie not found" }
    MOVIES.pop(movie_id)
    index : int = 0
    for movie in MOVIES:
        movie["id"] = index
        index += 1
    return MOVIES