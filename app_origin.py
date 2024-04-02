import streamlit as st

st.set_page_config(
    page_title="Ian Chen - Engineer, Educator, Entrepreneur",
    page_icon="👨🏻‍💻",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
        border-radius: 50%;
    }
    </style>

    <div class="profile-img">

    ![](https://avatars.githubusercontent.com/u/7678108?v=4)
    </div>
    """,
        unsafe_allow_html=True,
    )
    # st.image('https://avatars.githubusercontent.com/u/7678108?v=4')
with col2:
    st.markdown(
        """
    # Ian Chen (He/Him)
                
    - Instructor at [Lighthouse Labs](https://www.lighthouselabs.ca/)
    - Engineer at [Clio](https://www.clio.com/)
    """
    )

st.markdown(
    """
# Projects

- [Project 1](https://www.google.com)
- [Project 2](https://www.google.com)
- [Project 3](https://www.google.com)
"""
)

st.markdown(
    """
# Contact
""")
col1, col2, col3 = st.columns(3)

# Card with image and text
for col in [col1, col2, col3]:
    col.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 10%;
        }
        </style>

        <div class="profile-img">

        ![](https://avatars.githubusercontent.com/u/7678108?v=4)
        </div>
        """,
        unsafe_allow_html=True,
    )

col1, col2, col3 = st.columns(3)

# Card with image and text
for col in [col1, col2, col3]:
    col.markdown(
        """
        <style>
        .profile-img img {
            width: 100%;
            border-radius: 10%;
        }
        </style>

        <div class="profile-img">

        ![](https://avatars.githubusercontent.com/u/7678108?v=4)
        </div>
        """,
        unsafe_allow_html=True,
    )


ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)