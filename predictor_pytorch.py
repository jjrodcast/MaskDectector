## Import needed packages
import torch
import numpy as np
from torch.autograd import Variable
from torchvision import transforms
from PIL import Image

def model_predict(model, image, classes = None):

    image = Image.fromarray(image) # eliminar en caso el input sea del tipo PIL.Image
    
    data_transforms = transforms.Compose([
    transforms.Resize(160),
    transforms.CenterCrop(160), 
    transforms.ToTensor(),
    transforms.Normalize([0.5737, 0.4802, 0.4410],[0.2369, 0.2243, 0.2235])])

    use_gpu = torch.cuda.is_available()
    device = torch.device("cuda:0" if use_gpu else "cpu")   

    model.eval() 

    imgblob = data_transforms(image)
    imgblob.unsqueeze_(dim=0)
    imgblob = Variable(imgblob)
    torch.no_grad()

    imgblob = imgblob.to(device)

    output = model(imgblob)
    prob, pred = torch.max(output, 1)

    if classes is None:
        return(int(pred),float(prob))
    else:
        return(classes[int(pred)],float(prob))

