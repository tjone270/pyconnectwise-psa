# ContactTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**service_alert_flag** | **bool** |  | [optional] 
**service_alert_message** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.contact_type_info import ContactTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ContactTypeInfo from a JSON string
contact_type_info_instance = ContactTypeInfo.from_json(json)
# print the JSON string representation of the object
print ContactTypeInfo.to_json()

# convert the object into a dict
contact_type_info_dict = contact_type_info_instance.to_dict()
# create an instance of ContactTypeInfo from a dict
contact_type_info_form_dict = contact_type_info.from_dict(contact_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


