# Test script for sending multiple async requests to the CSE 130 httpserver.
# src: https://github.com/ross/requests-futures

from requests_futures.sessions import FuturesSession

# Constants --------------------------------------------------------------------

__url = 'http://localhost:8080'

__request_objects = [
    {'type': 'GET', 'target_filename': 'filename_27_char11111111111'},
    {'type': 'GET', 'target_filename': 'filename_27_char11111111112'},
]

# Main -------------------------------------------------------------------------

def main():

    session = FuturesSession()
    live_requests = []

    print("starting threads...")

    # make requests
    for req in __request_objects:
        request_params = {'request-target': req.target_filename}
        future_request = session.get(__url, params=request_params)
        live_requests.push(future_request)

    print("\nwaiting for results...")

    # print results
    for req in live_requests:
        response = req.result()
        print('response one status: {0}'.format(response.status_code))
        print(response.content)
        print("\n")

# Run --------------------------------------------------------------------------

if (__name__ == '__main__'):
    main()
