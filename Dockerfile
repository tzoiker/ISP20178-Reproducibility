# Base image
FROM python:2.7

# Author information
MAINTAINER artem.nikitin@skolkovotech.ru

# Set a working directory
WORKDIR example

# Install latex.
RUN apt-get update && apt-get install -y texlive

# Install necessary libraries
RUN pip install numpy scipy matplotlib sklearn

# Add necessary files. Good practice to do it at the end
# in order to avoid reinstallation of dependencies when files change
ADD code ./code
ADD data ./data
ADD latex ./latex
ADD run.sh ./

# Make run.sh executable
RUN chmod +x run.sh

# /example/results contents will be shared with the host
# if -v option used with "docker run" command
VOLUME /example/results

CMD ./run.sh

