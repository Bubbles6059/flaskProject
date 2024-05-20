from flask import Flask, render_template, request

app = Flask(__name__)

#Non-recursive function
@app.route('/binaryconv', methods=['GET'])
def binary_converter():
    num = request.args.get('num')
    #Integer cast as url gives the parameter as a string
    num = int(num)
    #Blank return string
    ret = ""
    #While loop that iterates through the integer to add to the string
    while num >= 1:
        temp = (int)(num % 2)
        ret += str(temp)
        num /= 2
    #Reverses the string that contains the binary as binary goes right to left
    ret = ret[::-1]
    return ret

#Default page
@app.route('/')
def default():
    return "Please enter /binaryconv?num=(your number) in the url above"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

