import sys

from arg_parser import parse_args
from template_loader import load_template
from slide_chooser import choose_slide
from text_replacer import replace_text
from log_creater import create_log

def main():
    cmd = " ".join(sys.argv)
    args = parse_args()
    prs = load_template()
    new_prs = choose_slide(prs, args.pattern)
    final_prs = replace_text(new_prs, args)

    print(f"\n正在保存到: {args.output}")

    try:
        final_prs.save(args.output)
        print(f"保存成功！请打开 {args.output} 查看结果。")
        create_log(cmd, 0, args.output)
        return 0
    except Exception as e:
        print(f"保存失败: {e}")
        create_log(cmd, 1, e)
        return 1

if __name__ == "__main__":
    sys.exit(main())