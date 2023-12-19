# NotifyTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.notify_type_reference import NotifyTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of NotifyTypeReference from a JSON string
notify_type_reference_instance = NotifyTypeReference.from_json(json)
# print the JSON string representation of the object
print NotifyTypeReference.to_json()

# convert the object into a dict
notify_type_reference_dict = notify_type_reference_instance.to_dict()
# create an instance of NotifyTypeReference from a dict
notify_type_reference_form_dict = notify_type_reference.from_dict(notify_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


