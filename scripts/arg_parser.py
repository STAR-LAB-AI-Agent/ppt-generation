import argparse

def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-o', '--output',
        type=str,
        default='./output.pptx',
    )

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

    title = argparse.ArgumentParser(add_help=False)
    title.add_argument(
        '--title',
        type=str,
        required=True,
    )
    title.add_argument(
        '--name',
        type=str,
        required=True,
    )
    title.add_argument(
        '--teacher',
        type=str,
        required=True,
    )

    subparsers = parser.add_subparsers(dest='pattern', required=True)

    parser_title = subparsers.add_parser('title', parents=[title])
    parser_end = subparsers.add_parser('end', parents=[title])

    parser_1text = subparsers.add_parser('1text', parents=[ntext])
    parser_2text = subparsers.add_parser('2text', parents=[ntext])
    parser_3text = subparsers.add_parser('3text', parents=[ntext])
    parser_4text = subparsers.add_parser('4text', parents=[ntext])
    return parser.parse_args()