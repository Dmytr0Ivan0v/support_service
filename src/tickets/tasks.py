from time import sleep

from config.celery import celery_app


@celery_app.task
def hello_task(name: str):
    sleep(5)
    print(f"Hello from {name}")
