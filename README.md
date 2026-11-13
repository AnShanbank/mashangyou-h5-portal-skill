# 码上游样式 H5 宣传门户 · Cursor Agent Skill

把视频、PPT 做成手机竖滑宣传页（样式对齐「码上游」内容页），并可选部署到腾讯云静态托管。

## 样式参考（必看）

https://4680264.ma3you.cn/html/content_show/index.html?v=20250213&article_id=benJjYN#/

成品示例（消防宣传月）：  
https://satisfaction-portal-d0bjcfbf4087-1468353816.tcloudbaseapp.com/fire-month-2026/

## 同事怎么用（没有精益文化仓库也可以）

### 1. 安装技能到 Cursor

**推荐：个人技能（所有项目可用）**

```powershell
# 克隆本仓库到任意目录，例如 Desktop
git clone https://github.com/AnShanbank/mashangyou-h5-portal-skill.git

# 复制技能文件夹到 Cursor 个人 skills
$src = ".\mashangyou-h5-portal-skill\mashangyou-h5-portal"
$dst = "$env:USERPROFILE\.cursor\skills\mashangyou-h5-portal"
New-Item -ItemType Directory -Force -Path "$env:USERPROFILE\.cursor\skills" | Out-Null
Copy-Item -Recurse -Force $src $dst
```

装好后应存在：`%USERPROFILE%\.cursor\skills\mashangyou-h5-portal\SKILL.md`

然后**新开一个 Agent 对话**。

### 2. 跟 Agent 说

```text
用 mashangyou-h5-portal 技能，按码上游样式做 H5 宣传页。
参考：https://4680264.ma3you.cn/html/content_show/index.html?v=20250213&article_id=benJjYN#/
素材在：{你的视频和PPT文件夹}
PPT 大图竖向紧密拼接、不要边框；页头放公司 Logo 和 HCCI。
做好本地预览；若已登录 tcb，部署并给我链接。
```

也可以让 Agent 先读本仓库：

```text
先阅读 https://github.com/AnShanbank/mashangyou-h5-portal-skill 里的技能说明，再按码上游样式做 H5。
```

### 3. 本机依赖（做一次）

| 依赖 | 用途 |
|------|------|
| Cursor Agent | 执行技能 |
| Microsoft PowerPoint | PPT 导出页图 |
| Python + `pywin32` | `pip install pywin32` |
| （可选）`@cloudbase/cli` / `tcb` | 一键部署预览 |

Logo 样例在仓库 `logo样例/`（可直接拷进页面 `media/`）。

## 仓库结构

```text
mashangyou-h5-portal/     ← 复制到 ~/.cursor/skills/ 的技能本体
  SKILL.md
  reference.md
  scripts/export_pptx_pages.py
logo样例/
README.md                 ← 本说明
```

## 说明

- 技能不依赖「精益文化」业务仓库；素材路径由你本地提供即可。  
- 腾讯云部署需本机已登录 `tcb`；环境 ID / 云路径按你们团队约定修改，勿覆盖他人站点。  
- 对外文案称 **EHS部**；默认对应 HCCI「卓越安全」。
