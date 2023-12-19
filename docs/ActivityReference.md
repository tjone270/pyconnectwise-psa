# ActivityReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.activity_reference import ActivityReference

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityReference from a JSON string
activity_reference_instance = ActivityReference.from_json(json)
# print the JSON string representation of the object
print ActivityReference.to_json()

# convert the object into a dict
activity_reference_dict = activity_reference_instance.to_dict()
# create an instance of ActivityReference from a dict
activity_reference_form_dict = activity_reference.from_dict(activity_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


