# EntityTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.entity_type_reference import EntityTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTypeReference from a JSON string
entity_type_reference_instance = EntityTypeReference.from_json(json)
# print the JSON string representation of the object
print EntityTypeReference.to_json()

# convert the object into a dict
entity_type_reference_dict = entity_type_reference_instance.to_dict()
# create an instance of EntityTypeReference from a dict
entity_type_reference_form_dict = entity_type_reference.from_dict(entity_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


