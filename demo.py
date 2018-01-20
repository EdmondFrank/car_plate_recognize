from crnnport import *
#crnn
model,converter = crnnSource()
print ("\ninput exit break\n")

im_path = "/home/ef/python/car_plate_recognize/data/results/3.png" 
im = cv2.imread(im_path)
if im is None:
  exit
text_recs = []
with open("/home/ef/python/car_plate_recognize/data/results/res_3.txt","r+") as f:
  text_recs_str = f.read().strip().split(',')
  text_recs = [int(i) for i in text_recs_str]
print(text_recs)
crnnRec(model,converter,im,[text_recs])
cv2.waitKey(0)    





