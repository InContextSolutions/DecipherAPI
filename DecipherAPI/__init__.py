import simplejson as json
import dateutil.parser
import DecipherAPI.client


def list_command(args):
    client = DecipherAPI.client.Client(
        args.username, args.password, host=args.host)
    result = client.list_surveys(fmt=args.fmt)
    if args.fmt == 'json':
        print(json.dumps(result))
    else:
        print(result)


def pull_command(args):
    client = DecipherAPI.client.Client(
        args.username, args.password, host=args.host)
    start_t = args.start
    if start_t:
        start_t = dateutil.parser.parse(start_t)
    end_t = args.end
    if end_t:
        end_t = dateutil.parser.parse(end_t)
    columns = args.columns
    if columns:
        columns = columns.split(',')
    filters = args.filters
    if filters:
        filters = filters.split(',')
    result = client.get_survey(args.survey, start=start_t, end=end_t,
                               status=args.status, columns=columns, filters=filters, fmt=args.fmt)
    if result:
        if args.fmt == 'json':
            print(json.dumps(result))
        else:
            print(result)
    else:
        print("no data")


def cli():
    import argparse

    desc = """A command-line utility for interacting with the Decipher API.
    Help is available on subcommands (e.g. `DecipherAPI.pull --help`)"""

    parser = argparse.ArgumentParser(description=desc)
    subparsers = parser.add_subparsers(title='valid subcommands')

    parser.add_argument(
        "-U", "--username", help="user identification", type=str, required=True)
    parser.add_argument(
        "-P", "--password", help="user password", type=str, required=True)
    parser.add_argument(
        "-H", "--host", help="host", default=DecipherAPI.client.DEFAULT_HOST, type=str)

    # pull command
    pull_parser = subparsers.add_parser('pull', help='pull survey data')
    pull_parser.add_argument(
        "-s", "--survey", help="survey name", type=str, required=True)
    pull_parser.add_argument(
        "-t", "--start", help="utc start time: YYYY-MM-DDTHH:MM:SS.mmmmmm", type=str)
    pull_parser.add_argument(
        "-T", "--end", help="utc end time: YYYY-MM-DDTHH:MM:SS.mmmmmm", type=str)
    pull_parser.add_argument("-S", "--status", help="survey status", choices=[
                             'all', 'partial', 'complete', 'qualified', 'terminated', 'overquota'], type=str)
    pull_parser.add_argument("-c", "--columns", help="include columns", type=str)
    pull_parser.add_argument(
        "-F", "--filters", help="filter columns", type=str)
    pull_parser.add_argument(
        "-f", "--fmt", help="return format", choices=["json", "tsv", "csv"], default="json", type=str)
    pull_parser.set_defaults(func=pull_command)

    # list command
    list_parser = subparsers.add_parser('list', help='list surveys')
    list_parser.add_argument(
        "-f", "--fmt", help="return format", choices=["json", "tsv", "csv"], default="json", type=str)
    list_parser.set_defaults(func=list_command)

    args = parser.parse_args()
    args.func(args)
