export PYTHONPATH=$PWD:/home/pbagad/projects/coco-caption/

epoch=19
split='validation'
cfgs_file='cfgs/anet.yml'

id=anet-2L-gt-mask
python3 scripts/test.py \
    --cfgs_file $cfgs_file \
    --densecap_eval_file ./tools/densevid_eval/evaluate.py \
    --batch_size 1 \
    --start_from ./checkpoint/$id/model_epoch_$epoch.t7 \
    --id $id-$epoch \
    --val_data_folder $split \
    --cuda | tee log/eval-$id-epoch$epoch

# id=anet-2L-e2e-mask
# python3 scripts/test.py \
#     --cfgs_file $cfgs_file \
#     --densecap_eval_file ./tools/densevid_eval/evaluate.py \
#     --batch_size 1 \
#     --start_from ./checkpoint/$id/model_epoch_$epoch.t7 \
#     --id $id-$epoch \
#     --val_data_folder $split \
#     --learn_mask \
#     --gated_mask \
#     --cuda | tee log/eval-$id-epoch$epoch