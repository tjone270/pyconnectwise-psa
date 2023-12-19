# ActivityTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.activity_type_reference import ActivityTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityTypeReference from a JSON string
activity_type_reference_instance = ActivityTypeReference.from_json(json)
# print the JSON string representation of the object
print ActivityTypeReference.to_json()

# convert the object into a dict
activity_type_reference_dict = activity_type_reference_instance.to_dict()
# create an instance of ActivityTypeReference from a dict
activity_type_reference_form_dict = activity_type_reference.from_dict(activity_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


