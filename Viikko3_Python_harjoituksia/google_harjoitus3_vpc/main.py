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


def list_firewalls():
    request = service.firewalls().list(project="minun-projekti-328712")
    while request is not None:
        response = request.execute()

        for firewall in response['items']:
            # TODO: Change code below to process each `firewall` resource:
            pprint(firewall)

        request = service.firewalls().list_next(previous_request=request, previous_response=response)


def create_firewall():
    firewall_body = {
        "name": "python-firewall",
        "description": "python firewall rule",
        "network": "global/networks/python-vpc",
        "direction": "INGRESS",
        "sourceRanges": [
            "0.0.0.0/0"
        ],
        "priority": 1000,
        "allowed": [
            {
                "IPProtocol": "TCP",
                "ports": [
                    "80"
                ]
            }
        ]
    }

    request = service.firewalls().insert(project="minun-projekti-328712", body=firewall_body)
    response = request.execute()

    # TODO: Change code below to process the `response` dict:
    pprint(response)


create_firewall()