from flask import Flask, render_template, request, jsonify
from flask_cors import cross_origin, CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods = ['GET'])
@cross_origin()
def homepage():
    return render_template("index.html")

@app.route("/hello", methods = ['GET'])
@cross_origin()
def hello():
    try:
        language = request.args.get('language').lower()
        if language == "hindi":
            response = {
              "message": {
                "ID": "A123456789",
                "msgText": "Namastey sansar"
              }
            }
            return jsonify(response)

        if language == "english":
            response = {
                "message": {
                    "ID": "A123456790",
                    "msgText": "Hello world"
                }
            }
            return jsonify(response)

        if language == "french":
            response = {
                "message": {
                    "ID": "A123456791",
                    "msgText": "Bonjour le monde"
                }
            }
            return jsonify(response)
        else:
            response = {
                "message": {
                    "msgText": "The requested language is not supported"
                }
            }
            return jsonify(response), 400
    except:
        return jsonify("Internal server error"), 400

if __name__ == "__main__":
    app.run(debug="true")
