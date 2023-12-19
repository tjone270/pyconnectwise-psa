# CommunicationTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**email_flag** | **bool** |  | [optional] 
**fax_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**phone_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.communication_type_info import CommunicationTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationTypeInfo from a JSON string
communication_type_info_instance = CommunicationTypeInfo.from_json(json)
# print the JSON string representation of the object
print CommunicationTypeInfo.to_json()

# convert the object into a dict
communication_type_info_dict = communication_type_info_instance.to_dict()
# create an instance of CommunicationTypeInfo from a dict
communication_type_info_form_dict = communication_type_info.from_dict(communication_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


