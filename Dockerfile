# app/Dockerfile

FROM python:3.12


WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip3 install -r requirements.txt

EXPOSE 80


# here I'll set the default value for the file name, can be overridden during container startup
ENV STREAMLIT_APP_FILE=frontend.py

# Use the CMD command with shell form to interpret environment variables
# CMD streamlit run --server.port=8502 --server.address=0.0.0.0 $STREAMLIT_APP_FILE
CMD streamlit run --server.port=80 --server.address=0.0.0.0 $STREAMLIT_APP_FILE


# docker volume create data_storage  
# docker volume create wiki 

# docker run -v data_storage:/app/data_storage -v wiki:/app/wiki -e STREAMLIT_APP_FILE=admin.py -it -d -p 80:8502 --restart always --name c-gen-ai tommal/gen-ai 

# docker run --rm -v /Users/tomasmali/Desktop/LangGraph:/app -it  -p 8222:80  --name c-agent tommal/agent


