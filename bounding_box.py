def resizeBoundingBox(image_dimens, bbox, percentage = 0.05):
  if percentage < .01 or percentage > 1. : raise Exception("Percentage not allowed. Range [0.01 - 1]")
  x, y, w, h = bbox
  image_width, image_height = image_dimens
  total_width,total_height = (x+w, y+h)
  
  paddingWidth = int(total_width * percentage)
  paddingHeight = int(total_height * percentage)
  
  new_x = 0 if(x-paddingWidth < 0) else x - paddingWidth
  new_y = 0 if(y-paddingHeight < 0) else y - paddingHeight
  
  new_w = new_x + w + (paddingWidth * 2)
  new_h = new_y + h + (paddingHeight * 2)

  new_w = image_width if(new_w > image_width) else w + (paddingWidth * 2)
  new_h = image_height if(new_h > image_height) else h + (paddingHeight * 2)

  return new_x, new_y, new_w, new_h