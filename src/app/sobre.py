import streamlit as st

team = [{
    'name': 'Tayná Fiúza',
    'bio': 'Aprendiz em ciência de dados, biotecnologista, mestre e doutoranda em bioinformática. Fortalezense morando em Natal.',
    'picture': './images/team_tayna.png',
    'social media': {
        'linkedin':'',
        'github':'https://github.com/fiuzatayna',
        'e-mail':'taynafiuza2@gmail.com',
    }
},{
    'name': 'Douglas Araújo',
    'bio': 'Estudante de Ciência da Computação na Universidade Estadual do Ceará (UECE). Pesquisador/bolsista associado do Laboratório LAURA do Programa de Pós-Graduação em Ciência da Computação da UECE.',
    'picture': './images/team_douglas.jpeg',
    'social media': {
        'linkedin':'',
        'github':'https://github.com/DouglasArS',
        'e-mail':'douglas.as.016@gmail.com',
    }
},{
    'name': 'Samya Maria',
    'bio': 'Iniciante em ciência de dados, cursando Ciência da Computação.',
    'picture': './images/team_samya.jpg',
    'social media': {
        'linkedin':'',
        'github':'https://github.com/SamyaMaria',
        'e-mail':'saamyamaria@gmail.com',
    }
}]
    

def page():
    st.title("Sobre")
    st.image('./images/social-preview-github.png')
    st.write("Nesse projeto desenvolvemos um modelo de aprendizado de máquina que indica a confiabilidade de notícias. O modelo foi treinado com 7200 textos, metade deles com conteúdo falso e a outra metade com textos verdadeiros. O modelo padrão utilizado nessa primeira versão foi o melhor dentre cinco tipos de modelos de aprendizagem que utilizaram um dentre cinco tipos de processamento dos textos.")
    st.write("Caso tenha dúvidas ou problemas na execução da verificação, entre em contato pelo e-mail dos membros da equipe (abaixo) ou sinalize o problema através do [repositório do projeto](https://github.com/atlantico-academy/fake-news-detector).")
    
    #----------
    st.header('Equipe')
    col1, col2 = st.columns([.4, .6])
    for people in team:
        with col1:
            st.image(people['picture'], width=250)
        with col2:
            st.subheader(people['name'])
            st.write(people['bio'])
            st.write(f"Github: [{people['social media']['github'].split('/')[-1]}]({people['social media']['github']})")
            st.write(f"E-mail: [{people['social media']['e-mail']}]({people['social media']['e-mail']})")
            st.text("")
            st.text("")
        