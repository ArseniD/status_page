from argparse import ArgumentParser


def create_parser():
    parser = ArgumentParser(description="""
    Create events and incidents on the cashet server
    """)
    parser.add_argument('path', help="the path to the log file")
    return parser
