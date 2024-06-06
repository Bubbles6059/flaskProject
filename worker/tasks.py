from celery import Celery, shared_task
import time

def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(
        CELERY=dict(
            broker_url="redis://localhost",
            result_backend="redis://localhost",
            task_ignore_result=True,
        ),
    )
    app.config.from_prefixed_env()
    celery_init_app(app)
    return app

flask_app = create_app()
celery_app = flask_app.extensions["celery"]

@shared_task(ignore_result=False)
def binary_conv_task(numURL):
    print("Started activity")
    num = int(numURL)
    binary_num = num
    # Blank return string
    ret = ""
    # While loop that iterates through the integer to add to the string
    while binary_num >= 1:
        temp = (int)(binary_num % 2)
        ret += str(temp)
        binary_num /= 2
    # Reverses the string that contains the binary as binary goes right to left
    ret = ret[::-1]
    # Inefficient code to scale
    '''
    for i in range(num):
        list.append(testString)
        time.sleep(0.01)
    '''
    time.sleep(4)
    print("Finished activity")
    return ret
