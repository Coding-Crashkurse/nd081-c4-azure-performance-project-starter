from azure.identity import DefaultAzureCredential
from azure.mgmt.compute import ComputeManagementClient

# Define the parameters
resource_group_name = 'acdnd-c4-project'
vmss_name = 'udacity-vmss'
new_capacity = 8

# Use DefaultAzureCredential to authenticate
# Make sure to set environment variables AZURE_CLIENT_ID, AZURE_CLIENT_SECRET, AZURE_TENANT_ID
# with the appropriate values for your Service Principal
credential = DefaultAzureCredential()

# Create ComputeManagementClient
compute_client = ComputeManagementClient(credential, 'd66cf093-0353-4ee3-bc60-6c7e86772153')

# Get VMSS
vmss = compute_client.virtual_machine_scale_sets.get(resource_group_name, vmss_name)

# Update capacity
vmss.sku.capacity = new_capacity

# Apply the update
compute_client.virtual_machine_scale_sets.begin_create_or_update(resource_group_name, vmss_name, vmss)
