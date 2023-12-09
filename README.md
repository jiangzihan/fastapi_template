# README

spacy lemma还原

模型要下好

```sh
pip3 install spacy --proxy=http://127.0.0.1:8089
curl -OL https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl -x socks5://127.0.0.1:1080
```


## boot

直接运行

```sh
python3 -m venv .venv
.venv/bin/pip3 install requirements.txt --proxy=http://127.0.0.1:8089
# 调整.env配置
python3 main.py
```