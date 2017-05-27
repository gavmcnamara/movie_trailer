import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar", "A Marine on an Alien Planet", "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY" )

lion_king = media.Movie("The Lion King", "About a lion who lost everything and thought he should give up... But when he was needed the most he remebered who he was",
                        "https://upload.wikimedia.org/wikipedia/en/3/3d/The_Lion_King_poster.jpg", "https://www.youtube.com/watch?v=4sj1MT05lAA")

pulp_fiction = media.Movie("Pulp Fiction", "Don't mess with Marcell", "https://upload.wikimedia.org/wikipedia/en/3/3b/Pulp_Fiction_%281994%29_poster.jpg",
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY")

forgetting_sarah_marshall = media.Movie("Forgetting Sarah Marshall", "A man on vacation after a terrible breakup runs into his old lover while finding new love",
                                        "https://upload.wikimedia.org/wikipedia/en/7/7c/Forgetting_sarah_marshall_ver2.jpg", "https://www.youtube.com/watch?v=PyVEHIO6jZ0")

three_hundred = media.Movie("300", "This is Sparta!", "https://vignette4.wikia.nocookie.net/theflophouse/images/7/7e/300-movie-poster.jpg/revision/latest?cb=20111111170631",
                            "https://www.youtube.com/watch?v=UrIbxk7idYA")
                            

#lion_king.show_trailer()
movies = [toy_story, avatar, lion_king, pulp_fiction, forgetting_sarah_marshall, three_hundred ]
#fresh_tomatoes.open_movies_page(movies)                       
#print(media.Movie.valid_ratings)
print(media.Movie.__module__)
print(media.Movie.__name__)
