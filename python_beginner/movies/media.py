import webbrowser

class Movie():

    """ This class provides a way to store movie related information"""
    
    valid_ratings = ["G", "PG", "PG-13", "R"]
    def __init__(self, movie_title, movie_storyline, poster_image,
                          trailer_youtube):
        
        """ This function helps define all the instances we want to include for our movies"""
        
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
   
    def show_trailer(self):
        
        """ This function allows for the movie trailer to be played"""
        
        webbrowser.open(self.trailer_youtube_url)
        

