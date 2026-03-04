# Portfolio

个人作品集站点，静态 HTML 页面 + 本地 HTTP 服务。

## 环境要求

- **Python 3**（系统自带即可，无需额外安装依赖）

## 使用 Cursor 启动（推荐）

用 Cursor 打开本项目后，在 AI 对话里输入下面任一提示词，让 Cursor 帮你启动本地服务器：

- **中文**：`帮我本地部署一下这个项目，我需要本地服务器来访问`
- **英文**：`Start the local server for this project so I can access it in the browser`

Cursor 会在项目目录执行 `python3 server.py` 并说明访问地址（默认 http://localhost:8000/）。

---

## 拉取与启动

### 1. 克隆项目

```bash
git clone <仓库地址>
cd portfolio
```

### 2. 启动本地服务器

在项目根目录执行：

```bash
python3 server.py
```

终端会保持运行，无需其他操作。

### 3. 在浏览器中访问

打开浏览器访问：

- **http://localhost:8000/**
- 或 **http://127.0.0.1:8000/**

即可查看站点。修改 `index.html`、`HK01.html`、`eatojpy.html` 等文件后，刷新页面即可看到效果。

### 4. 停止服务器

在运行 `python3 server.py` 的终端中按 **Ctrl + C** 停止服务。

## 项目说明

- **端口**：默认使用 **8000**，如需修改请编辑 `server.py` 最后一行的 `port=8000`。
- **路由**：未匹配到文件或目录的路径会回退到 `index.html`，适合前端路由或直接访问子页面（如 `/HK01.html`、`/eatojpy.html`）。
- **无需安装依赖**：仅使用 Python 标准库，无需 `pip install` 或 `npm install`。

## 修改内容

直接编辑项目中的 HTML、CSS、JS 或资源文件，保存后在浏览器中刷新即可。若已开启服务器，无需重启。
