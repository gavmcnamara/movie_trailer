# Movie Trailer Website

### To see the projects outcome:

  - Download zip file (python_beginner) or go to https://github.com/gavmcnamara/movie_trailer and download or clone repositories
  - Inside of python_beginner folder there is movies foler 
  - inside of movies foler there is fresh_tomatoes.html
  - open fresh_tomatoes.html in webbrowser to see the final outcome

### To view projects code:

  - Download zip file (movie) or go to https://github.com/gavmcnamara/movie_trailer and download or clone repositories
  - open folder (movie) and there will be a multiple python files and a html file
  - right click the file that you would like to view 
  - Open file with your choice of text editor (sublime, pycharm, etc...)
  
### To make edit this project
- Install python
- Use your favorite text editor or download one (such as, sublime text, etc.)
- Open file you would like to edit and enjoy!

### To create your own version of this project 
- Install Python 
- Use your favorite text editor or download one (such as, sublime text, etc.)
- Copy the fresh_tomatoes file either from my project or through the Github repository that Udacity provides: https://github.com/adarsh0806/ud036_StarterCode/blob/master/fresh_tomatoes.py
- Create two more python files and name them media.py and entertainment.py
- In media.py create a class called Movies with a function that will provide the information you feel is necessary for your own movie website (title, storyline, poster image, trailer, etc.)
- In entertainment.py create your instances of each movie you select to be on your webpage. Just make sure you import webbrowser in media.py and import fresh_tomatoes and import media for entertainment.py

Things to keep in mind while creating your own version:
- fresh_tomatoes.py has a function called open_movies_page which will generate your html page once its executed. example: fresh_tomatoes.open_movies_page(Movies). this will put all the movies in your class Movies into an HTML page called fresh_tomatoes.html

### What is this Project?
This Project (Movie Trailer) is a personal webpage that shows the title, poster image, and trailer for my (Gavin McNamara) favorite movies. 

# Modules
### fresh_tomatoes.py

This project uses a module called fresh_tomatoes.py. This module is used for generating a website that will display my favoite movies. This module has a function called open_movies_page that will take a list of my favortie movies and generate an HTML including the content I have provided, which will showcase these movies. 


### media.py
- This file imports the module webbrowser that allows for access to web based documents (in this case the trailer for each movie)
- media.py creates the class "Movies" that uses the init function to generate the title, storyline, poster image, and link to youtube trailer for each instance of the movies. 

### entertainment.py
- This file imports the module fresh_tomatoes and the newly created file media.py 
- It then creates instances of each movie by using media.Movie to access the class Movie
- Inside each instance will be accessing media.py Movie class (tile, storyline, trailer, poster image, and trailer) which will be filled out accordingly with each movie


# Contibutors
This project was inspired from ideas that udacity's program foudations with python provided.They had helped with my understanding of the project and supplied the tools for myself to create my own movie trailer project

Udacity also provided the fresh_tomatoes.py code that was used to generate the fresh_tomatoes.html page  


License
----

MIT
