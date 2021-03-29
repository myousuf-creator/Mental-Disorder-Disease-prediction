import flask
from flask import jsonify,request
import json
from predict import make_prediction
# person = '{"status":"False"}'
# person_dict = json.loads(person)

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/health', methods=['GET'])
def health():
    message = '{"status":"True"}'
    JSON_message = json.loads(message)
    return JSON_message


@app.route('/v1/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Step 1: Extract POST data from request body as JSON
        json_data = request.get_json()
        # _logger.debug(f'Inputs: {json_data}')

        # Step 2: Validate the input using marshmallow schema
        # input_data, errors = validate_inputs(input_data=json_data)
        #print(input_data)

        # Step 3: Model prediction
        result = make_prediction(input_data=json_data)
        # _logger.debug(f'Outputs: {result}')

        # Step 4: Convert numpy ndarray to list
        predictions = result.get('predictions')
        # version = result.get('version')
        # patient_id = result.get('patient_id')

        # Step 5: Return the response as JSON
        return jsonify({'predictions': predictions,
                        # 'version': version,
                        # 'patient_id':patient_id
                        })
                        # 'errors': errors

app.run()