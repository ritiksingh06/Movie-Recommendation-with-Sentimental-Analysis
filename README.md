# Movie-Recommendation-with-Sentimental-Analysis
Content Based Recommender System recommends movies similar to the movie user likes and analyses the sentiments on the reviews given by the user for that movie.

Link to view the applicatij :- https://hollywood-movie-recommend.herokuapp.com/

# Requirement For This Project 
1. pandas==1.0.3
2. numpy==1.18.1
3. scikit-learn==0.22.1
4. nltk==3.4.5
5. Flask==1.1.2
6. jinja2==2.11.2
  
## For Deploy at heroku we require gunicorn to run web app
  gunicorn==19.9.0

# To Run This Project
1.  install all the requirements
2.  Take a copy of this Repository In your locl drive
3.  Run this Command on your Terminal/cmd **python main.py**

# output 
![Screenshot from 2020-09-23 22-05-24](https://user-images.githubusercontent.com/67313757/94043025-e803ec80-fde9-11ea-8432-2418a3759efc.png)

![Screenshot from 2020-09-23 22-05-44](https://user-images.githubusercontent.com/67313757/94043037-ec300a00-fde9-11ea-8023-7366a0eb572c.png)

![Screenshot from 2020-09-23 22-05-57](https://user-images.githubusercontent.com/67313757/94043048-efc39100-fde9-11ea-8d45-ed77a39bb084.png)


# Sources of the datasets
The details of the movies(title, genre, runtime, rating, poster, etc) are fetched using an API by TMDB, https://www.themoviedb.org/documentation/api, and using the IMDB id of the movie in the API, web scraping was done  to get the reviews given by the user in the IMDB site using beautifulsoup4 and sentimental analysis was performed on those reviews.

1. https://www.kaggle.com/carolzhangdc/imdb-5000-movie-dataset

2. https://www.kaggle.com/rounakbanik/the-movies-dataset

3. https://en.wikipedia.org/wiki/List_of_American_films_of_2018

4. https://en.wikipedia.org/wiki/List_of_American_films_of_2019

5. https://en.wikipedia.org/wiki/List_of_American_films_of_2020
