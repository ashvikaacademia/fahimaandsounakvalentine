import streamlit as st
import datetime
from datetime import date
import time 

NAME="Sounak"
MESSAGE="We met randomly, you are my hb's best friend. But after like 3 days we connected so well that we actually started dating officially and it's been like a month. My favourite memory with you when on 23rd January we were returning from our date the car ride home was so romantic. We were both exhausted and most sleepy and our heads leaned towards each other and that's when I told you about my feelings for you. It was the most special moment. If I had to describe our relationship in one word it'd be a dream. After meeting you, I genuinely feel like you are just tailor made for me lol. I want to explore more quiet places holding hands and sharing airpods.I love how you listen to my yaps all the time and remember everything <3"
year=2026
month=1
day=9

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
        st.image("fahimaandsounak.jpeg",width=400)

    if st.button("Next 🎀"):
        st.session_state.page=3
    
def quiz():
    st.title("Ahahahah Quiz Time")
    st.write("Take a screenshot ater answering the questions :)")
    #using radio button where we add the label as question, captions if needed, etc. Also using input for the enxt two questions and saving it. Now it will be added in the list and will be sent to the partner
    q1="🪼 Pick a date idea which matches our vibe"
    o1=['Strolling through nature together ✨','Dinner and a movie 🍱','Cafe Hopping ☕️','Arcade 🎭','Creating art 🎨','Bookclub 📬','Clubbing 🎧','Long car drives 🎫']
    a1=st.radio(q1,o1)
    q2="🩰 What's your favourite memory of us?"
    a2=st.text_input(q2)
    q3="🎲 Describe us in one word"
    a3=st.text_input(q3)
    q4="🫶🏻 What's your favourite thing about me?"
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
            <div class="a"><h4>Our date idea: {a1}. Your favourite memory of us is {a2} (Awwwww). According to you, we can be described by {a3} yayyyyy :P. Sounak, your favourite thing about me is: {a4} 💫</h4></div>
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
        st.image("buildup.jpg", width=650)

    if st.button("Okay I'm ready 🫶"):
        st.session_state.page=6

def popping_question():
    col1, col2, col3 = st.columns([1, 6, 1]) 
    with col2:
        st.write("d")
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
        st.image("gonna be us.png")

else:
    st.write("aghhhh invalid")


        
        
