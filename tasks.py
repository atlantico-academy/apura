from invoke import task


@task
def init(c):
    c.run("poetry run python -m spacy download pt_core_news_sm")