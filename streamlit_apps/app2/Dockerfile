FROM python:3.8 as builder

RUN mkdir /install

WORKDIR /install

COPY requirements.txt requirements.txt

RUN pip install --force-reinstall  --prefix="/install" -r requirements.txt

FROM python:3.8-slim

EXPOSE 8501

COPY --from=builder /install /usr/local
COPY . .

CMD streamlit run app.py --server.enableCORS=false
