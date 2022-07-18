import streamlit as st


def page():
    st.title("Sobre")
    
    st.image('./images/social-preview-github.png')
    
    team = [{
        'name': 'tayná',
        'bio': '',
        'picture': '',
        'social media': {
            'linkedin':'',
            'twitter':'',
            'e-mail':'',
        }
    },{
        'name': 'douglas',
        'bio': '',
        'picture': '',
        'social media': {
            'linkedin':'',
            'twitter':'',
            'e-mail':'',
        }
    }]
    
    for people in team:
        st.text(people['name'])