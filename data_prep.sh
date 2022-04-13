
# setup data
mkdir -p data/anet

# download annotation files
cd data/
wget http://youcook2.eecs.umich.edu/static/dat/anet_densecap/anet.tar.gz
tar -xvf anet.tar.gz
rm -rf anet.tar.gz
echo "Downloaded annotation files"

# download video features for validation set
cd anet/
wget http://youcook2.eecs.umich.edu/static/dat/anet_densecap/validation_feat_anet.tar.gz
tar -xvf validation_feat_anet.tar.gz
echo "Downloaded video features for validation set"
num_resnet=`ls -l validation/*_resnet.npy | wc -l`
echo "Number of resnet features: $num_resnet"
rm -rf validation_feat_anet.tar.gz

# download evalution code
cd ../tools/
git clone https://github.com/LuoweiZhou/densevid_eval
cd ../

# download pre-trained models
mkdir -p checkpoint
cd checkpoint
wget http://youcook2.eecs.umich.edu/static/dat/densecap_checkpoints/pre-trained-models.tar.gz
tar -xvf pre-trained-models.tar.gz
rm -rf pre-trained-models.tar.gz
cd ../

