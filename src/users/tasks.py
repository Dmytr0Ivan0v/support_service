from config.celery import celery_app


@celery_app.task
def greeting(user_name: str):
    print(f"Welcome to 'Support servise', {user_name}!")
