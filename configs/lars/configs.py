
# the new config inherits the base configs to highlight the necessary modification
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

_base_ = '../panoptic_fpn/panoptic-fpn_r50_fpn_1x_coco.py'
# 1. dataset settings
dataset_type = 'CocoPanopticDataset'
data_root = 'D:/Codes/mmdetection/configs/lars/dataset/'
metainfo = {
    'classes': (
        'Static Obstacle', 'Water', 'Sky', 'Boat/ship', 'Row boats', 
        'Paddle board', 'Buoy', 'Swimmer', 'Animal', 'Float', 'Other'
    ),
    'palette': [
        (255, 212, 25), (70, 245, 255), (170, 0, 255), (255, 39, 43), 
        (255, 39, 43), (255, 39, 43), (255, 39, 43), (255, 39, 43), 
        (255, 39, 43), (255, 39, 43), (255, 39, 43)
    ]
}
classes= (
        'Static Obstacle', 'Water', 'Sky', 'Boat/ship', 'Row boats', 
        'Paddle board', 'Buoy', 'Swimmer', 'Animal', 'Float', 'Other'
    )
data = dict(
    samples_per_gpu=2,
    workers_per_gpu=2,
    train=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file=data_root +'lars_v1.0.0_annotations/train/panoptic_annotations.json',
        img_prefix=data_root + 'lars_v1.0.0_images/train/images',
        seg_prefix = data_root + 'lars_v1.0.0_annotations/train/panoptic_masks'),
    val=dict(
        type=dataset_type,
        # explicitly add your class names to the field `classes`
        classes=classes,
        ann_file=data_root +'lars_v1.0.0_annotations/val/panoptic_annotations.json',
        img_prefix=data_root +'lars_v1.0.0_images/val/images',
        seg_prefix = data_root + 'lars_v1.0.0_annotations/val/panoptic_masks'))

train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        type='CocoPanopticDataset',
        data_root=data_root,
        metainfo=metainfo,
        ann_file='lars_v1.0.0_annotations/train/panoptic_annotations.json',
        data_prefix=dict(img=data_root + 'lars_v1.0.0_images/train/images',
                         seg=data_root + 'lars_v1.0.0_annotations/train/panoptic_masks')))

val_dataloader = dict(
    dataset=dict(
        type='CocoPanopticDataset',
        data_root=data_root,
        metainfo=metainfo,
        ann_file='lars_v1.0.0_annotations/val/panoptic_annotations.json',
        data_prefix=dict(img=data_root + 'lars_v1.0.0_images/val/images',
                         seg=data_root + 'lars_v1.0.0_annotations/val/panoptic_masks')))

test_dataloader = val_dataloader
# # 2. model settings

# # explicitly over-write all the `num_classes` field from default 80 to 5.
# model = dict(
#     roi_head=dict(
#         bbox_head=[
#             dict(
#                 type='Shared2FCBBoxHead',
#                 # explicitly over-write all the `num_classes` field from default 80 to 5.
#                 num_classes=5),
#             dict(
#                 type='Shared2FCBBoxHead',
#                 # explicitly over-write all the `num_classes` field from default 80 to 5.
#                 num_classes=5),
#             dict(
#                 type='Shared2FCBBoxHead',
#                 # explicitly over-write all the `num_classes` field from default 80 to 5.
#                 num_classes=5)],
#     # explicitly over-write all the `num_classes` field from default 80 to 5.
#     mask_head=dict(num_classes=5)))