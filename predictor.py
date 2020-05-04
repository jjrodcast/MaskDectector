def predict(model, classes, image):
    pred = model.predict(image)
    return classes[int(pred[0])]