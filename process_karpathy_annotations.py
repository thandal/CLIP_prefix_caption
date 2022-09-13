import json

""" Processes the original Karpathy splits into clipcap-style caption json files.

Download the karpathy splits from http://cs.stanford.edu/people/karpathy/deepimagesent/caption_datasets.zip
and unzip them into data/coco/karpathy_split_annotations, then run this script.
"""

d = json.load(open('data/coco/karpathy_split_annotations/dataset_coco.json'))

output = {}
SPLIT_COUNTS = {}
for i in d['images']:
  SPLIT_COUNTS.setdefault(i['split'], 0)
  SPLIT_COUNTS[i['split']] += 1
  output.setdefault(i['split'], [])
  for s in i['sentences']:
      output[i['split']].append({
          'image_id': str(i['cocoid']),
          'caption': s['raw'].strip()
          #'id': str(i['cocoid']),  # Doesn't seem to be used for anything
          })

print(f'{SPLIT_COUNTS=}')

for split in output.keys():
  with open(f'{split}_caption.json', 'w') as outfile:
    json.dump(output[split], outfile)

