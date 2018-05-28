from flask import Flask, request, jsonify


app = Flask(__name__)
app.config["SECRET_KEY"] = "Very very very secret key"

port_number = 8000

@app.route("/", methods=['POST'])
def get_analytics():
    curr_data = request.json['curr_data']
    prev_data  =  request.json['prev_data']
    curr_data_dict = {}
    prev_data_dict = {}
    add = []
    reuse = []
    deaths = []
    reverseDeaths = []
    remove = []
    for item in curr_data:
        curr_data_dict[item['slug']] = item


    for item in prev_data:
        prev_data_dict[item['slug']] = item

    for i in curr_data_dict:
        if i in prev_data_dict:
            curr_alive = curr_data_dict[i]['is_alive']
            pre_Alive =  prev_data_dict[i]['is_alive']
            if pre_Alive == 'true' and not curr_alive == 'true':
                deaths.append(i)
            elif not pre_Alive == 'true' and curr_alive == 'true':
                reverseDeaths.append(i)
            reuse.append(i)
        else:
            add.append(i)
    for i in prev_data_dict:
        if i not in curr_data_dict:
            remove.append(i)

    return jsonify({ 'add': add, 'reuse': reuse, 'deaths':deaths, 'reverseDeaths': reverseDeaths, 'remove':remove})


def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = "Content-Type, x-access-token, Accept"
    header['Access-Control-Allow-Methods'] = "GET, POST, DELETE"
    return response



if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=port_number)
