FROM python
COPY . /main
WORKDIR /main
RUN pip install -r requirements.txt
CMD ["python","main.py"]
