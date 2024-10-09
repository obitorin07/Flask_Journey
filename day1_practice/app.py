from flask import Flask, request

app = Flask(__name__)

@app.route("/arithmetic")
def arithmetic():
    # Fetch 'x' and 'y' from query parameters
    x = request.args.get("x")
    y = request.args.get("y")

    # Check if both 'x' and 'y' are provided
    if x and y:
        result = int(x) + int(y)
        return f"The sum of x and y is: {result}"
    else:
        return "Please provide both 'x' and 'y' as query parameters."

if __name__ == '__main__':
    app.run(debug=True)
