from invoke import task


@task
def init(c):
    c.run("python -m spacy download pt_core_news_sm")