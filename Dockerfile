FROM python:3.7

RUN pip install --upgrade pip &&\
    pip install coverage &&\
    pip install pylint

CMD bash