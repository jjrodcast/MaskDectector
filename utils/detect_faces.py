import numpy as np
import cv2
from utils.bounding_box import resizeBoundingBox
from utils.predictor_keras import predict
from utils.predictor_pytorch import model_predict

def detect_faces(img, face_model, confidence=0.5, target_size=(160, 160), enable_generator=False):
    faces = face_model.detect_faces(img)
    img_color = img.copy()
    index = 1
    for face in faces:
        bbox = face['box']
        cnf = face['confidence']
        if cnf >= confidence:
            x,y,w,h = bbox
            img_face_slice = img[y:(y + h),x:(x + w), :]
            img_resize = cv2.resize(img_face_slice, target_size, cv2.INTER_AREA)      
            cv2.rectangle(img_color, (x, y), (x + w, y + h), (0,255,0), 3)
            if (enable_generator):
                cv2.imwrite(f'face_{str(index)}.jpg', img_resize[:,:,::-1])
                index = index + 1
    return img_color


def detect_faces_with_mask(img, face_model, mask_model, classes=['no_mask', 'mask'], confidence=0.5, bbox_percentage=0.1, predictor='keras', target_size=(160,160)):
    if predictor != 'keras' and predictor != 'torch': raise Exception('Predictor must be keras or torch')
    
    faces = face_model.detect_faces(img)
    img_color = img.copy()
    for face in faces:
        bbox = face['box']
        cnf = face['confidence']
        if cnf >= confidence:
            x, y, w, h = resizeBoundingBox((img.shape[1], img.shape[0]), bbox, bbox_percentage)
            img_face_slice = img[y:(y + h),x:(x + w), :]
            img_resize = cv2.resize(img_face_slice, target_size, cv2.INTER_AREA)
            pred,_ = predict(mask_model, classes, np.expand_dims(img_resize[:,:,::-1], axis = 0)) if predictor == 'keras' else model_predict(mask_model, img_resize, classes)
            color = (0,255, 0) if pred == 'mask' else (255,0,0)
            cv2.rectangle(img_color, (x, y), (x + w, y + h), color, 3)
            cv2.putText(img_color, pred.replace("_", " ").capitalize(), (x-2, y-7), cv2.FONT_HERSHEY_SIMPLEX, .9, color, 2)
    return img_color
