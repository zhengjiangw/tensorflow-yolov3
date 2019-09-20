import json

from core.config import cfg
from core.dataset import Dataset


class PersonDataset(Dataset):
  """
  make perple dataset here
  """
  
  def load_annotations(self, dataset_type):
    
    self.generate_txt_from_json()
    return super.load_annotations(dataset_type)
  
  
  def generate_txt_from_json(self):
    with open(cfg.TRAIN.ANNOT_PATH, "r") as f:
      doc = json.loads(f.read())
  
    lines = []
    annotations = doc['annotations']
    for img_info in annotations:
      anno_type = img_info['type']
      if anno_type != 'bbox':
        continue
      img_data = ""
      img_path = img_info['name'].split("/")[2]
      img_annos = img_info['annotation']
      img_data = img_data + img_path + " "
      for img_anno in img_annos:
        x = img_anno['x']
        y = img_anno['y']
        w = img_anno['w']
        h = img_anno['h']
        xmin = x - w // 2
        ymin = y - h // 2
        xmax = x + w // 2
        ymax = y + h // 2
        img_data = img_data + "%d,%d,%d,%d,%d " % (xmin, ymin, xmax, ymax, 1)
      img_data = img_data.strip()
      img_data += "\n"
      lines.append(img_data)
    
    with open("../data/dataset/people_train.txt", "w") as f:
      f.writelines(lines)


if __name__ == "__main__":
  PersonDataset(None)
