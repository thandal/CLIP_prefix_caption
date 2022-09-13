import json

"""
Grungy script to convert clipcap-style caption files to coco-caption eval style
I use https://github.com/EricWWWW/image-caption-metrics plus a patch to filter out '\n' and '\r'
"""

#filename = 'data/coco/karpathy_split_annotations/test_caption.json'
#filename = 'data/coco/karpathy_split_annotations/train_caption.json'
filename = 'data/coco/karpathy_split_annotations/val_caption.json'

d = json.load(open(filename))

output = {}
for i in d:
    image_id = i['image_id']
    output.setdefault(image_id, [])
    output[image_id].append(i['caption'])

json.dump(output, open(filename + '_evaluation.json', 'w'))
