# CommunicationType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**android_xref** | **str** |  Max length: 50; | [optional] 
**default_flag** | **bool** |  | [optional] 
**description** | **str** |  | 
**email_flag** | **bool** | Gets or sets at least one flag is required to be true -- phone, fax, or email. | [optional] 
**exchange_xref** | **str** |  Max length: 50; | [optional] 
**fax_flag** | **bool** | Gets or sets at least one flag is required to be true -- phone, fax, or email. | [optional] 
**google_xref** | **str** |  Max length: 50; | [optional] 
**id** | **int** |  | [optional] 
**iphone_xref** | **str** |  Max length: 50; | [optional] 
**phone_flag** | **bool** | Gets or sets at least one flag is required to be true -- phone, fax, or email. | [optional] 

## Example

```python
from connectwise_psa.models.communication_type import CommunicationType

# TODO update the JSON string below
json = "{}"
# create an instance of CommunicationType from a JSON string
communication_type_instance = CommunicationType.from_json(json)
# print the JSON string representation of the object
print CommunicationType.to_json()

# convert the object into a dict
communication_type_dict = communication_type_instance.to_dict()
# create an instance of CommunicationType from a dict
communication_type_form_dict = communication_type.from_dict(communication_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


