from flask import Flask
import time

app = Flask(__name__)

@app.route("/")
def hello():
    n = 37
    start_recursive = time.time()
    r_result = recursive_fibonacci(n)
    end_recursive = time.time()

    start_dynamic = time.time()
    d_result = dynamic_fibonacci(n)
    end_dynamic = time.time()

    time_r = (end_recursive - start_recursive)
    time_d = (end_dynamic - start_dynamic)  
    
    html = f"""
        <!HTML>
        <head>
            <title>Fibonacci comparison</title>
        </head>
        <body>
            <p>Time it took to calculate {n}th Fibonacci number using recursion:<b> {round(time_r, 3)} seconds.</b></p>
            <br/>
            <p>Time it took to calculate {n}th Fibonacci number using dynamic proramming:<b> {round(time_d, 7)} seconds.</b></p>

            <footer>
                <p><a href="https://github.com/ConstantKrieg/docker-flask-demo">Project GitHub</a></p>
            </footer>
        </body>
            """

    return html



def dynamic_fibonacci(n):
    l = []
    l.append(0) 
    l.append(1)
    l.append(1)

    for i in range(3, n+1):
        l.append(l[i-1] + l[i-2])

    return l[n]        


def recursive_fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return recursive_fibonacci(n-1)+recursive_fibonacci(n-2)


app.run(host='0.0.0.0')