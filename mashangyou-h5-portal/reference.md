# 码上游样式 H5 · 参考细节

## 标杆链接

https://4680264.ma3you.cn/html/content_show/index.html?v=20250213&article_id=benJjYN#/

打开后重点看：

| 元素 | 做法 |
|------|------|
| 背景 | 深蓝 + 细点纹理 |
| 标题 | 居中白字 |
| 模块标题 | 黄色胶囊条（黑边） |
| 视频 | 标题下通栏播放器 |
| 文档/PPT | 多页 JPG **首尾相接**竖滑，无外框 |

## HTML 骨架（精简）

```html
<div class="page">
  <div class="brand-bar">…logo + hcci…</div>
  <h1 class="page-title">…</h1>
  <details class="toc">…</details>

  <section class="block" id="v1">
    <div class="badge-wrap"><div class="badge">标题</div></div>
    <div class="media">
      <video controls playsinline preload="metadata" src="media/xxx.mp4"></video>
    </div>
  </section>

  <section class="block block-ppt" id="d1">
    <div class="badge-wrap"><div class="badge">专题标题</div></div>
    <div class="ppt-stack">
      <img src="media/ppt-docs/xxx/01.jpg" alt="" loading="lazy" />
      <img src="media/ppt-docs/xxx/02.jpg" alt="" loading="lazy" />
    </div>
  </section>
</div>
```

## 关键 CSS 要点

```css
.badge {
  background: #f5c400;
  color: #693c00;
  border: 3px solid #111;
  border-radius: 999px;
  box-shadow: 4px 5px 0 #111;
  font-weight: 700;
}
/* 禁止 .badge::before 做一排装饰小点 */

.block-ppt { width: 100%; }
.ppt-stack { line-height: 0; font-size: 0; }
.ppt-stack img {
  display: block;
  width: 100%;
  margin: 0;
  padding: 0;
  border: 0;
}
```

## 部署命令

```bash
tcb env list
tcb hosting deploy "<本地v1目录>" <独立cloudPath> -e <你们的envId> --concurrency 8
```

预览域名以控制台「静态网站托管」为准。成品参考：  
https://satisfaction-portal-d0bjcfbf4087-1468353816.tcloudbaseapp.com/fire-month-2026/

## 成例模块顺序（消防月）

1. 消防宣传月主题宣传片（视频）  
2. 烟雾蔓延逃生系统演示（视频）  
3. 火灾逃生误区（视频）  
4. 厂房火灾应急逃生（视频）  
5. 专题科普 · 火灾分类（PPT 竖拼）  
6. 专题科普 · 灭火方式选择及使用（PPT 竖拼）  
7. 专题科普 · 空呼 / 防毒面具使用（PPT 竖拼）  
8. 2026火灾事故案例警示（PPT 竖拼）  
