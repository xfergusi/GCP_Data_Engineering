# from ghcr.io/dbt-labs/dbt-bigquery:1.4.4

# workdir /usr/app

# copy . .
# copy profiles /usr/app/profiles
# copy profiles/profiles.yml /root/.dbt/profiles.yml


# # Set the environment variable for profiles directory
# ENV DBT_PROFILES_DIR=/root/.dbt
# RUN pip install --upgrade pip
# RUN python -m pip install dbt-core dbt-bigquery

# RUN ls

# RUN dbt deps


# Use the official dbt Docker image as the base image
FROM ghcr.io/dbt-labs/dbt-bigquery:1.4.4


# Set the working directory inside the container
WORKDIR /usr/app

# Copy the entire dbt project into the container
COPY . .
# Copy the profiles.yml file
# COPY profiles/profiles.yml /root/.dbt/profiles.yml
COPY .dbt/profiles.yml /root/.dbt/profiles.yml


# Set the environment variable for profiles directory
ENV DBT_PROFILES_DIR=/root/.dbt

RUN dbt --version
RUN dbt deps --profiles-dir ~/.dbt

# ENTRYPOINT ["sh", "-c", "dbt seed && dbt run"]
# ENTRYPOINT ["dbt", "seed"]
ENTRYPOINT ["dbt", "run"]

# docker run --rm \
#  -v ~/.config/gcloud/application_default_credentials.json:/root/.config/gcloud/application_default_credentials.json \
# learngcpdbt
# docker build -t australia-southeast1-docker.pkg.dev/ferg-sandbox-gcp/learn-gcp/learngcpdbt:latest .
# docker push australia-southeast1-docker.pkg.dev/ferg-sandbox-gcp/learn-gcp/learngcpdbt:latest