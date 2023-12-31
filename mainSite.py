import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(
    page_title="Portfolio with streamlit",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items=  {"About": "This is a Streamlit project"}
)

#no widget here
selected=option_menu(
    None,
    ["Home","Projects","Contact"],
    icons=["house","book","envelope"], menu_icon="cast", default_index=0,
    orientation="horizontal"    
)
if(selected=="Home"):
    st.title("About me")
    col1,col2=st.columns([1,2])
    with st.container():
        col1.image("Assets/Illustration.png", width=300)
        col1.subheader("Yasin Yeşilyurt")

    with st.container():
        col2.markdown("---")
        col2.header("""Artificial Intelligence Engineering Student in TOBB ETÜ \n (used to be) a Game Developer""")
        col2.text("Email me at: yasinyesilyurt_@hotmail.com")
        col2.caption("Ankara/Turkey")
        col2.markdown("---")

    abtMe="""\t I started programming in highscool when there were shutdowns due to pandemic. My projects consisted of 2 mobile games and 1 game jam game.
    Now i am mostly interested in artificial intelligence workfields and I selected my major according to this. 
    I want to mainly work on natural language processing image processing and other AI fields or maybe other ones that I don't know about."""
    
    st.markdown("---")
    st.text(abtMe)
    st.markdown("---")
    st.subheader("Skills")
    col1.empty()
    col2.empty() #you have to empty them before opening a new column
    
    cols1,cols2,cols3,cols4=st.columns([2,2,7,12])
    cols1.image("Assets/java.png",width=90)
    cols2.header("Java")
    cols1.image("Assets/csharplogo.png",width=90)
    cols2.header("C# with Unity")
    cols1.image("Assets/pythonlogo.png",width=90)
    cols2.header("Python")
    st.caption("And some libraries of these")
    with cols4:
        st.write("## Current year in Tobb Etü ")
        st.metric(label="Year", value="1", delta="1 grade/year")
    cols1.empty()
    cols2.empty()
    cols3.empty()
    cols4.empty()
    st.markdown("---")
 
#end of if
elif(selected=="Projects"):
    st.title("Projects")
    st.markdown("---")
    map1,map2=st.columns([3,5])

    with map1:
        st.header("Escape from Computer")
        st.caption("Featured")
        st.image("Assets/escBanner.png")
    with map2:
        st.subheader("About: ")
        st.text("A platformer game with a short story and great athmosphere")
        st.write("Game page [link](https://cheeseburgerhere.itch.io/escape-from-computer)")
        with st.expander("Screenshots from game: "):
            scr1,scr2,scr3=st.columns(3)
            scr1.image("Assets/escScr1.png")
            scr2.image("Assets/escScr2.png")
            scr3.image("Assets/escScr3.png")  

    map1.empty()
    map2.empty()
    st.markdown("---")
    maps1, maps2=st.columns([3,5])
    
    with maps1:
        st.header("Square with a Gun")
        st.image("Assets/SwGBanner.png",width=300)
    with maps2:
        st.subheader("About: ")
        st.text("Quick arcade game to pass time")
        st.write("Game page [link](https://cheeseburgerhere.itch.io/square-with-a-gun)")
        with st.expander("Screenshots from game: "):
            st.image("Assets/SwgScr.png")

    maps1.empty()
    maps2.empty()
    st.markdown("---")
    maps1, maps2=st.columns([3,5])
    
    with maps1:
        st.header("Stuck Together")
        st.image("Assets/StBanner.png",width=500)
    with maps2:
        st.subheader("About: ")
        st.text("A Game Jam game made in 1 week")
        st.write("Game page [link](https://cheeseburgerhere.itch.io/stuck-together)")
    #end of projects section

elif(selected=="Contact"):
    st.title("My Contacts: ")
    c1,c2=st.columns(2)
    with c1:
        st.markdown("---")
        st.subheader("[LinkedIn 🌐](https://www.linkedin.com/in/yasin-yesilyurt/)")
        st.markdown("---")
        st.subheader("[Github 💭](https://github.com/cheeseburgerhere)")
    with c2:
        st.markdown("---")
        st.subheader("Personal Email 👓: yasinyesilyurt_@hotmail.com")
        st.markdown("---")
        st.subheader("Developer Email 👜: divisiondevelopment@hotmail.com")
        st.markdown("---")
        st.subheader("[Itch.io page 👾](https://cheeseburgerhere.itch.io/)")
