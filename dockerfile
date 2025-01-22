#for image
FROM python:3.9

#maintainer
LABEL key="Anjali Gupta"

#directory
WORKDIR /main.py

#requirements
CMD [ "uvicorn main:app --reload"]

EXPOSE 8000

