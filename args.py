import argparse


parser = argparse.ArgumentParser()

# Data input settings
parser.add_argument('--cfgs_file', default='cfgs/anet.yml', type=str, help='dataset specific settings. anet | yc2')
parser.add_argument('--dataset', default='', type=str, help='which dataset to use. two options: anet | yc2')
parser.add_argument('--dataset_file', default='', type=str)
parser.add_argument('--feature_root', default='', type=str, help='the feature root')
parser.add_argument('--dur_file', default='', type=str)
parser.add_argument('--val_data_folder', default='validation', help='validation data folder')
parser.add_argument('--densecap_eval_file', default='/z/subsystem/densevid_eval/evaluate.py')
parser.add_argument('--densecap_references', default='', type=str)
parser.add_argument('--start_from', default='', help='path to a model checkpoint to initialize model weights from. Empty = dont')
parser.add_argument('--max_sentence_len', default=20, type=int)
parser.add_argument('--num_workers', default=2, type=int)

# Model settings: General
parser.add_argument('--d_model', default=1024, type=int, help='size of the rnn in number of hidden nodes in each layer')
parser.add_argument('--d_hidden', default=2048, type=int)
parser.add_argument('--n_heads', default=8, type=int)
parser.add_argument('--in_emb_dropout', default=0.1, type=float)
parser.add_argument('--attn_dropout', default=0.2, type=float)
parser.add_argument('--vis_emb_dropout', default=0.1, type=float)
parser.add_argument('--cap_dropout', default=0.2, type=float)
parser.add_argument('--image_feat_size', default=3072, type=int, help='the encoding size of the image feature')
parser.add_argument('--n_layers', default=2, type=int, help='number of layers in the sequence model')

# Model settings: Proposal and mask
parser.add_argument('--slide_window_size', default=480, type=int, help='the (temporal) size of the sliding window')
parser.add_argument('--slide_window_stride', default=20, type=int, help='the step size of the sliding window')
parser.add_argument('--sampling_sec', default=0.5, help='sample frame (RGB and optical flow) with which time interval')
parser.add_argument('--kernel_list', default=[1, 2, 3, 4, 5, 7, 9, 11, 15, 21, 29, 41, 57, 71, 111, 161, 211, 251],
                    type=int, nargs='+')
parser.add_argument('--max_prop_num', default=500, type=int, help='the maximum number of proposals per video')
parser.add_argument('--min_prop_num', default=50, type=int, help='the minimum number of proposals per video')
parser.add_argument('--min_prop_before_nms', default=200, type=int, help='the minimum number of proposals per video')
parser.add_argument('--pos_thresh', default=0.7, type=float)
parser.add_argument('--stride_factor', default=50, type=int, help='the proposal temporal conv kernel stride is determined by math.ceil(kernel_len/stride_factor)')

parser.add_argument('--gated_mask', action='store_true', dest='gated_mask')
parser.add_argument('--learn_mask', action='store_true', dest='learn_mask')

# Optimization: General
parser.add_argument('--batch_size', default=1, type=int, help='what is the batch size in number of images per batch? (there will be x seq_per_img sentences)')
parser.add_argument('--cuda', dest='cuda', action='store_true', help='use gpu')
parser.add_argument('--id', default='', help='an id identifying this run/job. used in cross-val and appended when writing progress files')


parser.set_defaults(cuda=False, learn_mask=False, gated_mask=False)

# args = parser.parse_args()


