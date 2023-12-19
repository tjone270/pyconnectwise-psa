# WorkTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.work_type_reference import WorkTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of WorkTypeReference from a JSON string
work_type_reference_instance = WorkTypeReference.from_json(json)
# print the JSON string representation of the object
print WorkTypeReference.to_json()

# convert the object into a dict
work_type_reference_dict = work_type_reference_instance.to_dict()
# create an instance of WorkTypeReference from a dict
work_type_reference_form_dict = work_type_reference.from_dict(work_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


