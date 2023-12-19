# GroupReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.group_reference import GroupReference

# TODO update the JSON string below
json = "{}"
# create an instance of GroupReference from a JSON string
group_reference_instance = GroupReference.from_json(json)
# print the JSON string representation of the object
print GroupReference.to_json()

# convert the object into a dict
group_reference_dict = group_reference_instance.to_dict()
# create an instance of GroupReference from a dict
group_reference_form_dict = group_reference.from_dict(group_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


