FROM python:3.10

WORKDIR /app
COPY . /app

# install graphviz
RUN apt-get update && apt-get install -y graphviz

# install python libraries
RUN pip install --no-cache-dir graphviz networkx lxml z3-solver numpy

ENTRYPOINT ["python3", "driver.py"]