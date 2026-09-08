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

    subparsers = parser.add_subparsers(dest='pattern')

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

    parser_1text = subparsers.add_parser('1text')
    parser_1text.add_argument(
        '--title',
        type=str,
        required=True,
    )
    parser_1text.add_argument(
        '--title1',
        type=str,
        required=True,
    )
    parser_1text.add_argument(
        '--text1',
        type=str,
        required=True,
    )

    parser_2text = subparsers.add_parser('2text')
    parser_2text.add_argument(
        '--title',
        type=str,
        required=True,
    )
    parser_2text.add_argument(
        '--title1',
        type=str,
        required=True,
    )
    parser_2text.add_argument(
        '--text1',
        type=str,
        required=True,
    )
    parser_2text.add_argument(
        '--title2',
        type=str,
        required=True,
    )
    parser_2text.add_argument(
        '--text2',
        type=str,
        required=True,
    )

    parser_3text = subparsers.add_parser('3text')
    parser_3text.add_argument(
        '--title',
        type=str,
        required=True,
    )
    parser_3text.add_argument(
        '--title1',
        type=str,
        required=True,
    )
    parser_3text.add_argument(
        '--text1',
        type=str,
        required=True,
    )
    parser_3text.add_argument(
        '--title2',
        type=str,
        required=True,
    )
    parser_3text.add_argument(
        '--text2',
        type=str,
        required=True,
    )
    parser_3text.add_argument(
        '--title3',
        type=str,
        required=True,
    )
    parser_3text.add_argument(
        '--text3',
        type=str,
        required=True,
    )

    parser_4text = subparsers.add_parser('4text')
    parser_4text.add_argument(
        '--title',
        type=str,
        required=True,
    )
    parser_4text.add_argument(
        '--title1',
        type=str,
        required=True,
    )
    parser_4text.add_argument(
        '--text1',
        type=str,
        required=True,
    )
    parser_4text.add_argument(
        '--title2',
        type=str,
        required=True,
    )
    parser_4text.add_argument(
        '--text2',
        type=str,
        required=True,
    )
    parser_4text.add_argument(
        '--title3',
        type=str,
        required=True,
    )
    parser_4text.add_argument(
        '--text3',
        type=str,
        required=True,
    )
    parser_4text.add_argument(
        '--title4',
        type=str,
        required=True,
    )
    parser_4text.add_argument(
        '--text4',
        type=str,
        required=True,
    )
    return parser.parse_args()