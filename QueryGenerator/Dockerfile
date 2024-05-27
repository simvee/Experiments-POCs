FROM hub.docker.target.com/continuumio/miniconda3:4.10.3

ARG AUTH_TOKEN=DUMMY_AUTH_TOKEN

ENV OAUTH_TOKEN=$AUTH_TOKEN

RUN apt-get update && \
    apt-get -y install wget vim gcc && \
    apt-get clean;



RUN conda config --set channel_alias https://binrepo.target.com/artifactory/api/conda/anaconda-remote && \
    conda config --add default_channels anaconda && \
    pip config set global.index-url https://binrepo.target.com/artifactory/api/pypi/pypi-remote/simple && \
    pip config set global.extra-index-url https://binrepo.target.com/artifactory/api/pypi/tgt-python/simple


# Customize the below path as per your requirements/folder structure

RUN mkdir /app
WORKDIR /app
RUN mkdir /app/src
RUN mkdir /app/test_cases
COPY /src /app/src
COPY /test_cases /app/test_cases
COPY /data /app/data
ADD /environment.yml .
ADD /entrypoint.sh .

RUN conda env create -f environment.yml && \
    conda clean -ya

RUN echo "conda activate pyenv" >> ~/.bashrc
RUN chmod +x /app/entrypoint.sh


#ENTRYPOINT ["/bin/bash", "--login", "-c", "cd /app && ./entrypoint.sh" ]
ENTRYPOINT ["/app/entrypoint.sh" ]
CMD ["team_name"]
