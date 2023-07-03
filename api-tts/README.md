### VITS模型

将模型放入`/usr/local/vits-simple-api/Model`

<details><summary>Folder structure</summary><pre><code>
│  hubert-soft-0d54a1f4.pt
│  model.onnx
│  model.yaml
├─g
│      config.json
│      G_953000.pth
│
├─louise
│      360_epochs.pth
│      config.json
│
├─Nene_Nanami_Rong_Tang
│      1374_epochs.pth
│      config.json
│
├─Zero_no_tsukaima
│       1158_epochs.pth
│       config.json
│
└─npy
       25ecb3f6-f968-11ed-b094-e0d4e84af078.npy
       all_emotions.npy
</code></pre></details>



### 修改模型路径

Modify in  `/usr/local/vits-simple-api/config.py` 

<details><summary>config.py</summary><pre><code>
# 在此填写模型路径
MODEL_LIST = [
    # VITS
    [ABS_PATH + "/Model/Nene_Nanami_Rong_Tang/1374_epochs.pth", ABS_PATH + "/Model/Nene_Nanami_Rong_Tang/config.json"],
    [ABS_PATH + "/Model/Zero_no_tsukaima/1158_epochs.pth", ABS_PATH + "/Model/Zero_no_tsukaima/config.json"],
    [ABS_PATH + "/Model/g/G_953000.pth", ABS_PATH + "/Model/g/config.json"],
    # HuBert-VITS (Need to configure HUBERT_SOFT_MODEL)
    [ABS_PATH + "/Model/louise/360_epochs.pth", ABS_PATH + "/Model/louise/config.json"],
    # W2V2-VITS (Need to configure DIMENSIONAL_EMOTION_NPY)
    [ABS_PATH + "/Model/w2v2-vits/1026_epochs.pth", ABS_PATH + "/Model/w2v2-vits/config.json"],
]
# hubert-vits: hubert soft 编码器
HUBERT_SOFT_MODEL = ABS_PATH + "/Model/hubert-soft-0d54a1f4.pt"
# w2v2-vits: Dimensional emotion npy file
# 加载单独的npy: ABS_PATH+"/all_emotions.npy
# 加载多个npy: [ABS_PATH + "/emotions1.npy", ABS_PATH + "/emotions2.npy"]
# 从文件夹里加载npy: ABS_PATH + "/Model/npy"
DIMENSIONAL_EMOTION_NPY = ABS_PATH + "/Model/npy"
# w2v2-vits: 需要在同一路径下有model.onnx和model.yaml
DIMENSIONAL_EMOTION_MODEL = ABS_PATH + "/Model/model.yaml"
</code></pre></details>

###  下载python依赖
`pip install -r requirements.txt`

### 启动

`python app.py`

# API

## GET

#### speakers list 

- GET http://127.0.0.1:23456/voice/speakers

  返回id对应角色的映射表

#### voice vits

- GET http://127.0.0.1:23456/voice/vits?text=text

  其他参数不指定时均为默认值

- GET http://127.0.0.1:23456/voice/vits?text=[ZH]text[ZH][JA]text[JA]&lang=mix

  lang=mix时文本要标注

- GET http://127.0.0.1:23456/voice/vits?text=text&id=142&format=wav&lang=zh&length=1.4

  文本为text，角色id为142，音频格式为wav，文本语言为zh，语音长度为1.4，其余参数默认

