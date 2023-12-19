# ActivityStatusReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.activity_status_reference import ActivityStatusReference

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityStatusReference from a JSON string
activity_status_reference_instance = ActivityStatusReference.from_json(json)
# print the JSON string representation of the object
print ActivityStatusReference.to_json()

# convert the object into a dict
activity_status_reference_dict = activity_status_reference_instance.to_dict()
# create an instance of ActivityStatusReference from a dict
activity_status_reference_form_dict = activity_status_reference.from_dict(activity_status_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


