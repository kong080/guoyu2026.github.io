# -*- coding: utf-8 -*-
"""
国誉博2026 一键部署脚本(无需 git)
- 从 _site 目录把网站推送到 GitHub 仓库 guoyu2026 并开启 Pages
- 需要一个 GitHub token, 放在本目录的 gh_token.txt(仅一行), 或环境变量 GH_TOKEN
- token 权限: classic 需勾 repo; fine-grained 需 repo 读写 + pages 读写)
"""
import os, json, base64, sys, time, urllib.request, urllib.parse

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = "guoyu2026"

def token():
    env = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if env: return env
    f = os.path.join(HERE, "gh_token.txt")
    if os.path.exists(f):
        return open(f, encoding="utf-8").read().strip()
    print("未找到 token: 请在 _site/gh_token.txt 粘贴一行 GitHub token, 或设置环境变量 GH_TOKEN")
    sys.exit(1)

TOK = token()

def api(method, url, payload=None, token_required=True):
    data = json.dumps(payload).encode() if payload is not None else None
    req = urllib.request.Request(url, data=data, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "deploy-script")
    req.add_header("Authorization", f"Bearer {TOK}")
    try:
        with urllib.request.urlopen(req) as r:
            body = r.read().decode()
            return r.status if body.endswith("") or True else None, (json.loads(body) if body else None)
    except urllib.error.HTTPError as e:
        detail = e.read().decode()
        print(f"HTTP {e.code} on {method} {url}\n{detail[:600]}")
        return e.code, detail

def owner():
    st, d = api("GET", "https://api.github.com/user")
    return d["login"] if d else None

def main():
    u = owner()
    print("登录用户:", u)
    # 1. 建仓库(若已存在则跳过)
    st, _ = api("POST", "https://api.github.com/user/repos",
                {"name": REPO, "description": "国誉博2026上海现场指南", "private": False, "has_wiki": False})
    if st not in (201, 422):
        sys.exit("创建仓库失败")
    print("仓库确认:", f"{u}/{REPO}")
    # 2. 上传所有文件
    files = []
    for root, _, names in os.walk(HERE):
        if ".github" in root or ".git" in root:
            continue
        for n in names:
            if n in ("build.py","template.html","data.json","gh_token.txt"):
                continue
            p = os.path.join(root, n)
            rel = os.path.relpath(p, HERE).replace("\\", "/")
            files.append((rel, p))
    # workflow
    wf = os.path.join(HERE, ".github", "workflows", "pages.yml")
    files.append((".github/workflows/pages.yml", wf))
    # readme
    rd = os.path.join(HERE, "README.md")
    if os.path.exists(rd):
        files.append(("README.md", rd))

    files.sort()
    print("待上传文件数:", len(files))
    mime_guess = {"html":"text/html; charset=utf-8", "md":"text/plain; charset=utf-8",
                  "jpg":"image/jpeg","jpeg":"image/jpeg","png":"image/png",
                  "webp":"image/webp","yml":"text/plain; charset=utf-8","gif":"image/gif"}
    n = 0
    for rel, path in files:
        data = open(path, "rb").read()
        b64 = base64.b64encode(data).decode()
        ext = os.path.splitext(path)[1].lower()
        url = "https://api.github.com/repos/%s/%s/contents/%s" % (u, REPO, urllib.parse.quote(rel, safe="/"))
        payload = {"message": f"add {rel}", "content": b64,
                   "content_type": mime_guess.get(ext, "application/octet-stream")}
        st, _ = api("PUT", url, payload)
        n += 1
        if st not in (201, 200, 409):  # 409 = 已存在/冲突, 继续
            pass
    print("文件上传完成:", n)
    # 3. 开启 Pages(GitHub Actions)
    st, _ = api("POST", f"https://api.github.com/repos/{u}/{REPO}/pages", {"build_type": "workflow"})
    if st not in (201, 200, 409, 422):
        # 已开启就设置 source
        api("PUT", f"https://api.github.com/repos/{u}/{REPO}/pages", {"build_type": "workflow"})
    print("*"*50)
    print("部署触发完成! 预计 1-3 分钟后生效")
    print("手机访问: https://%s.github.io/%s/" % (u, REPO))

if __name__ == "__main__":
    main()