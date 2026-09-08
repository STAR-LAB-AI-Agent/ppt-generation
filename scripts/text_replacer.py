def replace_text(prs, args):
    print("\n正在替换文本...")

    replacements = {
        '页面标题': getattr(args, 'title', None),
        '正文标题1': getattr(args, 'title1', None),
        '正文1': getattr(args, 'text1', None),
        '正文标题2': getattr(args, 'title2', None),
        '正文2': getattr(args, 'text2', None),
        '正文标题3': getattr(args, 'title3', None),
        '正文3': getattr(args, 'text3', None),
        '正文标题4': getattr(args, 'title4', None),
        '正文4': getattr(args, 'text4', None),
    }

    slide = prs.slides[0]
    for shape in slide.shapes:
        if shape.name in replacements:
            shape.text_frame.paragraphs[0].runs[0].text = replacements[shape.name]

    print("替换完成")
    return prs