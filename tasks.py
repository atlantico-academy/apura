from invoke import task
import gdown

@task
def init(c):
    c.run("poetry run python -m spacy download pt_core_news_sm")
    
    share_id = '1ACln8hSyr8Ec852O5pbItHLAvvdGjHcj'
    gdown.download(url='https://drive.google.com/uc?id='+share_id, 
                   output='./data/processed/textos_pre-processados.csv', 
                   quiet=False)