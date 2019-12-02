import os
import shutil
import random
'''
    指定idx，从label中生成gt和label
'''

label_all_dir = '/hdd/you/dataset/KITTI/training/label_2'
idx_dir = '/hdd/you/rgb-det/data/image_sets'
gt_dir = '/hdd/you/dataset/KITTI/training/test_eval/gt'
det_dir = '/hdd/you/dataset/KITTI/training/test_eval/det/data'
plot_dir = '/hdd/you/dataset/KITTI/training/test_eval/det/plot'

idx_type = ['train.txt','val.txt','trainval.txt']
white_list = ['Car']
score_space = {'Min':0.8,'Max':1}
n_sample = 49

if os.path.exists(gt_dir):
    shutil.rmtree(gt_dir)
os.makedirs(gt_dir)
if os.path.exists(det_dir):
    shutil.rmtree(det_dir)
os.makedirs(det_dir)
if os.path.exists(plot_dir):
    shutil.rmtree(plot_dir)

idx_path = os.path.join(idx_dir, idx_type[1])
with open(idx_path, 'r') as idx_f:
    for i, idx in enumerate(idx_f):
        idx = idx.rstrip()
        label_path = os.path.join(label_all_dir,idx+'.txt')
        gt_path = os.path.join(gt_dir,idx+'.txt')
        det_path = os.path.join(det_dir,idx+'.txt')
        # print(label_path, gt_path, det_path,sep='\n')
        
        shutil.copyfile(label_path,gt_path)
        label_f = open(label_path, 'r')
        labels = label_f.readlines()
        label_f.close()

        det_f = open(det_path,'w')
        for lab in labels:
            if lab.split()[0] not in white_list:
                continue
            score = random.uniform(score_space['Min'],score_space['Max'])
            lab = lab.rstrip() + ' ' + str(score)+'\n'
            det_f.write(lab)
        det_f.close()

        if i == n_sample-1:
            break
        
        

