from fastapi import FastAPI
import random

app = FastAPI()

# Fibonacci API
@app.get("/test/fibo")
def fibonacci():
    fib_series = [55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765]
    return {"numbers": fib_series}

# Even Numbers API
@app.get("/test/even")
def even_numbers():
    even_nums = list(range(8, 58, 2))  # Even numbers from 8 to 56
    return {"numbers": even_nums}

# Random Numbers API
@app.get("/test/rand")
def random_numbers():
    rand_nums = random.sample(range(1, 31), 10)  # 10 random numbers from 1 to 30
    return {"numbers": rand_nums}

# Root Endpoint
@app.get("/")
def home():
    return {"message": "Welcome to the Numbers API"}
