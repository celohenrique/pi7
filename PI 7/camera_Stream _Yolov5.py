from flask import Flask, render_template, Response
import cv2
import torch
import time
from sql_insert import sql_insert_data

app=Flask(__name__,template_folder='templates')

camera = cv2.VideoCapture(0)
model = torch.hub.load('yolov5', 'custom', path='best.pt', source='local')
model.conf=0.3
def gen_frames():
    global wh, wth
    wth = 0
    wh = 0
    a = ''
    b = ''
    c = ''
    d = ''
    # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()
        #time.sleep(2)# read the camera frame
        if not success:
            break
        else:
            frame=cv2.resize(frame,(512,512))
            results = model(frame)
            a1 = (results.pandas().xyxy[0])
            array = a1[['name']].to_numpy()
            array = array.tolist()
            #object = a1.iloc[:, -1].values

            if not array:
                a='Nothing'
                b='Nothing'
            if ['without_helmet'] in array:
                res = array.count(['without_helmet'])
                wth=wth+res
                a='No. of person without helmet: '+ str(res)
                time.sleep(3)

            if ['with_helmet'] in array:
                rec = array.count(['with_helmet'])
                wh = wh + rec
                b = 'No. of person with helmet: ' + str(rec)
                time.sleep(3)
            c = 'No. of Total person without helmet: ' + str(wth)
            d = 'No. of Total person with helmet: ' + str(wh)
            sql_insert_data(wh,wth)
            frame=cv2.putText(frame, a, (20, 50), cv2.FONT_HERSHEY_SIMPLEX,0.6, (255, 0, 0), 2)
            frame = cv2.putText(frame, b, (20, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
            frame = cv2.putText(frame, c, (20, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 255), 2)
            frame = cv2.putText(frame, d, (20, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 100, 100), 2)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
