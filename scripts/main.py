import sys

from arg_parser import parse_args
from template_loader import load_template
from slide_chooser import choose_slide
from text_replacer import replace_text

def main():
    args = parse_args()
    prs = load_template(args.template)
    new_prs = choose_slide(prs, args.pattern)
    final_prs = replace_text(new_prs, args)

    print(f"\n正在保存到: {args.output}")

    try:
        final_prs.save(args.output)
        print(f"保存成功！请打开 {args.output} 查看结果。")
        return 0
    except Exception as e:
        print(f"保存失败: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())