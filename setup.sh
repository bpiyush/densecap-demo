conda create -y -n densecap python=3.6
conda activate densecap

# install torch 0.4.0
conda install pytorch=0.4.0 cuda90 -c pytorch

# install requirments for torchvision==0.1.6 compatible with pytorch==0.4.0
pip install Pillow six
pip install https://download.pytorch.org/whl/torchvision-0.1.6-py3-none-any.whl

# install torchtext==0.1.1 compatible with pytorch==0.4.0
pip install torchtext==0.1.1

# install other requirements
pip install pyyaml==5.4.1
pip install pandas argparse
pip install spacy==1.10.0

# check
python -c "import torch; print('PyTorch version: ', torch.__version__)"
python -c "import torchvision; print('Successfully imported torchvision')"
python -c "import torchtext; print('Successfully imported torchtext')"