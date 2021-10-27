import sys
import typing

import googleapiclient.discovery

ZONE_NAME = "us-west4-b"
PROJECT_NAME = "minun-projekti-328712"
IMAGE_NAME = ""
IMAGE_PROJECT_NAME = ""
INSTANCE_TYPE = ""
INSTANCE_NAME = ""
compute = googleapiclient.discovery.build("compute", "v1")
import google.cloud.compute_v1 as compute_v1
#list in a specific zone
def list_instances(project_id, zone):


    print("Listing VM instances...")

    # Describe instances
    response = compute.instances().list(project=project_id, zone=zone).execute()
    print(f"Instances in project: {project_id}")
    if response.get("items"):
        for instance in response["items"]:
            print(f"Id: {instance['id']}")
            print(f"Name: {instance['name']}")
            print(f"Status: {instance['status']}")
            print(f"Machine type: {instance['machineType']}")
    else:
        print("No instances")


def list_all_instances(project_id):
    instance_client = compute_v1.InstancesClient()
    request = compute_v1.AggregatedListInstancesRequest(project=project_id, max_results=20)
    agg_list = instance_client.aggregated_list(request=request)
    all_instances = {}
    print("Instances found:")

    for zone, response in agg_list:
        if response.instances:
            all_instances[zone] = response.instances
            print(f"{zone}:")
            for instance in response.instances:
                print(f"{instance.name} ({instance.machine_type})")
    return all_instances

