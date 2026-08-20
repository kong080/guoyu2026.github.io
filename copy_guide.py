# -*- coding: utf-8 -*-
"""把攻略页配图从素材目录复制到 _site/guide，并改ASCII名"""
import os, shutil
MAT = r"d:\文档\300AI助手\302TraeWork\6a857cb91129eba8757e9457\素材"
G   = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guide")
os.makedirs(G, exist_ok=True)

pairs = [
    ("扭蛋区_01.webp",          "g_gacha.webp"),
    ("大头贴拍照机_01.webp",     "g_photo.webp"),
    ("会场盖章区_01.webp",       "g_stamp.webp"),
    ("冰箱贴赠礼_01.webp",       "g_magnet_1.webp"),
    ("冰箱贴赠礼_02.webp",       "g_magnet_2.webp"),
    ("TYAKASHA小屋_01.webp",     "g_hut_1.webp"),
    ("TYAKASHA小屋_02.webp",     "g_hut_2.webp"),
    ("TYAKASHA小屋_03.webp",     "g_hut_3.webp"),
]
for src, dst in pairs:
    s = os.path.join(MAT, src)
    d = os.path.join(G, dst)
    if os.path.exists(s):
        shutil.copy2(s, d); print("OK", dst)
    else:
        print("MISS", src)
print("guide 目录:", len(os.listdir(G)), "个文件")