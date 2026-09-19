PATTERN_TO_INDEX = {
    'title': 0,
    'end': 1,
    '1text': 2,
    '2text': 3,
    '3text': 4,
    '4text': 5,
}

def choose_slide(prs, pattern):
    print(f"\n正在提取目标页: {pattern}")
    index = PATTERN_TO_INDEX[pattern]
    for i in range(len(prs.slides) - 1, -1, -1):
        if i != index:
            prs.slides._sldIdLst.remove(prs.slides._sldIdLst[i])
    print(f"成功提取目标页: {pattern}")
    return prs