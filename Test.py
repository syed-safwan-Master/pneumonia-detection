import numpy as np
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input
from keras.utils import load_img, img_to_array



_model = None

def get_model():
    global _model
    if _model is None:
        _model = load_model('our_model.h5')
    return _model

def prediction(path):
    model = get_model()
    img = load_img(path, target_size=(224, 224))
    imagee = img_to_array(img)
    imagee = np.expand_dims(imagee, axis=0)
    img_data = preprocess_input(imagee)
    pred = model.predict(img_data)
    if pred[0][0] > pred[0][1]:
        return "1001"
    else:
        print('Person is affected with Pneumonia.')
        return "positive"


