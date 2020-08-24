from xtcocotools.coco import COCO
from xtcocotools.cocoeval import COCOeval
import numpy as np

gt_file = '../annotations/example_coco_val.json'
preds = '../annotations/example_coco_preds.json'

sigmas = np.array(
                [.26, .25, .25, .35, .35, .79, .79, .72, .72, .62,.62, 1.07, 1.07, .87, .87, .89, .89])/10.0

cocoGt = COCO(gt_file)
cocoDt = cocoGt.loadRes(preds)
cocoEval = COCOeval(cocoGt, cocoDt, 'keypoints', sigmas, use_area=True)
cocoEval.evaluate()
cocoEval.accumulate()
cocoEval.summarize()
