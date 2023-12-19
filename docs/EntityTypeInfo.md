# EntityTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.entity_type_info import EntityTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EntityTypeInfo from a JSON string
entity_type_info_instance = EntityTypeInfo.from_json(json)
# print the JSON string representation of the object
print EntityTypeInfo.to_json()

# convert the object into a dict
entity_type_info_dict = entity_type_info_instance.to_dict()
# create an instance of EntityTypeInfo from a dict
entity_type_info_form_dict = entity_type_info.from_dict(entity_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


