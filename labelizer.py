from scipy.io import loadmat
from PIL import Image

x = loadmat('devkit/cars_test_annos.mat')
y = loadmat('devkit/cars_meta.mat')

print(x['annotations'][0][0])
print(y)

# for i in range(len(x['annotations'][0])):
#   x1, x2, y1, y2, fname = x['annotations'][0][i]
#   x1, x2, y1, y2, fname = x1[0][0], y1[0][0], x2[0][0], y2[0][0], fname[0]

#   img = Image.open('test/' + fname)
#   cropped = img.crop((x1, y1, x2, y2))
#   cropped.save('new/' + fname)
