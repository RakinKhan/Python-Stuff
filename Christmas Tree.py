#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
def christmas_tree():
  for item in picture:
    item_row = ''
    for indiv_item in item:
      if indiv_item == False:
        item_row = item_row + ' '
      else:
        item_row = item_row + '*'

    print(item_row)
christmas_tree()

