FROM lukechannings/deno
RUN apt update 
RUN apt upgrade -y 
RUN apt install python3 git -y
COPY pagic.config.ts .
COPY run.py .
RUN deno install --unstable --allow-read --allow-write --allow-net --allow-run --name=pagic https://deno.land/x/pagic/mod.ts
RUN git clone https://github.com/bageljrkhanofemus/blag.git 
RUN python3 run.py
