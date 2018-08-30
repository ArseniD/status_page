import pytest

from status_page import cli


@pytest.fixture
def parser():
    return cli.create_parser()


def test_parser_without_log_path(parser):
    """
    Without a specified log file parser will exit
    """
    with pytest.raises(SystemExit):
        parser.parse_args([])


def test_parser_with_path_argument(parser):
    """
    The parser will not exit if it receives a path as an argument
    """
    args = parser.parse_args(['/opt/logs/daily_check.log'])
    assert args.path == '/opt/logs/daily_check.log'
