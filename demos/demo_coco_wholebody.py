from xtcocotools.coco import COCO
from xtcocotools.cocoeval import COCOeval
import numpy as np

gt_file = '../annotations/example_wholebody_val.json'
preds = '../annotations/example_wholebody_preds.json'

sigmas_body = [0.026, 0.025, 0.025, 0.035, 0.035, 0.079, 0.079, 0.072, 0.072, 0.062, 0.062, 0.107, 0.107, 0.087,
               0.087, 0.089, 0.089]
sigmas_foot = [0.068, 0.066, 0.066, 0.092, 0.094, 0.094]
sigmas_face = [0.042, 0.043, 0.044, 0.043, 0.040, 0.035, 0.031, 0.025, 0.020, 0.023, 0.029, 0.032, 0.037, 0.038, 0.043,
               0.041, 0.045, 0.013, 0.012, 0.011, 0.011, 0.012, 0.012, 0.011, 0.011, 0.013, 0.015, 0.009, 0.007, 0.007,
               0.007, 0.012, 0.009, 0.008, 0.016, 0.010, 0.017, 0.011, 0.009, 0.011, 0.009, 0.007, 0.013, 0.008, 0.011,
               0.012, 0.010, 0.034, 0.008, 0.008, 0.009, 0.008, 0.008, 0.007, 0.010, 0.008, 0.009, 0.009, 0.009, 0.007,
               0.007, 0.008, 0.011, 0.008, 0.008, 0.008, 0.01, 0.008]
sigmas_lefthand = [0.029, 0.022, 0.035, 0.037, 0.047, 0.026, 0.025, 0.024, 0.035, 0.018, 0.024, 0.022, 0.026, 0.017,
               0.021, 0.021, 0.032, 0.02, 0.019, 0.022, 0.031]
sigmas_righthand = [0.029, 0.022, 0.035, 0.037, 0.047, 0.026, 0.025, 0.024, 0.035, 0.018, 0.024, 0.022, 0.026, 0.017,
               0.021, 0.021, 0.032, 0.02, 0.019, 0.022, 0.031]

sigmas_wholebody = sigmas_body + sigmas_foot + sigmas_face + sigmas_lefthand + sigmas_righthand

cocoGt = COCO(gt_file)
cocoDt = cocoGt.loadRes(preds)
cocoEval = COCOeval(cocoGt, cocoDt, 'keypoints_body', np.array(sigmas_body), use_area=True)
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()

cocoGt = COCO(gt_file)
cocoDt = cocoGt.loadRes(preds)
cocoEval = COCOeval(cocoGt, cocoDt, 'keypoints_foot', np.array(sigmas_foot), use_area=True)
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()

cocoGt = COCO(gt_file)
cocoDt = cocoGt.loadRes(preds)
cocoEval = COCOeval(cocoGt, cocoDt, 'keypoints_face', np.array(sigmas_face), use_area=True)
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()

cocoGt = COCO(gt_file)
cocoDt = cocoGt.loadRes(preds)
cocoEval = COCOeval(cocoGt, cocoDt, 'keypoints_lefthand', np.array(sigmas_lefthand), use_area=True)
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()

cocoGt = COCO(gt_file)
cocoDt = cocoGt.loadRes(preds)
cocoEval = COCOeval(cocoGt, cocoDt, 'keypoints_righthand', np.array(sigmas_righthand), use_area=True)
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()

cocoGt = COCO(gt_file)
cocoDt = cocoGt.loadRes(preds)
cocoEval = COCOeval(cocoGt, cocoDt, 'keypoints_wholebody', np.array(sigmas_wholebody), use_area=True)
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()
