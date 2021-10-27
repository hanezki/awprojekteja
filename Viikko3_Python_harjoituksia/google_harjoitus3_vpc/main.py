from pprint import pprint

from googleapiclient import discovery

service = discovery.build("compute", "v1")


def list_networks():
    project = "minun-projekti-328712"

    request = service.networks().list(project=project)
    while request is not None:
        response = request.execute()

        for network in response["items"]:
            pprint(network)

        request = service.networks().list_next(previous_request=request, previous_response=response)


def create_vpc():
    network_body = {
        "name": "python-vpc",
        "autoCreateSubnetworks": True,
        "description": "juukeli",
        "mtu": 1430,
        "routingConfig": {
            "routingMode": "GLOBAL"
        }
    }

    request = service.networks().insert(project="minun-projekti-328712", body=network_body)
    response = request.execute()

    pprint(response)


create_vpc()