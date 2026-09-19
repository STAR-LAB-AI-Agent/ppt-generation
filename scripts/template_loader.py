from pptx import Presentation
from pathlib import Path

TEMPLATE_PATH = Path(__file__).parent.parent / "templates" / "BIT-template.pptx"

def load_template():
    print(f"\n正在加载模板: {TEMPLATE_PATH}")

    try:
        prs = Presentation(TEMPLATE_PATH)
        print(f"加载成功！模板总页数: {len(prs.slides)}")
        return prs
    except Exception as e:
        print(f"加载失败: {e}")
        return None