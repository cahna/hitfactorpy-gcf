import json

import functions_framework
from hitfactorpy.parsers.match_report.pandas import parse_match_report
from pydantic.json import pydantic_encoder

@functions_framework.http
def http_main(request):
    """HTTP Cloud Function.
    Args:
       request (flask.Request): The request object.
       <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
       The response text, or any set of values that can be turned into a
       Response object using `make_response`
       <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
    """
    request_body = request.get_data(as_text=True)
    match_report = parse_match_report(request_body)
    return json.dumps(match_report, default=pydantic_encoder)

