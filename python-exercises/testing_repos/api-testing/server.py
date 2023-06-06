from flask import Flask, jsonify, request
from flask_cors import CORS
from werkzeug import exceptions

app = Flask(__name__)
dogs = []

CORS(app)

# @app.route('/api')
# def api_route():
#     return jsonify({'message': 'Expected output'})

@app.route('/api/dogs', methods=['GET', 'POST'])
def dogs_handler():
    if request.method == 'POST':
        dog = request.get_json()
        dogs.append(dog)
        dog['id'] = len(dogs)
        resp = {'dog': dog}
        code = 201
    else:
        resp = {'dogs': dogs}
        code = 200
    return jsonify(resp), code

@app.route('/api/dogs/<int:dog_id>')
def dog_handler(dog_id):
    dog = next(dog for dog in dogs if dog['id'] == dog_id)
    return jsonify({'dog': dog}), 200


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

if __name__ == '__main__': # pragma: no cover
    app.run(debug=True)


