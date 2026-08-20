# -*- coding: utf-8 -*-
"""国誉博2026 手机站构建脚本: 复制图片 + 生成 index.html(数据内嵌)"""
import os, shutil, json

BASE = os.path.dirname(os.path.abspath(__file__))
MAT  = r"d:\文档\300AI助手\302TraeWork\6a857cb91129eba8757e9457\素材"
D = os.path.join(MAT, "代理产品")
P = os.path.join(MAT, "小猪佩奇")
IMG = os.path.join(BASE, "images")
os.makedirs(IMG, exist_ok=True)

products = []
_seen = set()

def grab(src, key):
    if not os.path.exists(src): return None
    ext = os.path.splitext(src)[1].lower()
    dst = os.path.join(IMG, key + ext)
    if key not in _seen:
        shutil.copy2(src, dst); _seen.add(key)
    return "images/" + key + ext

def add(z, brand, series, name, cat, sub, spec, col, pr, imgs=(), note=""):
    ilist = []
    for key in imgs:
        r = grab(os.path.join(D, key + ".jpg"), key)
        if not r:
            r = grab(os.path.join(D, key + ".webp"), key)
        if not r:
            r = grab(os.path.join(P, key + ".jpg"), key)
        if not r:
            r = grab(os.path.join(P, key + ".png"), key)
        if r: ilist.append(r)
    products.append(dict(z=z, brand=brand, series=series, name=name, cat=cat,
                         sub=sub, spec=spec, col=col, pr=pr, img=ilist, note=note))

# ================= 限定 =================
L="限定"
add(L,"KOKUYO限定","HAKU","2026 HAKU主题限定套装","本册","限定套装","螺旋本·无线装订本","A5螺旋/ A6无线",45,note="A5 40页双螺旋 + A6 无线本 + 中性笔 + 束口袋")
add(L,"KOKUYO限定","绣线书香","限定无线装订本(绣线书香)","本册","无线装订本","无线装订本","B5·中式刺绣",32.8,note="藏青底白酒双雀 + 清代短丝荷塘")
add(L,"KOKUYO限定","浮生画卷","限定无线装订本(浮生画卷)","本册","无线装订本","无线装订本","A5·世界名画",24,note="冲浪里/街巷/猫咪/骷髅")
add(L,"KOKUYO限定","书写套装","A6限定书写套装","本册","书写套装","套装","A6",27,note="5款经典用纸装订成册")
add(L,"KOKUYO限定","限定新品TOP1","STUDY HOLIC B5无线装订本","本册","无线装订本","无线装订本","古生物/古埃及/考古/海洋/人类",17.5,note="限量TOP1·各17.5元")
add(L,"STUDY HOLIC","限定新品TOP1","两用书签(2WAY)","工具","书签","书签","多主题",9.5)
add(L,"STUDY HOLIC","限定新品TOP1","测量野帐","本册","野帐","野帐","古生物/考古/古埃及",28.6,note="硬壳 3mm方格 可盖章")
add(L,"STUDY HOLIC","限定新品TOP1","双层分类收纳笔袋","包袋","笔袋","笔袋","5主题",40)
add(L,"STUDY HOLIC","限定新品TOP1","托特包","包袋","托特包","托特包","考古/古生物/古埃及/人类学",52)
add(L,"UHA×KOKUYO","糖果联名","无线装订本(糖果封面)","本册","无线装订本","无线装订本","牛奶糖/酷露露等",24)
add(L,"UHA×KOKUYO","糖果联名","迷你收纳包","包袋","收纳包","收纳包","葡萄酷露露",29.8)
add(L,"KOKUYO限定","mini系列","限定mini包","包袋","收纳包","迷你包","米白帆布",29.8)
add(L,"KOKUYO限定","mini系列","mini波士顿包","包袋","书包","波士顿包","mini",29.8)

# ================= 联名 =================
Z="联名"
# 塔卡沙 (有价格明细)
add(Z,"塔卡沙TYAKASHA","联名明细","Campus收纳包","包袋","收纳包","收纳包","绿色/蓝色",117.1,note="210×135×25mm WSG-PC3M132")
add(Z,"塔卡沙TYAKASHA","联名明细","横开笔袋","包袋","笔袋","笔袋","蓝色/白色/黄色",54.4,note="210×80×45mm WSG-PC3M322")
add(Z,"塔卡沙TYAKASHA","联名明细","Campus学院风背提包","包袋","书包","背提包","深蓝/棕色",198.8,note="420×280×125mm WSG-SB3M16")
add(Z,"塔卡沙TYAKASHA","联名明细","网格口袋书包","包袋","书包","书包","深蓝/黄色",258.8,note="约15.4L WSG-SB3M14")
add(Z,"塔卡沙TYAKASHA","联名明细","折叠伞","伞具","折叠伞","伞","2色",180,note="约237g 防紫外线")
# 高旗将雄
add(Z,"高旗将雄","熊の森生活","Campus扩容笔袋","包袋","笔袋","笔袋","观星/吃饭",57.8,note="205×115×40mm WSG-PCFM373")
add(Z,"高旗将雄","熊の森生活","无线装订本","本册","无线装订本","无线装订本","B5 / A5",None,note="Campus日本进口原纸")
add(Z,"高旗将雄","熊の森生活","软线圈本","本册","软线圈本","软线圈本","B5 / A6",None)
add(Z,"高旗将雄","熊の森生活","牛皮纸四孔活页本","本册","活页本","四孔活页本","B5 / A5",None)
add(Z,"高旗将雄","熊の森生活","按动中性笔","笔具","圆珠笔","0.5mm","多色",None)
add(Z,"高旗将雄","熊の森生活","Campus原纸色修正带","工具","修正带","修正带","标准",None)
add(Z,"高旗将雄","熊の森生活","单片夹套装","工具","文件","A4","一套4张",None)
add(Z,"高旗将雄","熊の森生活","托特包","包袋","托特包","托特包","单肩",None)
# GreenFlash Pixelook
add(Z,"GreenFlash Pixelook","像素风","无线装订本","本册","无线装订本","无线装订本","B5·180°平摊",None)
add(Z,"GreenFlash Pixelook","像素风","软线圈本","本册","软线圈本","软线圈本","A6·360°翻转",None)
add(Z,"GreenFlash Pixelook","像素风","两孔mini活页本","本册","活页本","活页本","A7",None)
add(Z,"GreenFlash Pixelook","像素风","按动中性笔","笔具","圆珠笔","0.5mm双珠","多色",None)
add(Z,"GreenFlash Pixelook","像素风","Campus原纸色修正带","工具","修正带","修正带","标准",None)
add(Z,"GreenFlash Pixelook","像素风","透明收纳包","包袋","收纳包","收纳包","透明",None)
add(Z,"GreenFlash Pixelook","像素风","限定金属挂件","周边","挂件","挂件","12种图案",None)
# 小猪佩奇 (第4弹,有图无价)
add(Z,"小猪佩奇","童趣甜心&永恒经典","Campus无线装订本","本册","无线装订本","无线装订本","B5/A5/A6·满版/拼贴",None,
    imgs="Campus无线装订本_01 Campus无线装订本_02 Campus无线装订本_03 Campus无线装订本_04 Campus无线装订本_05 Campus无线装订本_06 Campus无线装订本_07 Campus无线装订本_08".split())
add(Z,"小猪佩奇","童趣甜心&永恒经典","Campus软线圈本","本册","软线圈本","软线圈本","A5/A6",None,
    imgs="Campus软线圈本_01 Campus软线圈本_02 Campus软线圈本_03 Campus软线圈本_04".split())
add(Z,"小猪佩奇","童趣甜心&永恒经典","Campus螺旋本","本册","螺旋本","螺旋本","A7",None,
    imgs="Campus螺旋本_01 Campus螺旋本_02 Campus螺旋本_03 Campus螺旋本_04".split())
add(Z,"小猪佩奇","童趣甜心&永恒经典","草稿本","本册","草稿本","无线胶装","A5",None,
    imgs="草稿本_01 草稿本_02".split())
add(Z,"小猪佩奇","童趣甜心&永恒经典","高透明笔袋","包袋","笔袋","笔袋","4款·托盘款",None,
    imgs="高透明笔袋_01 高透明笔袋_02 高透明笔袋_03 高透明笔袋_04".split())
add(Z,"小猪佩奇","童趣甜心&永恒经典","桌立式笔袋","包袋","笔袋","笔盒笔袋2in1","多色",None,
    imgs="桌立式笔袋_01 桌立式笔袋_02 桌立式笔袋_03 桌立式笔袋_04".split())
add(Z,"小猪佩奇","童趣甜心&永恒经典","按动中性笔&修正带","笔具","圆珠笔","0.5mm","转印图案",None,
    imgs="按动中性笔&修正带_01 按动中性笔&修正带_02 按动中性笔&修正带_03 按动中性笔&修正带_04 按动中性笔&修正带_05 按动中性笔&修正带_06 按动中性笔&修正带_07".split())
add(Z,"小猪佩奇","童趣甜心&永恒经典","HB三角铅笔&活动铅笔","笔具","铅笔","三角/活动","多色",None,
    imgs="HB三角铅笔&活动铅笔_01 HB三角铅笔&活动铅笔_02 HB三角铅笔&活动铅笔_03 HB三角铅笔&活动铅笔_04 HB三角铅笔&活动铅笔_05".split())
add(Z,"小猪佩奇","童趣甜心&永恒经典","角角乐橡皮","工具","橡皮","角角乐","45°/90°",None,
    imgs="角角乐橡皮_01 角角乐橡皮_02 角角乐橡皮_03".split())
add(Z,"小猪佩奇","童趣甜心&永恒经典","学生套尺","工具","尺子","套尺","5件套",None,
    imgs="学生套尺_01 学生套尺_02 学生套尺_03".split())

# ================= 代理品牌 =================
J="代理"
# 北村人×GreenFlash
add(J,"北村人×GreenFlash","首次入驻","便签本","本册","便签本","便签本","蜡笔风",None,
    imgs="便签本_01 便签本_02".split())
add(J,"北村人×GreenFlash","首次入驻","便利贴&胶带","贴纸","便利贴/胶带","装饰","多款",None,
    imgs="便利贴&胶带_01 便利贴&胶带_02".split())
add(J,"北村人×GreenFlash","首次入驻","圆珠笔(亚克力挂件)","笔具","圆珠笔","圆珠笔","透明",None,
    imgs="圆珠笔_01 圆珠笔_02".split())
add(J,"北村人×GreenFlash","首次入驻","亚克力夹子","工具","夹子","夹子","多款",None,
    imgs="夹子_01 夹子_02".split())
add(J,"北村人×GreenFlash","首次入驻","A4透明文件夹","工具","文件","三口袋","透明",None,
    imgs="文件袋_01 文件袋_02".split())
add(J,"北村人×GreenFlash","首次入驻","PVC收纳袋","包袋","收纳包","PVC","多款",None,
    imgs="PVC收纳袋_01 PVC收纳袋_02".split())
add(J,"北村人×GreenFlash","首次入驻","折叠收纳袋","包袋","收纳包","折叠","轻便",None,
    imgs="折叠收纳袋_01 折叠收纳袋_02 折叠收纳袋_03".split())
add(J,"北村人×GreenFlash","首次入驻","托特包(刺绣)","包袋","托特包","托特包","多款",None,
    imgs="托特包_01 托特包_02 托特包_03".split())
# GreenFlash 未知生物
add(J,"GreenFlash未知生物","第2弹","方形便签本","本册","便签本","透明PVC","神秘生物",None,
    imgs="方形便签本_01 方形便签本_02 方形便签本_03 方形便签本_04".split())
add(J,"GreenFlash未知生物","第2弹","七款极光贴纸","贴纸","贴纸","防水闪粉","7款",None,
    imgs="七款极光贴纸_01 七款极光贴纸_02".split())
add(J,"GreenFlash未知生物","第2弹","PVC迷你收纳袋","包袋","收纳包","PVC铁片","多款",None,
    imgs="PVC迷你收纳袋_01 PVC迷你收纳袋_02 PVC迷你收纳袋_03".split())
add(J,"GreenFlash未知生物","第2弹","方形收纳包","包袋","收纳包","绒布","多款",None,
    imgs="方形收纳包_01 方形收纳包_02 方形收纳包_03 方形收纳包_04".split())
# 艾普克
add(J,"艾普克","萌宠便签本","可折叠萌宠便签本","本册","便签本","可折叠站立","3款猫咪",None,
    imgs=["可折叠萌宠便签本_%02d"%i for i in range(1,11)], note="可平躺可折叠站立 背面动物头像咬合")
add(J,"艾普克","撕撕乐","撕撕乐卷卷贴纸","贴纸","贴纸","超长卷卷","循环图案",None,
    imgs=["撕撕乐卷卷贴纸_%02d"%i for i in range(1,12)], note="随用随撕 图案循环")
add(J,"艾普克","模切","萌趣模切分装贴纸","贴纸","贴纸","预裁形状","多主题",None,
    imgs=["萌趣模切分装贴纸_%02d"%i for i in range(1,9)], note="一撕即完整小可爱 无白边")
# NB株式会社
add(J,"NB株式会社","夏日系列","夏日系列异形明信片","纸品","明信片","异形","企鹅/北极熊/海豹",None,
    imgs=["夏日系列 异形明信片_%02d"%i for i in range(1,5)])
add(J,"NB株式会社","贺卡","贺卡 unbox 曲奇礼盒","纸品","贺卡","铁盒","复古绿",None,
    imgs="贺卡 unbox 曲奇礼盒_01 贺卡 unbox 曲奇礼盒_02".split())
add(J,"NB株式会社","贴纸","My mood 和纸贴纸","贴纸","贴纸","和纸","啾啾/小兔/猫咪/修勾",None,
    imgs="My mood 和纸贴纸_01 My mood 和纸贴纸_02 My mood 和纸贴纸_03 My mood 和纸贴纸_04".split())
add(J,"NB株式会社","信纸","悠闲小动物日常 夜晚 迷你信纸","纸品","信纸","迷你信纸","啾啾团子/企鹅",None,
    imgs="悠闲小动物的日常 夜晚 迷你信纸_01 悠闲小动物的日常 夜晚 迷你信纸_02".split())
add(J,"NB株式会社","盒装贴纸","RESSA PANDA BOOKS 盒装贴纸","贴纸","贴纸","盒装","熊猫店长/小猫/水獭",None,
    imgs="RESSA PANDA BOOKS 盒装贴纸_01 RESSA PANDA BOOKS 盒装贴纸_02 RESSA PANDA BOOKS 盒装贴纸_03 RESSA PANDA BOOKS 盒装贴纸_04 RESSA PANDA BOOKS 盒装贴纸_05 RESSA PANDA BOOKS 盒装贴纸_06".split())
add(J,"NB株式会社","贴纸","啾言啾语 贴纸","贴纸","贴纸","日常","小鸟碎碎念",None,
    imgs="啾言啾语 贴纸_01 啾言啾语 贴纸_02".split())
add(J,"NB株式会社","便签本","便签本(毛茸茸脑袋)","本册","便签本","便签本","多款",None,
    imgs="便签本_01 便签本_02".split())
add(J,"NB株式会社","鹦鹉信纸","Pyokotto 迷你信纸 鹦鹉","纸品","信纸","迷你信纸","粉紫暮色",None,
    imgs="Pyokotto 迷你信纸 鹦鹉_01 Pyokotto 迷你信纸 鹦鹉_02".split())
add(J,"NB株式会社","明信片","Creald 明信片 山雀和菓子","纸品","明信片","明信片","雪白糯米",None,
    imgs="Creald 明信片 北长尾山雀和和菓子_01".split())
add(J,"NB株式会社","便签本","猫咪日常 便签本 茂三郎","本册","便签本","昭和咖啡店","复古",None,
    imgs="猫咪日常 便签本 茂三郎_01".split())
add(J,"NB株式会社","山野町内会","山野町内会 信纸","纸品","信纸","信纸","露营/星空/划船",None,
    imgs=["山野町内会 信纸_%02d"%i for i in range(1,5)])
add(J,"NB株式会社","山野町内会","山野町内会 便签本","本册","便签本","便签本","小熊/松鼠",None,
    imgs=["山野町内会 便签本_%02d"%i for i in range(1,7)])
add(J,"NB株式会社","山野町内会","山野町内会 明信片","纸品","明信片","明信片","企鹅等",None,
    imgs=["山野町内会 明信片_%02d"%i for i in range(1,9)])
add(J,"NB株式会社","山野町内会","山野町内会 和纸贴纸","贴纸","贴纸","和纸","狐狸等",None,
    imgs=["山野町内会 和纸贴纸_%02d"%i for i in range(1,9)])
add(J,"NB株式会社","山野町内会","山野町内会 贴纸","贴纸","贴纸","贴纸","狐狸等",None,
    imgs=["山野町内会 贴纸_%02d"%i for i in range(1,9)])
# ZOOm in Animals
add(J,"ZOOm in Animals","动物便签","异形便签套装","本册","便签本","异形套装","多款",None,
    imgs=["ZOOm in Animals 异形便签套装_%02d"%i for i in range(1,8)])
add(J,"ZOOm in Animals","动物信纸","迷你异形信纸套装","纸品","信纸","迷你异形","多款",None,
    imgs=["ZOOm in Animals 迷你异形信纸套装_%02d"%i for i in range(1,8)])
add(J,"ZOOm in Animals","信纸","迷你信纸套装","纸品","信纸","迷你信纸","多款",None,
    imgs=["ZOOm in Animals 迷你信纸套装_%02d"%i for i in range(1,5)])
add(J,"ZOOm in Animals","贴纸","和纸贴纸","贴纸","贴纸","和纸","动物",None,
    imgs=["ZOOm in Animals 和纸贴纸_%02d"%i for i in range(1,8)])
add(J,"ZOOm in Animals","便签","异形便签","本册","便签本","异形","动物",None,
    imgs=["ZOOm in Animals 异形便签_%02d"%i for i in range(1,7)])

print("总商品数:", len(products))
# 保存数据
data = json.dumps(products, ensure_ascii=False)
with open(os.path.join(BASE, "data.json"), "w", encoding="utf-8") as f:
    f.write(data)
print("图片复制+数据生成完成, 图片目录含", len(os.listdir(IMG)), "个文件")