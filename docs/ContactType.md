# ContactType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**description** | **str** |  Max length: 50; | 
**id** | **int** |  | [optional] 
**service_alert_flag** | **bool** |  | [optional] 
**service_alert_message** | **str** |  Max length: 150; | [optional] 

## Example

```python
from connectwise_psa.models.contact_type import ContactType

# TODO update the JSON string below
json = "{}"
# create an instance of ContactType from a JSON string
contact_type_instance = ContactType.from_json(json)
# print the JSON string representation of the object
print ContactType.to_json()

# convert the object into a dict
contact_type_dict = contact_type_instance.to_dict()
# create an instance of ContactType from a dict
contact_type_form_dict = contact_type.from_dict(contact_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


