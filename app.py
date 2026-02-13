import streamlit as st
import datetime
from datetime import date
import time 

NAME="Vivi"
MESSAGE="Hi Poorvi, do you remember the 27th? You know exactly which one I mean, the most special day of my life, the day that means more to me than anything else. That date will always stay close to my heart because it gave me moments I will cherish forever. And do you remember Valentine’s week in 2024? We were standing at the auto stand and you had your favorite flower in your hands. I didn’t give it to you right away and you were a little upset with me, but when I finally did, you took it so gently and placed it inside your diary like it was something precious. That moment still makes me smile because it was not just about a flower, it was about us. And now here we are, another Valentine’s Day, your Valentine’s Day. This past year has been so beautiful. Yes, there were some hurdles along the way and we both know that, but what matters most is that we faced them together. Every challenge only made us stronger and brought us closer. Poorvi , I just want you to know how deeply I love you. You mean the world to me. You are my peace, my happiness, my strength. You are my home and my safe place. In you I find everything I need. You truly are my everything. On this Valentine’s Day I just want to promise you that my love for you will always remain pure and true. I want to stand beside you in every season of life, in laughter and in tears, in success and in struggle. I want to celebrate many more 27ths with you, create countless new memories and keep choosing you every single day. Happy Valentine’s Day my love. Forever yours."
year=2023
month=5
day=27

if "page" not in st.session_state:
    st.session_state.page=1


def landing_page():
    st.title(f"Hieee, {NAME} 💗")
    #st.title() renders as an h1 behind the scenes.
   
    st.markdown("""
            <style>
            .a{
            text-align:center;
            color:blue; 
            }
            </style>
    

            <div class="a"><h2>Let me take you on a journey, are you ready?</h2></div>
            
            """, unsafe_allow_html=True)
    st.markdown("""
            <style>
            .b{
            text-align:left;
            color:black;
            font-style: italic;
            text-decoration: overline underline; 
                
            }
            </style>
    

            <div class="b"><h6>You'll have to click on each button twice to unlock :")</h6></div>
            
            """, unsafe_allow_html=True)
    
    #to move to teh next page which we will do using if and else later
    if st.button("Yes 💌"):
        st.session_state.page=2


def story_page():
    #the story and images using title, markdown to style, and st.image 
    st.title("🪩 But first....")

    st.markdown(f"""
            <style>
            .a{{
            text-align:center;
            color:#191970; 
            }}
            </style>
    

            <div class="a"><h4>{MESSAGE}</h4></div>
            
            """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 4, 1]) 
    with col2:
        st.write("he")
        #st.image("sakshandvivi.jpeg",width=500)

    if st.button("Next 🎀"):
        st.session_state.page=3
    
def quiz():
    st.title("Ahahahah Quiz Time")
    st.write("Take a screenshot ater answering the questions :)")
    #using radio button where we add the label as question, captions if needed, etc. Also using input for the enxt two questions and saving it. Now it will be added in the list and will be sent to the partner
    q1="🪼 Pick a date idea which matches our vibe"
    o1=['Strolling through nature together ✨','Dinner and a movie 🍱','Cafe Hopping ☕️','Arcade 🎭','Creating art 🎨','Travelling 📬','Clubbing 🎧','Long car drives 🎫']
    a1=st.radio(q1,o1)
    q2="🩰 What's your favourite memory of us?"
    a2=st.text_input(q2)
    q3="🎲 Describe Saksham in 40-50 words"
    a3=st.text_input(q3)
    q4="🫶🏻 Where would you like to travel with me?"
    a4=st.text_input(q4)

    
    if st.button("I'm done 🪅"):
        if a2 and a3 and a4:
            st.markdown(f"""
            <style>
            .a{{
            text-align:center;
            color:#191970; 
            }}
            </style>
            <div class="a"><h4>Our date idea: {a1}. Your favourite memory of us is {a2} (Awwwww). According to you, we can be described by {a3} yayyyyy :P. Vivi, you would like to travel to: {a4} 💫</h4></div>
            """, unsafe_allow_html=True)
        
        else:
            st.write("Please fill all the fields and try again :(")
    if st.button("Next 💿"):
        if a2 and a3 and a4:
            st.session_state.page=4
        else:
            st.write("Please fill all the fields and try again :(")

    


def addonDays():
    st.markdown("""
            <style>
            .e{
            text-align:left;
            color:#191970; 
            font-style:italic;
            
            }
            </style>
    

            <div class="e"><h2>I've loved you for</h2></div>
            
            """, unsafe_allow_html=True)
    x=datetime.datetime.now()
    # Format: date(year, month, day)
    f_date = date(year, month, day)
    l_date = date(int(x.strftime("%Y")), int(x.strftime("%m")), int(x.strftime("%d")))

    # Calculate the difference
    delta = l_date - f_date
    st.markdown(f"""
            <style>
            .f{{
            text-align:center;
            color:yellow; 
            font-style:italic;
            }}
            </style>
    

            <div class="f"><h1>{delta.days} days</h1></div>
            
            """, unsafe_allow_html=True)
    
    st.markdown(f"""
            <style>
            .g{{
            text-align:right;
            color:#191970; 
            font-style:italic;
            }}
            </style>
    

            <div class="g"><h3>and babe I've cherished all of them ❤️‍🔥</h3></div>
            
            """, unsafe_allow_html=True)
    
    
    if st.button("Next 💋"):
        st.session_state.page=5

def buildup():
    col1, col2, col3 = st.columns([1, 6, 1]) 
    with col2:
        st.write("he")
        #st.image("buildup.jpg", width=650)

    if st.button("Okay I'm ready 🫶"):
        st.session_state.page=6

def popping_question():
    col1, col2, col3 = st.columns([1, 6, 1]) 
    with col2:
        st.write("he")
        #st.video("Popping the question.mp4", format="video/mp4", start_time=0, subtitles=None, end_time=None, loop=False, autoplay=True, muted=False, width=650)
    if st.button("Lemme answer 🫧"):
        st.session_state.page=7

def answering():
    if "position_index" not in st.session_state:
        st.session_state.position_index=0

    pos=st.session_state.position_index
    if pos%3==0:
        col1, col2 = st.columns(2)
        with col1:
            if st.button('Yes 💗'):
                st.session_state.page=8
        with col2:
            if st.button('No 😭'):
                st.session_state.position_index+=1
    elif pos%3==1:
        col1,col2,col3=st.columns(3)
        with col1:
            if st.button('Yes 💗'):
                st.session_state.page=8
        with col3:
            if st.button('No 😭'):
                st.session_state.position_index+=1
    else:
        col1, col2 = st.columns(2)
        with col1:
            if st.button('No 😭'):
                st.session_state.position_index+=1
        with col2:
            if st.button('Yes 💗'):
                st.session_state.page=8
                
if st.session_state.page==1:
    landing_page()

elif st.session_state.page==2:
    story_page()

elif st.session_state.page==3:
    quiz()

elif st.session_state.page==4:
    addonDays()

elif st.session_state.page==5:
    buildup()

elif st.session_state.page==6:
    popping_question()

elif st.session_state.page==7:
    answering()
    if st.session_state.page==8:
        st.write("he")
        #st.image("gonna be us.png")

else:
    st.write("aghhhh invalid")
