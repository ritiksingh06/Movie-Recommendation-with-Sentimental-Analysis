import streamlit as st
import pandas as pd
import numpy as np
import main_prediction as mp
import time as t
import streamlit.components.v1 as components


# Reading main movie data and setting movie title as index to avoid random index problem 
hide="""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
"""
st.markdown(hide, unsafe_allow_html=True) 

# wide mode / full screen mode 

def _max_width_():
    max_width_str = f"max-width: 2000px;"
    st.markdown(
        f"""
    <style>
    .reportview-container .main .block-container{{
        {max_width_str}
    }}
    </style>    
    """,
        unsafe_allow_html=True,
    )

_max_width_()

def find_movie(movie,movie_data,user_movie,l):
    with st.spinner("Loading ...."):
        t.sleep(3)

    #rec_from_rev==recommend movie from review model as ri_model
    recommended_movie=mp.rec_from_rev(movie)

    # inde=mp.remove_irrelevent_index(rec,recommended_movie,inde)

    st.write("""
    ### **Your Favourite Movie**
    """)

    # displaying user favourite movie.
    user_fav_movie=movie_data.iloc[[user_movie]]
    st.table(user_fav_movie[l])

    with st.spinner("Searching Recommendation for you ....."):
        t.sleep(2)

    # creating dataset of recommended_movie or similar movies from user
    show_movie=movie_data.loc[recommended_movie,:]

    st.write("""
    ### **Movie Recommended For You**
    """)

    # displaying recommended movie or similar movie
    st.table(show_movie[l])

    st.success("Hope You Like Our Recommendation")
    st.info("Enter Differnet Movie Name To Find More Movie")

def main():
    side_head="""
    <style>
        .side_tit {
            background-color:#23CFC4;
            text-align:center;
            left:2px;
            width:100%
            font-style:oblique;
        }
    </style>
    <div class="side_tit">
    <h3> Hollywood Movie Finder</h3>
    </div>
    """
    st.sidebar.markdown(side_head,unsafe_allow_html=True)
    De_Dv="""
    <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
    <style>
        .credit {
            background-color:#23CFC4;
            text-align:center;
            left:2px;
            width:100%
        }
        h3 {
            text-alihn:center;
            font-style:oblique;
            font family:'Lobster', cursive;
        }
        h4 {
            text-align:Center;
            color:#0A7490
            font-style:oblique;
        }

    </style>
    <div class="credit">
        <h4>Design and Developed by :<br> Aquib Ahmad and Ritik Singh</h4>

    <div>
    """
    st.sidebar.header("About This Site")
    st.sidebar.info("""In our site we help user to find Hollywood Movie simialr to user favourite Movie.  
    we can done Movie Prediction by calculating Cosine-similarity and semantic-analysis.
    """)
    st.sidebar.markdown(De_Dv,unsafe_allow_html=True)

    #read main data
    movie_data=pd.read_csv("main_data.csv")
    movie_data.set_index("movie_title",inplace=True)
    movie_data.drop(["comb"],axis=1,inplace=True)

    # list l represt order of column to be shown on web
    l=["actor_1_name","actor_2_name","actor_3_name","genres","director_name"]
    # dat=movie_data.iloc[inde]
    # print(dat[[l[0],l[1],l[2]]].head(5))

    title="""
    <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
    <style>
        .title {
            font-family:'Lobster', cursive;
            text-align:center;
            font-size:22px;
        }
        h3 {
            font-family:'Lobster', cursive;
            text-align:center;
            font-size:22px
        }
    </style>
    <div class="title">
    <h1>Hollywod Movie Finder</h1>
    <h3> Find Your Favourite Movie Here</h3>
    <div>
    """
    components.html(title)
    place_holder=st.empty()
    mov="""
    <link href="https://fonts.googleapis.com/css2?family=Lobster&display=swap" rel="stylesheet">
    <style>
        .movi {
            font-family:'Lobster', cursive;
            text-align:left;    
        }
    </style>
    <div class="movi">
    <h4>Enter HollyWood Movie Name</h4>
    </div>
    """
    st.markdown(mov,unsafe_allow_html=True)
    # place_holder.subheader("*Enter hollywood Movie Name*")
    # taking input from user and finding similar movie by using function defined on main_prediction.py
    try:
        n=st.text_input("")
        movie,index,user_movie=mp.recommend(n)
    except IndexError:
        place_holder.subheader("")
    else:
        find_movie(movie,movie_data,user_movie,l)

if __name__ == "__main__":
    main()
















    