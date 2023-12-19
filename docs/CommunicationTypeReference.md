# CommunicationTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.communication_type_reference import CommunicationTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationTypeReference from a JSON string
communication_type_reference_instance = CommunicationTypeReference.from_json(json)
# print the JSON string representation of the object
print CommunicationTypeReference.to_json()

# convert the object into a dict
communication_type_reference_dict = communication_type_reference_instance.to_dict()
# create an instance of CommunicationTypeReference from a dict
communication_type_reference_form_dict = communication_type_reference.from_dict(communication_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


