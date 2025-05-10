from flask import Flask, render_template_string

app = Flask(__name__)

html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>Sayali's Web Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #a1c4fd, #c2e9fb);
            text-align: center;
            padding: 50px;
        }
        .card {
            background-color: white;
            padding: 30px;
            margin: auto;
            width: 50%;
            border-radius: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
        }
        p {
            font-size: 18px;
            color: #666;
        }
        a.button {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 25px;
            background-color: #4CAF50;
            color: white;
            text-decoration: none;
            border-radius: 8px;
        }
        a.button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="card">
        <h1>Welcome to Sayali's Web App 🌟</h1>
        <p>This is a simple and beautiful web page built using Python and Flask.</p>
        <a href="https://github.com" class="button">Visit GitHub</a>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(html_template)

if __name__ == '__main__':
    app.run(debug=True)
