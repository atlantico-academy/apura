FROM python:3.8-slim

RUN mkdir /app
COPY . /app
WORKDIR /app

RUN pip install --upgrade pip && pip install -r requirements.txt
RUN python -m spacy download pt_core_news_sm
RUN python -m nltk.downloader -d /app/nltk_data all

CMD streamlit run app.py --server.port $PORT