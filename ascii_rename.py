# -*- coding: utf-8 -*-
"""把 _site/images 下所有图片改为纯ASCII名(item0001.jpg), 重写 data.json 并重建 index.html"""
import os, json, shutil

BASE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(BASE, "images")
DJSON = os.path.join(BASE, "data.json")
TPL = os.path.join(BASE, "template.html")
IDX = os.path.join(BASE, "index.html")

d = json.load(open(DJSON, encoding="utf-8"))

# 收集全部引用路径(保留顺序), 去重
seen = []
for p in d:
    for im in p["img"]:
        if im not in seen:
            seen.append(im)

mapping = {}
count = 0
for old in seen:
    src = os.path.join(BASE, old)
    if not os.path.exists(src):
        print("MISS src:", old); continue
    ext = os.path.splitext(old)[1].lower() or ".jpg"
    count += 1
    new = f"item{count:04d}{ext}"
    dst = os.path.join(IMG, new)
    shutil.copy2(src, dst)
    mapping[old] = "images/" + new

# 重写 data.json
for p in d:
    p["img"] = [mapping.get(im, im) for im in p["img"]]
json.dump(d, open(DJSON, "w", encoding="utf-8"), ensure_ascii=False)

# 重建 index.html
t = open(TPL, encoding="utf-8").read()
html = t.replace("__DATA_JSON__", json.dumps(d, ensure_ascii=False))
open(IDX, "w", encoding="utf-8").write(html)

# 删除旧中文文件
for old in seen:
    p = os.path.join(BASE, old)
    if os.path.exists(p):
        try: os.remove(p)
        except: pass

print("重命名完成:", count, "张 -> images/itemnnnn")
print("data.json 与 index.html 已重建")