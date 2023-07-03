import re
import requests
import os
import random
import string
from requests_toolbelt.multipart.encoder import MultipartEncoder

abs_path = os.path.dirname(__file__)
base = "http://127.0.0.1:23456"


# 映射表
def voice_speakers():
    url = f"{base}/voice/speakers"

    res = requests.post(url=url)
    json = res.json()
    for i in json:
        print(i)
        for j in json[i]:
            print(j)
    return json


# 语音合成 voice vits
def voice_vits(text, id=0, format="wav", lang="auto", length=1, noise=0.667, noisew=0.8, max=50):
    fields = {
        "text": text,
        "id": str(id),
        "format": format,
        "lang": lang,
        "length": str(length),
        "noise": str(noise),
        "noisew": str(noisew),
        "max": str(max)
    }
    boundary = '----VoiceConversionFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))

    m = MultipartEncoder(fields=fields, boundary=boundary)
    headers = {"Content-Type": m.content_type}
    url = f"{base}/voice"

    res = requests.post(url=url, data=m, headers=headers)
    fname = re.findall("filename=(.+)", res.headers["Content-Disposition"])[0]
    path = f"{abs_path}/{fname}"

    with open(path, "wb") as f:
        f.write(res.content)
    print(path)
    return path


# 语音转换 hubert-vits
def voice_hubert_vits(upload_path, id, format="wav", length=1, noise=0.667, noisew=0.8):
    upload_name = os.path.basename(upload_path)
    upload_type = f'audio/{upload_name.split(".")[1]}'  # wav,ogg

    with open(upload_path, 'rb') as upload_file:
        fields = {
            "upload": (upload_name, upload_file, upload_type),
            "id": str(id),
            "format": format,
            "length": str(length),
            "noise": str(noise),
            "noisew": str(noisew),
        }
        boundary = '----VoiceConversionFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))

        m = MultipartEncoder(fields=fields, boundary=boundary)
        headers = {"Content-Type": m.content_type}
        url = f"{base}/voice/hubert-vits"

        res = requests.post(url=url, data=m, headers=headers)
    fname = re.findall("filename=(.+)", res.headers["Content-Disposition"])[0]
    path = f"{abs_path}/{fname}"

    with open(path, "wb") as f:
        f.write(res.content)
    print(path)
    return path


# 维度情感模型 w2v2-vits
def voice_w2v2_vits(text, id=0, format="wav", lang="auto", length=1, noise=0.667, noisew=0.8, max=50, emotion=0):
    fields = {
        "text": text,
        "id": str(id),
        "format": format,
        "lang": lang,
        "length": str(length),
        "noise": str(noise),
        "noisew": str(noisew),
        "max": str(max),
        "emotion": str(emotion)
    }
    boundary = '----VoiceConversionFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))

    m = MultipartEncoder(fields=fields, boundary=boundary)
    headers = {"Content-Type": m.content_type}
    url = f"{base}/voice/w2v2-vits"

    res = requests.post(url=url, data=m, headers=headers)
    fname = re.findall("filename=(.+)", res.headers["Content-Disposition"])[0]
    path = f"{abs_path}/{fname}"

    with open(path, "wb") as f:
        f.write(res.content)
    print(path)
    return path


# 语音转换 同VITS模型内角色之间的音色转换
def voice_conversion(upload_path, original_id, target_id):
    upload_name = os.path.basename(upload_path)
    upload_type = f'audio/{upload_name.split(".")[1]}'  # wav,ogg

    with open(upload_path, 'rb') as upload_file:
        fields = {
            "upload": (upload_name, upload_file, upload_type),
            "original_id": str(original_id),
            "target_id": str(target_id),
        }
        boundary = '----VoiceConversionFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))
        m = MultipartEncoder(fields=fields, boundary=boundary)

        headers = {"Content-Type": m.content_type}
        url = f"{base}/voice/conversion"

        res = requests.post(url=url, data=m, headers=headers)

    fname = re.findall("filename=(.+)", res.headers["Content-Disposition"])[0]
    path = f"{abs_path}/{fname}"

    with open(path, "wb") as f:
        f.write(res.content)
    print(path)
    return path


def voice_ssml(ssml):
    fields = {
        "ssml": ssml,
    }
    boundary = '----VoiceConversionFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))

    m = MultipartEncoder(fields=fields, boundary=boundary)
    headers = {"Content-Type": m.content_type}
    url = f"{base}/voice/ssml"

    res = requests.post(url=url, data=m, headers=headers)
    fname = re.findall("filename=(.+)", res.headers["Content-Disposition"])[0]
    path = f"{abs_path}/{fname}"

    with open(path, "wb") as f:
        f.write(res.content)
    print(path)
    return path


def voice_dimensional_emotion(upload_path):
    upload_name = os.path.basename(upload_path)
    upload_type = f'audio/{upload_name.split(".")[1]}'  # wav,ogg

    with open(upload_path, 'rb') as upload_file:
        fields = {
            "upload": (upload_name, upload_file, upload_type),
        }
        boundary = '----VoiceConversionFormBoundary' + ''.join(random.sample(string.ascii_letters + string.digits, 16))

        m = MultipartEncoder(fields=fields, boundary=boundary)
        headers = {"Content-Type": m.content_type}
        url = f"{base}/voice/dimension-emotion"

        res = requests.post(url=url, data=m, headers=headers)
    fname = re.findall("filename=(.+)", res.headers["Content-Disposition"])[0]
    path = f"{abs_path}/{fname}"

    with open(path, "wb") as f:
        f.write(res.content)
    print(path)
    return path


import time

# while 1:
#     text = input()
#     l = len(text)
#     time1 = time.time()
#     voice_vits(text)
#     time2 = time.time()
#     print(f"len:{l}耗时:{time2 - time1}")

# text = "你好"


# ssml = """
# <speak lang="zh" format="mp3" length="1.2">
#     <voice id="92" >这几天心里颇不宁静。</voice>
#     <voice id="125">今晚在院子里坐着乘凉，忽然想起日日走过的荷塘，在这满月的光里，总该另有一番样子吧。</voice>
#     <voice id="142">月亮渐渐地升高了，墙外马路上孩子们的欢笑，已经听不见了；</voice>
#     <voice id="98">妻在屋里拍着闰儿，迷迷糊糊地哼着眠歌。</voice>
#     <voice id="120">我悄悄地披了大衫，带上门出去。</voice><break time="2s"/>
#     <voice id="121">沿着荷塘，是一条曲折的小煤屑路。</voice>
#     <voice id="122">这是一条幽僻的路；白天也少人走，夜晚更加寂寞。</voice>
#     <voice id="123">荷塘四面，长着许多树，蓊蓊郁郁的。</voice>
#     <voice id="124">路的一旁，是些杨柳，和一些不知道名字的树。</voice>
#     <voice id="125">没有月光的晚上，这路上阴森森的，有些怕人。</voice>
#     <voice id="126">今晚却很好，虽然月光也还是淡淡的。</voice><break time="2s"/>
#     <voice id="127">路上只我一个人，背着手踱着。</voice>
#     <voice id="128">这一片天地好像是我的；我也像超出了平常的自己，到了另一个世界里。</voice>
#     <voice id="129">我爱热闹，也爱冷静；<break strength="x-weak"/>爱群居，也爱独处。</voice>
#     <voice id="130">像今晚上，一个人在这苍茫的月下，什么都可以想，什么都可以不想，便觉是个自由的人。</voice>
#     <voice id="131">白天里一定要做的事，一定要说的话，现在都可不理。</voice>
#     <voice id="132">这是独处的妙处，我且受用这无边的荷香月色好了。</voice>
# </speak>
# """
# ssml = """
# <speak lang="zh">
#     <voice id="92" length="1.4">这几天心里颇不宁静。今晚<break/>在院子里坐着乘凉，忽然想起<break/>日日走过的荷塘，在这满月的光里，总该另有一番样子吧。</voice>
#     <voice id="142" length="1.4">月亮渐渐地升高了，墙外马路上孩子们的欢笑，已经听不见了；</voice><break time="2s"/>
#     <voice id="0" length="1.4" model="w2v2-vits" lang="ja">こんにちは</voice>
# </speak>
# """
# ssml = """
# <speak lang="ja">
#     <voice id="142" length="1.4">こんにちは</voice>
#     <voice id="0" length="1.4" model="w2v2-vits" emotion="177">こんにちは</voice>
#     <voice id="0" length="1.4" model="w2v2-vits">こんにちは</voice>
# </speak>
# """
ssml = """
<speak lang="auto">
    <voice>这几天心里颇不宁静。</voice>
    <voice>今晚在院子里坐着乘凉，忽然想起日日走过的荷塘，在这满月的光里，总该另有一番样子吧。</voice>
    <voice>月亮渐渐地升高了，墙外马路上孩子们的欢笑，已经听不见了；</voice>
    <voice>妻在屋里拍着闰儿，迷迷糊糊地哼着眠歌。</voice>
    <voice>我悄悄地披了大衫，带上门出去。</voice><break time="2s"/>
    <voice>沿着荷塘，是一条曲折的小煤屑路。</voice>
    <voice>这是一条幽僻的路；白天也少人走，夜晚更加寂寞。</voice>
    <voice>荷塘四面，长着许多树，蓊蓊郁郁的。</voice>
    <voice>路的一旁，是些杨柳，和一些不知道名字的树。</voice>
    <voice>没有月光的晚上，这路上阴森森的，有些怕人。</voice>
    <voice>今晚却很好，虽然月光也还是淡淡的。</voice><break time="2s"/>
    <voice>路上只我一个人，背着手踱着。</voice>
    <voice>这一片天地好像是我的；我也像超出了平常的自己，到了另一个世界里。</voice>
    <voice>我爱热闹，也爱冷静；<break strength="x-weak"/>爱群居，也爱独处。</voice>
    <voice>像今晚上，一个人在这苍茫的月下，什么都可以想，什么都可以不想，便觉是个自由的人。</voice>
    <voice>白天里一定要做的事，一定要说的话，现在都可不理。</voice>
    <voice>这是独处的妙处，我且受用这无边的荷香月色好了。</voice>
</speak>
"""

text = """你知道1+1=几吗？我觉得1+1≠3"""

t1 = time.time()
# voice_conversion("H:/git/vits-simple-api/47fa127a-03ab-11ee-a4dc-e0d4e84af078.wav", 91, 93)
# voice_hubert_vits("H:/git/vits-simple-api/47fa127a-03ab-11ee-a4dc-e0d4e84af078.wav",0)
# voice_vits(text,format="wav",lang="zh")
# voice_w2v2_vits(text,emotion=111)
# os.system(voice_ssml(ssml))
os.system(voice_vits(text,id=126, format="wav", max=0,noise=0.33,noisew=0.4,lang="zh"))
# voice_dimensional_emotion("H:/git/vits-simple-api/47fa127a-03ab-11ee-a4dc-e0d4e84af078.wav")
t2 = time.time()
# print(f"len:{len(text)}耗时:{t2 - t1}")
# for i in range(10):
#     t1 = time.time()
#     voice_vits(text, format="wav", lang="zh")
#     t2 = time.time()
#     print(f"len:{len(text)}耗时:{t2 - t1}")
