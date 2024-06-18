from celery import shared_task
import time
from worker import config

flask_app = config.create_app()
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
