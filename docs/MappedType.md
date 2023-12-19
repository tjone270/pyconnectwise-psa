# MappedType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gl_type** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**rec_id_field** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 
**table** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.mapped_type import MappedType

# TODO update the JSON string below
json = "{}"
# create an instance of MappedType from a JSON string
mapped_type_instance = MappedType.from_json(json)
# print the JSON string representation of the object
print MappedType.to_json()

# convert the object into a dict
mapped_type_dict = mapped_type_instance.to_dict()
# create an instance of MappedType from a dict
mapped_type_form_dict = mapped_type.from_dict(mapped_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


