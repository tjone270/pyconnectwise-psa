# OwnershipType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 200; | 

## Example

```python
from connectwise_psa.models.ownership_type import OwnershipType

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipType from a JSON string
ownership_type_instance = OwnershipType.from_json(json)
# print the JSON string representation of the object
print OwnershipType.to_json()

# convert the object into a dict
ownership_type_dict = ownership_type_instance.to_dict()
# create an instance of OwnershipType from a dict
ownership_type_form_dict = ownership_type.from_dict(ownership_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


