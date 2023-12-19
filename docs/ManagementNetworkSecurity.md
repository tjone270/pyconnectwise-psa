# ManagementNetworkSecurity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**password** | **str** |  Max length: 50; | [optional] 
**site** | **str** |  Max length: 100; | 
**username** | **str** |  Max length: 50; | [optional] 

## Example

```python
from connectwise_psa.models.management_network_security import ManagementNetworkSecurity

# TODO update the JSON string below
json = "{}"
# create an instance of ManagementNetworkSecurity from a JSON string
management_network_security_instance = ManagementNetworkSecurity.from_json(json)
# print the JSON string representation of the object
print ManagementNetworkSecurity.to_json()

# convert the object into a dict
management_network_security_dict = management_network_security_instance.to_dict()
# create an instance of ManagementNetworkSecurity from a dict
management_network_security_form_dict = management_network_security.from_dict(management_network_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


