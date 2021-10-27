import sys
import typing

import googleapiclient.discovery
import google.cloud.compute_v1 as compute_v1

ZONE_NAME = "us-central1-b"
PROJECT_NAME = "minun-projekti-328712"
IMAGE_NAME = "ubuntu-1604-lts"
INSTANCE_TYPE = "n1-standard-1"
INSTANCE_NAME = "my-instance"
compute = googleapiclient.discovery.build("compute", "v1")

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


# create instance
def create_instance1(
    project_id: str,
    zone: str,
    instance_name: str,
    machine_type: str = "n1-standard-1",
    source_image: str = "projects/debian-cloud/global/images/family/debian-10",
    network_name: str = "global/networks/default",
) -> compute_v1.Instance:
    """
    Send an instance creation request to the Compute Engine API and wait for it to complete.
    Args:
        project_id: project ID or project number of the Cloud project you want to use.
        zone: name of the zone you want to use. For example: “us-west3-b”
        instance_name: name of the new virtual machine.
        machine_type: machine type of the VM being created. This value uses the
            following format: "zones/{zone}/machineTypes/{type_name}".
            For example: "zones/europe-west3-c/machineTypes/f1-micro"
        source_image: path to the operating system image to mount on your boot
            disk. This can be one of the public images
            (like "projects/debian-cloud/global/images/family/debian-10")
            or a private image you have access to.
        network_name: name of the network you want the new instance to use.
            For example: "global/networks/default" represents the `default`
            network interface, which is created automatically for each project.
    Returns:
        Instance object.
    """
    instance_client = compute_v1.InstancesClient()
    operation_client = compute_v1.ZoneOperationsClient()

    # Describe the size and source image of the boot disk to attach to the instance.
    disk = compute_v1.AttachedDisk()
    initialize_params = compute_v1.AttachedDiskInitializeParams()
    initialize_params.source_image = (
        source_image  # "projects/debian-cloud/global/images/family/debian-10"
    )
    initialize_params.disk_size_gb = 10
    disk.initialize_params = initialize_params
    disk.auto_delete = True
    disk.boot = True
    disk.type_ = compute_v1.AttachedDisk.Type.PERSISTENT

    # Use the network interface provided in the network_name argument.
    network_interface = compute_v1.NetworkInterface()
    network_interface.name = network_name

    # Collect information into the Instance object.
    instance = compute_v1.Instance()
    instance.name = instance_name
    instance.disks = [disk]
    full_machine_type_name = f"zones/{zone}/machineTypes/{machine_type}"
    instance.machine_type = full_machine_type_name
    instance.network_interfaces = [network_interface]

    # Prepare the request to insert an instance.
    request = compute_v1.InsertInstanceRequest()
    request.zone = zone
    request.project = project_id
    request.instance_resource = instance

    # Wait for the create operation to complete.
    print(f"Creating the {instance_name} instance in {zone}...")
    operation = instance_client.insert(request=request)
    while operation.status != compute_v1.Operation.Status.DONE:
        operation = operation_client.wait(
            operation=operation.name, zone=zone, project=project_id
        )
    if operation.error:
        print("Error during creation:", operation.error, file=sys.stderr)
    if operation.warnings:
        print("Warning during creation:", operation.warnings, file=sys.stderr)
    print(f"Instance {instance_name} created.")
    return instance


def stop_instance(instance_id):
    """
    Stop a Compute Engine VM instance
    """

    print('Stopping VM instance ...')
    print('Instance Id: ' + instance_id)

    # Stop VM instance
    compute.instances().stop(
          project=PROJECT_NAME,
          zone=ZONE_NAME,
          instance=INSTANCE_NAME).execute()

    return


def start_instance(instance_id):
    """
    Start a Compute Engine VM instance
    """

    print('Starting VM instance ...')
    print('Instance Id: ' + instance_id)

    # Start VM instance
    compute.instances().start(
          project=PROJECT_NAME,
          zone=ZONE_NAME,
          instance=INSTANCE_NAME).execute()

    return


