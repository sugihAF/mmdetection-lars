from mmdet.apis import init_detector, inference_detector, show_result_ins
import mmcv

# Specify the path to model config and checkpoint file
config_file = 'configs/panoptic_fpn/panoptic-fpn_r50_fpn_1x_coco.py'
checkpoint_file = 'checkpoints/panoptic-fpn_r50_fpn_1x_coco_20200928pth-6822e9c7.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

# test a single image
img = 'configs/lars/davimar_seq_01_00017.jpg'  # replace with the path to your image
result = inference_detector(model, img)

# visualize the results in a new window
show_result_ins(img, result, model.CLASSES, score_thr=0.3, out_file="output.png")