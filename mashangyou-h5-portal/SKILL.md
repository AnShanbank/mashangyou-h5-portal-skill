---
name: mashangyou-h5-portal
description: >-
  按「码上游」单页竖滑 H5 样式，把视频、PPT/课件做成可扫码学习的宣传门户，
  并可部署到腾讯云 CloudBase 静态托管。在用户提到码上游、H5 宣传页、竖滑专题、
  消防宣传门户、内容展示页、借鉴 ma3you 链接、课件拼接上线，或要给同事发预览链接时使用。
---

# 码上游样式 H5 宣传门户

把 **视频 + PPT 课件** 做成手机友好的单页竖滑门户，视觉与交互对齐码上游内容页，自建静态站部署（不依赖码上游平台）。

## 必看参考（先打开再仿）

**样式标杆**（布局/黄标/视频嵌入/PPT 竖拼）：  
https://4680264.ma3you.cn/html/content_show/index.html?v=20250213&article_id=benJjYN#/

用浏览器打开后确认：

1. 深蓝纹理底 + 居中白标题  
2. 每个模块：**黄色圆角标题条** → 紧接下方媒体  
3. 视频：HTML5 `<video controls>` 通栏  
4. PPT：**每一页导出成图，竖向紧密拼接**，无白边框、无翻页条、无下载栏装饰  
5. 页头可放品牌：公司 Logo（深底用白字）+ HCCI 圆环

成品示例：  
https://satisfaction-portal-d0bjcfbf4087-1468353816.tcloudbaseapp.com/fire-month-2026/

技能仓库（安装与说明）：见本技能所在 GitHub 仓库 `README.md`。

## 何时用本技能

- 「按这个链接格式做一版」并丢码上游 / ma3you 链接  
- 消防月、安全宣贯、专题科普等多视频 + 多课件要上线预览  
- 要把文件夹里的 `.mp4` / `.pptx` 做成同事可打开的链接  

若用户只要策划方案、不要 H5，不走本技能。

## 工作流（按序执行）

```
进度：
- [ ] 1. 打开参考链接，对齐模块顺序与样式要点
- [ ] 2. 收集素材：视频、PPT、Logo
- [ ] 3. PPT → 页图（竖拼用）
- [ ] 4. 写 index.html（码上游结构）
- [ ] 5. 本地 serve 预览
- [ ] 6. （可选）tcb hosting 部署，把链接发给用户
```

### 1. 对齐参考页

用浏览器打开标杆链接，记下模块标题顺序。用户给的本地文件名优先。

### 2. 素材落盘

在用户指定目录下建：

```text
{活动名}/v1-码上游样式/
  index.html
  media/
    *.mp4
    logo-white.png
    hcci-ring.png
    ppt-docs/{专题短名}/01.jpg …
  部署说明.md
```

Logo：用户自备，或使用技能仓库里的 `logo样例/logo-white.png`、`logo样例/hcci-ring.png`。

EHS 对外文案称 **EHS部**，不要写「安全环保部」。对应支柱默认 **HCCI「卓越安全」**。

### 3. PPT 导出为页图

Windows + PowerPoint + `pywin32`：

```bash
python "%USERPROFILE%\.cursor\skills\mashangyou-h5-portal\scripts\export_pptx_pages.py" ^
  --pptx "路径/某课件.pptx" ^
  --out "路径/v1-码上游样式/media/ppt-docs/短名" ^
  --width 1200
```

若技能装在项目内，把脚本路径改成项目里的  
`.cursor/skills/mashangyou-h5-portal/scripts/export_pptx_pages.py`。

规则：

- 每个 PPT 单独子目录；`01.jpg` 起连续编号  
- **整页竖拼**，不要「上一页/下一页」小窗  
- 不要白卡片边框、圆角外框、翻页条  

无 PowerPoint：先转 PDF，再用 PyMuPDF 渲 JPG（宽度 ≥ 1200）。

### 4. 写页面（结构约束）

`品牌条 → 大标题 →（可选目录）→ 重复「黄标 + 媒体」→ 页脚`

- 视频：`黄标 + <video controls playsinline>`  
- 课件：`黄标 + .ppt-stack` 连续 `<img>`，宽 100%，图间距 0  
- 同时只播一个视频  
- 不要码上游底栏「该内容由用户自行制作」；页脚写事业部 / 运营部×EHS部 / HCCI  
- 黄标：`#f5c400`、深棕字、黑描边；**不要**黄标上方装饰小白点  

骨架见 [reference.md](reference.md)。

### 5. 本地预览

```bash
npx --yes serve "…/v1-码上游样式" -l 5179
```

勿用 `file://`。

### 6. 部署腾讯云（可选）

本机已登录 `tcb` 时：

```bash
tcb hosting deploy "本地/v1-码上游样式目录" <独立cloudPath> -e <你们的envId> --concurrency 8
```

- **必须换独立 cloudPath**，避免覆盖他人站点  
- 首次可能有「确定访问」提示  
- 改版加 `?v=时间戳` 防缓存  

若同事未配置云账号：只交付本地目录 + 预览方式即可。

## 用户一句话模板

```text
按码上游样式做 H5 宣传页，参考：
https://4680264.ma3you.cn/html/content_show/index.html?v=20250213&article_id=benJjYN#/
素材在：{文件夹路径}
视频和 PPT 都放进去；PPT 要大图竖向紧密拼接、不要边框。
做好部署（或本地预览）并给我链接。
```

## 验收清单

- [ ] 结构像参考链接：黄标 + 通栏媒体竖滑  
- [ ] PPT 全宽竖拼、无翻页 UI、无多余边框  
- [ ] 有公司 Logo + HCCI（深色底用白字 Logo）  
- [ ] 手机宽度可读；长视频提示 Wi‑Fi  
- [ ] 已给出可打开的预览方式（本地或 HTTPS）  

## 更多

- [reference.md](reference.md)
