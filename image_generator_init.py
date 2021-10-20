from IPython import get_ipython

imagenet_1024 = False
imagenet_16384 = True 
gumbel_8192 = False 
coco = False
faceshq = False 
wikiart_1024 = False 
wikiart_16384 = False 
sflckr = False
ade20k = False 
ffhq = False 
celebahq = False 

def init(): 
    print("Installing Bert Extractive Summarizer...")
    get_ipython().system('pip install bert-extractive-summarizer')

    # VQGAN + CLIP
    print("Downloading CLIP...")
    get_ipython().system('git clone https://github.com/openai/CLIP                 &> /dev/null')
    
    print("Installing AI Python libraries...")
    get_ipython().system('git clone https://github.com/CompVis/taming-transformers &> /dev/null')
    get_ipython().system('pip install ftfy regex tqdm omegaconf pytorch-lightning  &> /dev/null')
    get_ipython().system('pip install kornia                                       &> /dev/null')
    get_ipython().system('pip install einops                                       &> /dev/null')
    get_ipython().system('pip install wget                                         &> /dev/null')
    
    print("Installing libraries to handle metadata...")
    get_ipython().system('pip install stegano                                      &> /dev/null')
    get_ipython().system('apt install exempi                                       &> /dev/null')
    get_ipython().system('pip install python-xmp-toolkit                           &> /dev/null')
    get_ipython().system('pip install imgtag                                       &> /dev/null')
    get_ipython().system('pip install pillow==7.1.2                                &> /dev/null')
    
    print("Installing libraries to create video...")
    get_ipython().system('pip install imageio-ffmpeg                               &> /dev/null')
    get_ipython().system('mkdir steps')

    if imagenet_1024:
        get_ipython().system('curl -L -o vqgan_imagenet_f16_1024.yaml -C - "https://heibox.uni-heidelberg.de/d/8088892a516d4e3baf92/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1" #ImageNet 1024')
        get_ipython().system('curl -L -o vqgan_imagenet_f16_1024.ckpt -C - "https://heibox.uni-heidelberg.de/d/8088892a516d4e3baf92/files/?p=%2Fckpts%2Flast.ckpt&dl=1"  #ImageNet 1024')
    if imagenet_16384:
        get_ipython().system('curl -L -o vqgan_imagenet_f16_16384.yaml -C - "https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1" #ImageNet 16384')
        get_ipython().system('curl -L -o vqgan_imagenet_f16_16384.ckpt -C - "https://heibox.uni-heidelberg.de/d/a7530b09fed84f80a887/files/?p=%2Fckpts%2Flast.ckpt&dl=1" #ImageNet 16384')
    if gumbel_8192:
        get_ipython().system('curl -L -o gumbel_8192.yaml -C - "https://heibox.uni-heidelberg.de/d/2e5662443a6b4307b470/files/?p=%2Fconfigs%2Fmodel.yaml&dl=1" #Gumbel 8192')
        get_ipython().system('curl -L -o gumbel_8192.ckpt -C - "https://heibox.uni-heidelberg.de/d/2e5662443a6b4307b470/files/?p=%2Fckpts%2Flast.ckpt&dl=1" #Gumbel 8192')
    if coco:
        get_ipython().system('curl -L -o coco.yaml -C - "https://dl.nmkd.de/ai/clip/coco/coco.yaml" #COCO')
        get_ipython().system('curl -L -o coco.ckpt -C - "https://dl.nmkd.de/ai/clip/coco/coco.ckpt" #COCO')
    if faceshq:
        get_ipython().system('curl -L -o faceshq.yaml -C - "https://drive.google.com/uc?export=download&id=1fHwGx_hnBtC8nsq7hesJvs-Klv-P0gzT" #FacesHQ')
        get_ipython().system('curl -L -o faceshq.ckpt -C - "https://app.koofr.net/content/links/a04deec9-0c59-4673-8b37-3d696fe63a5d/files/get/last.ckpt?path=%2F2020-11-13T21-41-45_faceshq_transformer%2Fcheckpoints%2Flast.ckpt" #FacesHQ')
    if wikiart_1024: 
        get_ipython().system('curl -L -o wikiart_1024.yaml -C - "http://mirror.io.community/blob/vqgan/wikiart.yaml" #WikiArt 1024')
        get_ipython().system('curl -L -o wikiart_1024.ckpt -C - "http://mirror.io.community/blob/vqgan/wikiart.ckpt" #WikiArt 1024')
    if wikiart_16384: 
        get_ipython().system('curl -L -o wikiart_16384.yaml -C - "http://eaidata.bmk.sh/data/Wikiart_16384/wikiart_f16_16384_8145600.yaml" #WikiArt 16384')
        get_ipython().system('curl -L -o wikiart_16384.ckpt -C - "http://eaidata.bmk.sh/data/Wikiart_16384/wikiart_f16_16384_8145600.ckpt" #WikiArt 16384')
    if sflckr:
        get_ipython().system('curl -L -o sflckr.yaml -C - "https://heibox.uni-heidelberg.de/d/73487ab6e5314cb5adba/files/?p=%2Fconfigs%2F2020-11-09T13-31-51-project.yaml&dl=1" #S-FLCKR')
        get_ipython().system('curl -L -o sflckr.ckpt -C - "https://heibox.uni-heidelberg.de/d/73487ab6e5314cb5adba/files/?p=%2Fcheckpoints%2Flast.ckpt&dl=1" #S-FLCKR')
    if ade20k:
        get_ipython().system('curl -L -o ade20k.yaml -C - "https://static.miraheze.org/intercriaturaswiki/b/bf/Ade20k.txt" #ADE20K')
        get_ipython().system('curl -L -o ade20k.ckpt -C - "https://app.koofr.net/content/links/0f65c2cd-7102-4550-a2bd-07fd383aac9e/files/get/last.ckpt?path=%2F2020-11-20T21-45-44_ade20k_transformer%2Fcheckpoints%2Flast.ckpt" #ADE20K')
    if ffhq:
        get_ipython().system('curl -L -o ffhq.yaml -C - "https://app.koofr.net/content/links/0fc005bf-3dca-4079-9d40-cdf38d42cd7a/files/get/2021-04-23T18-19-01-project.yaml?path=%2F2021-04-23T18-19-01_ffhq_transformer%2Fconfigs%2F2021-04-23T18-19-01-project.yaml&force" #FFHQ')
        get_ipython().system('curl -L -o ffhq.ckpt -C - "https://app.koofr.net/content/links/0fc005bf-3dca-4079-9d40-cdf38d42cd7a/files/get/last.ckpt?path=%2F2021-04-23T18-19-01_ffhq_transformer%2Fcheckpoints%2Flast.ckpt&force" #FFHQ')
    if celebahq:
        get_ipython().system('curl -L -o celebahq.yaml -C - "https://app.koofr.net/content/links/6dddf083-40c8-470a-9360-a9dab2a94e96/files/get/2021-04-23T18-11-19-project.yaml?path=%2F2021-04-23T18-11-19_celebahq_transformer%2Fconfigs%2F2021-04-23T18-11-19-project.yaml&force" #CelebA-HQ')
        get_ipython().system('curl -L -o celebahq.ckpt -C - "https://app.koofr.net/content/links/6dddf083-40c8-470a-9360-a9dab2a94e96/files/get/last.ckpt?path=%2F2021-04-23T18-11-19_celebahq_transformer%2Fcheckpoints%2Flast.ckpt&force" #CelebA-HQ')
