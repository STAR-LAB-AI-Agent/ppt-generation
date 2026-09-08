from pptx import Presentation

def load_template(template_path):
    print(f"\n正在加载模板: {template_path}")

    try:
        prs = Presentation(template_path)
        print(f"加载成功！模板总页数: {len(prs.slides)}")
        return prs
    except Exception as e:
        print(f"加载失败: {e}")
        return None