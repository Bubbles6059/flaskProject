from flask import request, jsonify, redirect
import redis
from celery.result import AsyncResult
from worker.tasks import binary_conv_task, flask_app

redisInstance = redis.Redis()

#testString = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
list = []

#Non-recursive function
@flask_app.route('/binaryconv', methods = ['GET','POST'])
def binary_converter() -> dict[str, object]:
    '''
    numURL = request.args.get('num')
    #Integer cast as url gives the parameter as a string
    num = int(numURL)
    binary_num = num
    #Blank return string
    ret = ""
    #While loop that iterates through the integer to add to the string
    while binary_num >= 1:
        temp = (int)(binary_num % 2)
        ret += str(temp)
        binary_num /= 2
    #Reverses the string that contains the binary as binary goes right to left
    ret = ret[::-1]
    #Inefficient code to scale
    for i in range(num):
        list.append(testString)
        time.sleep(0.01)
    return ret
    '''

    if(request.method == 'GET'):
        numURL = request.args.get('num')
        print(numURL)
        result = binary_conv_task.delay(numURL)
        return redirect('/get_result?result_id=' + str(result.id))

@flask_app.route('/get_result', methods = ['GET'])
def retrieve_result() -> dict[str, object]:
    result_id = request.args.get('result_id')
    result = AsyncResult(result_id)  # -Line 4
    if result.ready():  # -Line 5
        # Task has completed
        if result.successful():  # -Line 6

            return {
                "ready": result.ready(),
                "successful": result.successful(),
                "value": result.result,  # -Line 7
            }
        else:
            # Task completed with an error
            return jsonify({'status': 'ERROR', 'error_message': str(result.result)})
    else:
        # Task is still pending
        return jsonify({'status': 'Running'})



#Default page
@flask_app.route('/')
def default():
    return "Please enter /binaryconv?num=(your number) in the url above"

@flask_app.route('/health')
def health():
    result = jsonify(success=True)
    return result

if __name__ == '__main__':
    flask_app.run(debug=True, host='0.0.0.0')

