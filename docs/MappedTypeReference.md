# MappedTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.mapped_type_reference import MappedTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of MappedTypeReference from a JSON string
mapped_type_reference_instance = MappedTypeReference.from_json(json)
# print the JSON string representation of the object
print MappedTypeReference.to_json()

# convert the object into a dict
mapped_type_reference_dict = mapped_type_reference_instance.to_dict()
# create an instance of MappedTypeReference from a dict
mapped_type_reference_form_dict = mapped_type_reference.from_dict(mapped_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


