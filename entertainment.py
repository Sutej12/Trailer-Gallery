import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=LDXYRzerjzU")

avatar = media.Movie("Avatar", "A animation", "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=6ziBFh3V1aM")

avengers = media.Movie("Avengers:- Endgame", "We're in the EndGame Now", "https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg", "https://www.youtube.com/watch?v=ee1172yeqyE")

captain_marvel = media.Movie("Captain Marvel", "The new Avenger", "https://upload.wikimedia.org/wikipedia/en/8/85/Captain_Marvel_poster.jpg", "https://www.youtube.com/watch?v=Z1BCujX3pw8")


movies = [captain_marvel, avengers, avatar, toy_story]
fresh_tomatoes.open_movies_page(movies)