FROM python:3.13.2

RUN mkdir -p /app
RUN mkdir -p /volume

WORKDIR /app

COPY Code/Python/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY Code/Python/send_meshtastic_messages.py .

CMD ["python", "send_meshtastic_messages.py"]