---
name: ppt-generator
description: 将一段至四段文案填入北京理工大学 BIT 模板，生成一页指定版式的 PPT。
disable-model-invocation: false
user-invocable: true
---

# ppt-generator

把 1~4 段「小标题 + 正文」文案填入 PPT 模板，每次生成**一页**。目标模板为北京理工大学
答辩/汇报模板（BIT）。

## 何时使用

当任务需要"把一段到四段文字做成 PPT 页面"（如答辩页、总结页、要点页）且每段都可拆出
小标题与正文时使用。一次调用对应一页；若需多页需多次调用（本技能不支持一次拼多页）。

## 按段落数选择版式

| 文案段数 | 子命令 | 必填参数 |
|---------|--------|---------|
| 一段 | `1text` | `--title --title1 --text1` |
| 两段 | `2text` | `--title --title1 --text1 --title2 --text2` |
| 三段 | `3text` | `--title --title1 --text1 --title2 --text2 --title3 --text3` |
| 四段 | `4text` | `--title --title1 --text1 --title2 --text2 --title3 --text3 --title4 --text4` |

参数含义：
- `--title`：页面标题，表明整页主题，**不宜过长**。
- `--titleN`：第 N 段的小标题，**几个字概括即可**。
- `--textN`：第 N 段的正文。

## 正文长度上限

每段正文不得超过下列上限（超出易溢出版面），也不应字数过少（过少会使版面过于空旷）：

| 子命令 | 每段正文上限 |
|--------|------------|
| `1text` | 180 字 |
| `2text` | 90 字 |
| `3text` | 60 字 |
| `4text` | 80 字 |

## 命令结构

入口为技能内的 `scripts/main.py`。命令需在技能根目录下执行。要点：

- **`-o / -t` 必须写在子命令之前**；写在之后会报 unrecognized arguments。
- 未指定 `-o` 时输出到默认位置；建议总是显式给出输出路径与文件名。

```
python scripts/main.py -o "<输出路径>.pptx" <子命令> <参数...>
```

## 执行步骤

1. 依任务确定 1～4 段文案及其小标题、正文，据此选子命令。
2. 组装 `--title` 及各段 `--titleN` / `--textN`（正文不超上限）。
3. 以"运行示例"中的结构调用脚本，`-o` 放在子命令之前并给出输出文件路径。
4. 依据脚本输出确认成功。

## 运行示例

两段文字：

```text
python scripts/main.py -o page.pptx 2text --title "研究背景与意义" --title1 "研究背景" --text1 "深度学习在图像识别等任务上已取得重大突破。" --title2 "研究意义" --text2 "自动化工具可显著提升文档生产与演示效率。"
```

三段文字：

```text
python scripts/main.py -o arch.pptx 3text --title "系统架构设计" --title1 "输入层" --text1 "负责数据清洗与特征提取。" --title2 "处理层" --text2 "执行核心算法与业务逻辑。" --title3 "输出层" --text3 "汇总结果并生成可视化报告。"
```
