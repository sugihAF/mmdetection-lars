import json

# Load the JSON file
with open('panoptic_annotations - Copy.json', 'r') as f:
    data = json.load(f)

# Create a mapping of old category IDs to new continuous IDs
old_ids = [1, 3, 5, 11, 12, 13, 14, 15, 16, 17, 19]
new_ids = range(len(old_ids))
id_mapping = dict(zip(old_ids, new_ids))

# Update the category IDs in the JSON data
for annotation in data['annotations']:
    for segment in annotation['segments_info']:
        old_id = segment['category_id']
        segment['category_id'] = id_mapping[old_id]

# Update the IDs in the categories section
for category in data['categories']:
    old_id = category['id']
    category['id'] = id_mapping[old_id]

# Save the updated JSON data back to the file
with open('panoptic_annotations.json', 'w') as f:
    json.dump(data, f)