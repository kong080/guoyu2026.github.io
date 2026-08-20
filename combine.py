# -*- coding: utf-8 -*-
"""将 data.json 注入 template.html 生成 index.html"""
import os, json
BASE = os.path.dirname(os.path.abspath(__file__))
tpl = open(os.path.join(BASE, "template.html"), encoding="utf-8").read()
data = open(os.path.join(BASE, "data.json"), encoding="utf-8").read()
assert "__DATA_JSON__" in tpl, "模板中找不到占位符 __DATA_JSON__"
out = tpl.replace("const DATA = __DATA_JSON__;", "const DATA = " + data + ";")
open(os.path.join(BASE, "index.html"), "w", encoding="utf-8").write(out)
print("index.html 生成完成, 大小", len(out))