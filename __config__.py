WSJ0_MIX_2_8K_PATH = '/mnt/data/wsj0-mix/2speakers/wav8k'
ESC50_DOWNLOADED_P = '/tmp/ESC-50-master'
WSJ_MIX_HIERARCHICAL_P = '/mnt/nvme/hierarchical_sound_datasets/WSJ0_mix_partitioned/'
ESC50_HIERARCHICAL_P = '/mnt/nvme/hierarchical_sound_datasets/ESC50_partitioned/'
WHAM_ROOT_PATH = '/mnt/data/wham'
LIBRI2MIX_ROOT_PATH = '/mnt/data/libri_mix/Libri2Mix'
MUSDB_ROOT_PATH = '/mnt/data/Music/MUSDB18'
MUSDBWAV_ROOT_PATH = '/mnt/data/Music/MUSDB18wav'
MUSDBWAV8K_ROOT_PATH = '/mnt/data/Music/MUSDB18wav8k'
FUSS_ROOT_PATH = '/mnt/data/fuss_dataset/fuss_dev/ssdata'

# use python-dotenv instead to load the API key. the Comet.ml API key should 
# then be placed in a .env file with the variable name `API_KEY`.
from dotenv import dotenv_values
API_KEY = dotenv_values(".env")['API_KEY']
