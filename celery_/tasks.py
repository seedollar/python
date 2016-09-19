from celery import Celery
import time

app = Celery('tasks', backend='redis://localhost', broker='amqp://guest@localhost//')

@app.task
def add(x, y):
    time.sleep(20)
    return x + y