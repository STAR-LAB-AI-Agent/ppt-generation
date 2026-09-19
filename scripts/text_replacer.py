def replace_text(prs, args):
    print("\n正在替换文本...")

    names = ['页面标题', '正文标题1', '正文标题2', '正文标题3', '正文标题4', '正文1', '正文2', '正文3', '正文4']
    title = getattr(args, 'title', '')
    name = getattr(args, 'name', '')
    teacher = getattr(args, 'teacher', '')
    subtitles = getattr(args, 'subtitles', [])
    texts = getattr(args, 'texts', [])

    replacements = {names[0]: title}
    for keys, lst in [(names[1:5], subtitles), (names[5:9], texts)]:
        for i, key in enumerate(keys):
            replacements[key] = lst[i] if i < len(lst) else ''

    slide = prs.slides[0]
    for shape in slide.shapes:
        if shape.name in replacements:
            shape.text_frame.paragraphs[0].runs[0].text = replacements[shape.name]
        if shape.name == '个人信息':
            shape.text_frame.paragraphs[0].runs[0].text = shape.text_frame.paragraphs[0].runs[0].text.replace("北小理", name)
            shape.text_frame.paragraphs[1].runs[0].text = shape.text_frame.paragraphs[1].runs[0].text.replace("京小工", teacher)

    print("替换完成")
    return prs