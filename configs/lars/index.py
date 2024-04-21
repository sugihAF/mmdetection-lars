import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"
from mmdet.datasets import LarsPanopticDataset
from mmengine.config import read_base

with read_base():
    _base_ = '../panoptic_fpn/panoptic-fpn_r50_fpn_1x_coco.py'
#_base_ = '../mask2former/mask2former_r50_8xb2-lsj-50e_coco-panoptic-lars.py'
_delete_=True
# model = dict(
#     roi_head=dict(
#         bbox_head=dict(num_classes=11), mask_head=dict(num_classes=11)))
# Modify dataset related settings
device = 'cuda:0'
data_root = 'D:/Codes/Panoptic Segmentation/mmdetection/configs/lars/dataset/'
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
train_dataloader = dict(
    batch_size=1,
    dataset=dict(
        type='LarsPanopticDataset',
        data_root=data_root,
        metainfo=metainfo,
        ann_file='lars_v1.0.0_annotations/train/panoptic_annotations.json',
        data_prefix=dict(img='D:/Codes/Panoptic Segmentation/mmdetection/configs/lars/dataset/lars_v1.0.0_images/train/images',
                         seg='D:/Codes/Panoptic Segmentation/mmdetection/configs/lars/dataset/lars_v1.0.0_annotations/train/panoptic_masks')))
val_dataloader = dict(
    dataset=dict(
        type='LarsPanopticDataset',
        data_root=data_root,
        metainfo=metainfo,
        ann_file='lars_v1.0.0_annotations/val/panoptic_annotations.json',
        data_prefix=dict(img='D:/Codes/Panoptic Segmentation/mmdetection/configs/lars/dataset/lars_v1.0.0_images/val/images',
                         seg='D:/Codes/Panoptic Segmentation/mmdetection/configs/lars/dataset/lars_v1.0.0_annotations/val/panoptic_masks')))

test_dataloader = val_dataloader
# Modify metric related settings
# val_evaluator = dict(ann_file='D:/Codes/Panoptic Segmentation/mmdetection/configs/lars/dataset/lars_v1.0.0_annotations/val/panoptic_annotations.json')
# test_evaluator = val_evaluator

# load_from = 'https://download.openmmlab.com/mmdetection/v2.0/panoptic_fpn/panoptic_fpn_r50_fpn_1x_coco/panoptic_fpn_r50_fpn_1x_coco_20210821_101153-9668fd13.pth'
# load_from = 'https://download.openmmlab.com/mmdetection/v2.0/mask_rcnn/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco/mask_rcnn_r50_caffe_fpn_mstrain-poly_3x_coco_bbox_mAP-0.408__segm_mAP-0.37_20200504_163245-42aa3d00.pth'
