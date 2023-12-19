# OwnershipTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.ownership_type_info import OwnershipTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OwnershipTypeInfo from a JSON string
ownership_type_info_instance = OwnershipTypeInfo.from_json(json)
# print the JSON string representation of the object
print OwnershipTypeInfo.to_json()

# convert the object into a dict
ownership_type_info_dict = ownership_type_info_instance.to_dict()
# create an instance of OwnershipTypeInfo from a dict
ownership_type_info_form_dict = ownership_type_info.from_dict(ownership_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


