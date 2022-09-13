import json

"""
I was confused why clipcap's train_caption.json doesn't seem to match up with the original Karpathy split.
It is actually made of up of train + restval... but even then its missing a few?
"""

# rmokady train split
r = json.load(open("data/coco/annotations/train_caption.json"))
# karpathy train split
k = json.load(open("data/coco/karpathy_split_annotations/train_caption.json"))

print(f'{len(r)=}')
print(f'{len(k)=}')
print(f'{len(r) - len(k)=}')
print(f'{(len(r) - len(k))/5=}')

# full karpathy split data
d = json.load(open('data/coco/karpathy_split_annotations/dataset_coco.json'))

IMAGE_TO_SPLIT = {}
for i in d['images']:
  IMAGE_TO_SPLIT[str(i['cocoid'])] = i['split']

# Look at the composition of the rmokady train split
SPLIT_COUNTS = {}
for i in r:
  split = IMAGE_TO_SPLIT[i['image_id']]
  SPLIT_COUNTS[split] = SPLIT_COUNTS.get(split, 0) + 1

print(f'{SPLIT_COUNTS=}')
