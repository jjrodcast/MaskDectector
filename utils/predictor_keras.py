def predict(model, classes, image):
    prob = model.predict(image)
    pred = 0 if prob[0] < 0.5 else 1
    return (classes[pred], prob)