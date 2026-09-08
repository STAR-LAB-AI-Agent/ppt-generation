# ppt-generator — 文案自动生成 PPT 技能

一个用 Python 实现的「文案 → PPT」自动化工具/Skill：把 **1～4 段**「小标题 + 正文」填入
北京理工大学答辩/汇报模板（`BIT-template.pptx`），一次生成**一页**指定版式的 `.pptx`。
本项目同时是一个集成真实 Python 开源项目 [`python-pptx`](https://python-pptx.readthedocs.io/)
的课程作业示例。

> 随技能附带的文件组织：
> - 技能代码：`scripts/`
> - 模板：`templates/BIT-template.pptx`
> - 依赖库列表：`requirements.txt`

---

## 1. 项目简介

`ppt-generator` 提供一条命令把文案变成排好版的 PPT 页面。它读取一个现成的 PPT 模板，
按所选的版式**只保留对应的一页**，把模板占位符（`页面标题`、`正文标题N`、`正文N`）换成
你传入的文案，最后另存为新的 `.pptx`。

支持的页面版式与文案形态：

| 文案段数 | 子命令 | 占位/页面特征 |
|---------|--------|-------------|
| 一段 | `1text` | 1 个小标题 + 1 段正文 |
| 两段 | `2text` | 2 个小标题 + 2 段正文 |
| 三段 | `3text` | 3 个小标题 + 3 段正文 |
| 四段 | `4text` | 4 个小标题 + 4 段正文 |

底层完全基于 [python-pptx](https://python-pptx.readthedocs.io/) 
完成模板加载、页面筛选与文本替换。

---

## 2. 用户场景

适合把一段到四段文字快速做成整齐一页 PPT 的场景，例如：

- **答辩 / 汇报页**：把「研究背景 / 研究意义 / 结论」等要点各成一段，快速出页；
- **要点 / 总结页**：章节要点归纳为 3～4 段，保持统一版式；
- **批量排版**：内容来自数据或模板，用脚本统一排版，避免手工逐页调整。

一次调用 = 一页。若需整套 PPT，可多次调用后将各页合并到同一演示文稿。

---

## 3. 安装方法

需要 Python 3.8+，且在 Python 3.12 上开发并实测通过。

项目唯一运行依赖是 `python-pptx`，版本为 `1.0.2`：

```bash
pip install python-pptx==1.0.2
```

或通过本仓库的 `requirements.txt` 安装：

```bash
pip install -r requirements.txt
```

### 关于模板

`templates/BIT-template.pptx` 随技能目录一起提供，
**无需手动配置路径**。拷贝技能时请拷贝整个技能根目录并保持子文件夹相对结构。

---

## 4. 运行方法

主入口为技能目录下的 `scripts/main.py`。通用命令结构：

```text
python scripts/main.py -o <输出>.pptx <子命令> <--title> <--titleN> <--textN>...
```

### 关键运行约束

1. **`-o / -t` 必须写在子命令之前**。
2. **建议总用 `-o` 指定输出路径与文件名**，避免覆盖上次结果。

---

## 5. 工具 / Skill 使用方式

### 5.1 命令行方式

可选参数：
- -o/--output: 指定输出路径与文件名，默认为 `output.pptx` 。
- -t/--template: 指定模板文件路径，默认为自带模板。

下表给出各段数必须的参数：

| 子命令 | 必填参数 |
|--------|---------|
| `1text` | `--title --title1 --text1` |
| `2text` | `--title --title1 --text1 --title2 --text2` |
| `3text` | `--title --title1 --text1 --title2 --text2 --title3 --text3` |
| `4text` | `--title --title1 --text1 --title2 --text2 --title3 --text3 --title4 --text4` |

参数语义：
- `--title`：页面标题，应简短表明该页讲什么；
- `--titleN`：第 N 段小标题，几个字即可；
- `--textN`：第 N 段正文。

### 5.2 正文长度上限

每段正文不得超过下表（实测值,超出易溢出版面）：

| 子命令 | 每段正文上限 |
|--------|------------|
| `1text` | 180 字 |
| `2text` | 90 字 |
| `3text` | 60 字 |
| `4text` | 80 字 |

### 5.3 运行示例

**一段文字**：

```text
python scripts/main.py -o page_1text.pptx 1text --title "课程概述" --title1 "概述" --text1 "本课程系统介绍人工智能的核心概念、发展历程与典型应用场景，帮助学习者建立完整认知。"
```

**两段文字**：

```text
python scripts/main.py -o page_2text.pptx 2text --title "研究背景与意义" --title1 "研究背景" --text1 "深度学习在图像识别等任务上已取得重大突破。" --title2 "研究意义" --text2 "自动化工具可显著提升文档生产与演示效率。"
```

输出文件 `.pptx` 用 PowerPoint / WPS 等打开即可查看。

### 5.4 作为 Skill（给 Agent）使用

`ppt-generator` 也被注册为 Skill，供智能体侧按同一套子命令生成页面。
当出现"把 1～4 段文案做成 PPT 页"类任务时，Agent 参照 SKILL.md：选定子命令 → 组织
`--title`/`--titleN`/`--textN` → 用 5.1–5.2 的限制与约束调用脚本。本 README 面向安装与运维；
写给 Agent 的行为指令见技能附带的 `SKILL.md`。

---

## 6. 开源依赖及许可证

本项目集成并使用的开源项目为：

### python-pptx (MIT License)
- **项目名称**：python-pptx
- **版本**：`1.0.2`
- **许可证**：**MIT License**
- **官方主页**：https://python-pptx.readthedocs.io/ （源仓库：https://github.com/scanny/python-pptx）
- **实际使用方式**：
  - `pptx.Presentation()`：加载/新建演示文稿（`scripts/template_loader.py`）；
  - `prs.slides` / `_sldIdLst`：统计并筛选模板页面（`scripts/slide_chooser.py`）；
  - `shape.text_frame.paragraphs[0].runs[0].text`：定位并替换文本（`scripts/text_replacer.py`）；
  - `prs.save(path)`：另存生成结果（`scripts/main.py`）。

- （python-pptx 自身还依赖 `lxml`、`Pillow`、`XlsxWriter`、`typing_extensions` 等，
  由 pip 自动解析，均为各自开源许可，如对许可证合规有严格要求请一并核对。）

---

## 7. 测试方法

### 7.1 环境自检
```bash
python -c "import pptx; print(pptx.__version__)"   # 期望 1.0.2
python scripts/main.py --help                        # 期望列出 title/1text..4text 子命令
```

### 7.2 脚本功能测试（四种版式各生成一页）
在技能根目录执行：
```bash
python scripts/main.py -o _t1.pptx 1text --title "T" --title1 "A" --text1 "一"
python scripts/main.py -o _t2.pptx 2text --title "T" --title1 "A" --text1 "一" --title2 "B" --text2 "二"
python scripts/main.py -o _t3.pptx 3text --title "T" --title1 "A" --text1 "一" --title2 "B" --text2 "二" --title3 "C" --text3 "三"
python scripts/main.py -o _t4.pptx 4text --title "T" --title1 "A" --text1 "一" --title2 "B" --text2 "二" --title3 "C" --text3 "三" --title4 "D" --text4 "四"
```

### 7.3 Skill 功能测试
将Skill导入Agent框架后，使用 `/ppt-generator` 显式调用工具以测试工具是否正常运行，
输入与 `生成PPT` 相关的提示词以测试 Agent 是否能正常识别任务关键词。

---

## 8. 已知问题

- **一次仅一页**：每次调用只输出模板中被选中的那一页（脚本会裁掉其余 7 页）。做整套 PPT
  需多次调用再自行合并，或扩展脚本支持多页。
- **模板占位是名称匹配**：替换依赖模板中 shape 的名称（`页面标题`/`正文标题N`/`正文N`）。
  若换用其它模板，需保证占位 shape 命名一致，否则不会被替换。