# PatchOperation


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**op** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from connectwise_psa.models.patch_operation import PatchOperation

# TODO update the JSON string below
json = "{}"
# create an instance of PatchOperation from a JSON string
patch_operation_instance = PatchOperation.from_json(json)
# print the JSON string representation of the object
print PatchOperation.to_json()

# convert the object into a dict
patch_operation_dict = patch_operation_instance.to_dict()
# create an instance of PatchOperation from a dict
patch_operation_form_dict = patch_operation.from_dict(patch_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


