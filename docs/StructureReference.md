# StructureReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.structure_reference import StructureReference

# TODO update the JSON string below
json = "{}"
# create an instance of StructureReference from a JSON string
structure_reference_instance = StructureReference.from_json(json)
# print the JSON string representation of the object
print StructureReference.to_json()

# convert the object into a dict
structure_reference_dict = structure_reference_instance.to_dict()
# create an instance of StructureReference from a dict
structure_reference_form_dict = structure_reference.from_dict(structure_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


