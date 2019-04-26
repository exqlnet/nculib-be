from flask_restful.reqparse import RequestParser, Argument


def add_args(args, location="json"):

    req_parser = RequestParser()
    for arg in args:
        req_parser.add_argument(
            name=arg[0],
            type=arg[1],
            required=arg[2],
            default=arg[3],
            help=arg[4],
            location=location
        )
    return req_parser
