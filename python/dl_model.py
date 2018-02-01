import os

import anago
from anago.utils import download
from anago.reader import load_data_and_labels

dir_path = 'test_dir'
url = 'https://storage.googleapis.com/chakki/datasets/public/models.zip'
DATA_ROOT = os.path.join(os.path.dirname(__file__), '/home/gregoire.portier/NER/test.txt')

test_path = os.path.join(DATA_ROOT, 'test.txt')
x_test, y_test = load_data_and_labels(test_path)
print("loead")

print("start dl")
download(url, dir_path)
print("end dl")

model = anago.Sequence.load(dir_path)
print("model load")
model.eval(x_test, y_test)
