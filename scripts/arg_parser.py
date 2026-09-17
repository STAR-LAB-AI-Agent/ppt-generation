import argparse
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser()

    default_template_path = Path(__file__).parent.parent / "templates" / "BIT-template.pptx"
    parser.add_argument(
        '-t', '--template',
        type=str,
        default=default_template_path,
    )

    parser.add_argument(
        '-o', '--output',
        type=str,
        default='./output.pptx',
    )

    subparsers = parser.add_subparsers(dest='pattern', required=True)

    ntext = argparse.ArgumentParser(add_help=False)
    ntext.add_argument(
        '--title',
        type=str,
        required=True,
    )
    ntext.add_argument(
        '--subtitles',
        nargs='+',
        type=str,
        required=True,
    )
    ntext.add_argument(
        '--texts',
        nargs='+',
        type=str,
        required=True,
    )

    parser_title = subparsers.add_parser('title')
    parser_title.add_argument(
        '--title',
        type=str,
        required=True,
    )
    parser_title.add_argument(
        '--name',
        type=str,
        required=True,
    )
    parser_title.add_argument(
        '--teacher',
        type=str,
        required=True,
    )

    parser_end = subparsers.add_parser('end')
    parser_end.add_argument(
        '--title',
        type=str,
        required=True,
    )
    parser_end.add_argument(
        '--name',
        type=str,
        required=True,
    )
    parser_end.add_argument(
        '--teacher',
        type=str,
        required=True,
    )

    parser_1text = subparsers.add_parser('1text', parents=[ntext])
    parser_2text = subparsers.add_parser('2text', parents=[ntext])
    parser_3text = subparsers.add_parser('3text', parents=[ntext])
    parser_4text = subparsers.add_parser('4text', parents=[ntext])
    return parser.parse_args()