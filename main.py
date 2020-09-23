from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import main_prediction as mp

movie_data=pd.read_csv("datasets/main_data.csv")
movie_data.set_index("movie_title",inplace=True)
movie_data.drop(["comb"],axis=1,inplace=True)
l=["actor_1_name","actor_2_name","actor_3_name","genres","director_name"]

def pred(n):
    movie,inde,user_movie=mp.recommend(n)
    recommended_movie=mp.rec_from_rev(movie)

    user_fav_movie=movie_data.iloc[[user_movie]]
    # print(user_fav_movie)
    # print("rec_movie")
    show_movie=movie_data.loc[recommended_movie,:]
    # print(show_movie[l].to_html())
    return user_fav_movie,show_movie
# n=input("enter movie:-")
# pred(n,l)





app=Flask(__name__)
@app.route("/", methods=("GET","POST"))
def home():
    if request.method=="POST":
        n=request.form['usrmovie']
        # print(n)
        if n=="":
            err="please Enter Movie Name"
            return render_template("index.html",err=err)
        else:
            try:
                usr_movie,recom_movie=pred(n)
            except IndexError:
                err="enter correct movie name"
                return render_template("index.html",err=err)
            else:
                fav="Your Favouriate Movie"
                rec="Movie Recommended For You"
                return render_template('index.html', tables=[recom_movie[l].to_html(classes='user_movie',index_names=False)],
                                                tabs=[usr_movie[l].to_html(classes='user_movie',index_names=False)],
                                                rec=rec,fav=fav)
         
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)


