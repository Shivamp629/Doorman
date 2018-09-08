import numpy as np
import cv2
from keras.preprocessing import image
from keras.models import model_from_json

face_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_alt.xml')
emotion_model = model_from_json(open("models/facial_expression_model_structure.json", "r").read())
emotion_model.load_weights('models/facial_expression_model_weights.h5')
emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
# name_model = load_model('name_model.h5')

cap = cv2.VideoCapture(0)

while(True):
	# take frame, rescale, detect face
	ret, img = cap.read()
	img = cv2.resize(img, (640, 360))
	img = img[0:308,:]
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray, 1.3, 5)

	for (x,y,w,h) in faces:
		if w > 100: #trick: ignore small faces
			cv2.rectangle(img,(x,y),(x+w,y+h),(64,64,64),2) #highlight detected face
			detected_face = img[int(y):int(y+h), int(x):int(x+w)] #crop detected face
			detected_face = cv2.cvtColor(detected_face, cv2.COLOR_BGR2GRAY) #transform to gray scale
			detected_face = cv2.resize(detected_face, (48, 48)) #resize to 48x48

			face_pixels = image.img_to_array(detected_face)
			face_pixels = np.expand_dims(face_pixels, axis = 0)
			face_pixels /= 255 #pixels are in scale of [0, 255]. normalize all pixels in scale of [0, 1]

			emotion_preds = emotion_model.predict(face_pixels) #store probabilities of 7 expressions
			# name_pred = name_model.predict(face_pixels)

			#background of expression list
			overlay = img.copy()
			opacity = 0.4
			cv2.rectangle(img,(x+w+10,y-25),(x+w+150,y+115),(64,64,64),cv2.FILLED)
			cv2.addWeighted(overlay, opacity, img, 1 - opacity, 0, img)

			#connect face and expressions
			#TODO Name on top of emotions
			#cv2.line(img,(int((x+x+w)/2),y+15),(x+w,y-20),(255,255,255),1)
			cv2.line(img,(int((x+x+w)/2),y+15),(x+w,y-20),(255,255,255),1)
			cv2.line(img,(x+w,y-20),(x+w+10,y-20),(255,255,255),1)

			emotionArr = []
			for i in range(len(emotion_preds[0])):
				emotionArr.append((emotions[i], round(emotion_preds[0][i]*100, 2)))
				emotion = "%s %s%s" % (emotions[i], round(emotion_preds[0][i]*100, 2), '%')
				color = (255,255,255)
				cv2.putText(img, emotion, (int(x+w+15), int(y-12+i*20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
			emotion = max(emotionArr, key=lambda item:item[1])[0]
			print(emotion)

	cv2.imshow('img',img)

	if cv2.waitKey(1) & 0xFF == ord('q'): #press q to quit
		break

cap.release()
cv2.destroyAllWindows()
