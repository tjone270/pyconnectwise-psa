# GenericNameIdDTO


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.generic_name_id_dto import GenericNameIdDTO

# TODO update the JSON string below
json = "{}"
# create an instance of GenericNameIdDTO from a JSON string
generic_name_id_dto_instance = GenericNameIdDTO.from_json(json)
# print the JSON string representation of the object
print GenericNameIdDTO.to_json()

# convert the object into a dict
generic_name_id_dto_dict = generic_name_id_dto_instance.to_dict()
# create an instance of GenericNameIdDTO from a dict
generic_name_id_dto_form_dict = generic_name_id_dto.from_dict(generic_name_id_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


