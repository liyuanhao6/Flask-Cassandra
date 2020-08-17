from datetime import datetime

from flask import Flask, abort, jsonify, request

import cqlshOperate
import imageOperate

app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
class_names = [
    'T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 'Sandal', 'Shirt',
    'Sneaker', 'Bag', 'Ankle boot'
]
cqlshOperate.createKeySpace()


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def list_image(task_id):
    rows = cqlshOperate.getData()
    row = rows[task_id]
    task = {'id': 1}
    task['time'] = row[0]
    task['image_name'] = row[1]
    task['class_name'] = row[2]
    return jsonify(task), 200


@app.route('/api/tasks', methods=['GET'])
def list_all():
    tasks = []
    rows = cqlshOperate.getData()
    id = 1
    for row in rows:
        task = {'id': id}
        task['time'] = row[0]
        task['image_name'] = row[1]
        task['class_name'] = row[2]
        tasks.append(task)
        id += 1
    return jsonify(tasks), 200


@app.route('/api/tasks/upload', methods=['POST'])
def upload_image():
    img_bin = request.files['image']
    image_name = request.files['image'].filename
    img_bin.save(image_name)
    if image_name:
        image = imageOperate.process(image_name)
        label = imageOperate.predict(image)
        now = datetime.now()
        cqlshOperate.insertData(image_time=str(now),
                                image_name=image_name,
                                image_label=class_names[label])
        return class_names[label]
    abort(404)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)


'''

* Trying 127.0.0.1...
* TCP_NODELAY set
* Connected to 127.0.0.1 (127.0.0.1) port 8080 (#0)
> POST /api/tasks/upload HTTP/1.1
> Host: 127.0.0.1:8080
> User-Agent: curl/7.64.1
> Accept: */*
> Content-Length: 7334
> Content-Type: multipart/form-data; boundary=------------------------934af8e5dad05416
> Expect: 100-continue
>
< HTTP/1.1 100 Continue
* We are completely uploaded and fine
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Content-Type: text/html; charset=utf-8
< Content-Length: 3
< Server: Werkzeug/1.0.0 Python/3.7.1
< Date: Mon, 17 Aug 2020 07:33:09 GMT
<
* Closing connection 0
Bag

'''