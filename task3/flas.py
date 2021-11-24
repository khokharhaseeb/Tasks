from flask import Flask,render_template,Response
import came
import cv2
import os

app = Flask(__name__)
def cam():  
    global camera 
    camera = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc('X','V','I','D')
    cap_rec = cv2.VideoWriter('id.avi',fourcc,40.0,(640,480))
    while True:
        ret,frame=camera.read()
        if not ret:
            break
        cap_rec.write(frame)
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
      
@app.route("/")
def front():
    release_camera()
    return render_template('index.html')

camera=cv2.VideoCapture()
def use_camera():
    global camera
    camera=cv2.VideoCapture(0)
    
def release_camera():
    if camera.isOpened():
        camera.release()

@app.route("/camera")
def camer():
    release_camera()
    return render_template("data.html",dic = came.proces())
    
@app.route('/video_feed')
def video_feed():
    return Response(cam(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__=='__main__':
    app.run(debug=True)
