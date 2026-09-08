PATTERN_TO_INDEX = {
    'title': 0,
    'end': 1,
    'contents': 2,
    'content': 3,
    '1text': 4,
    '2text': 5,
    '3text': 6,
    '4text': 7,
}

def choose_slide(prs, pattern):
    print(f"\n正在提取目标页: {pattern}")
    index = PATTERN_TO_INDEX[pattern]
    for i in range(len(prs.slides) - 1, -1, -1):
        if i != index:
            prs.slides._sldIdLst.remove(prs.slides._sldIdLst[i])
    print(f"成功提取目标页: {pattern}")
    return prs