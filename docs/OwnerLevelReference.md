# OwnerLevelReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.owner_level_reference import OwnerLevelReference

# TODO update the JSON string below
json = "{}"
# create an instance of OwnerLevelReference from a JSON string
owner_level_reference_instance = OwnerLevelReference.from_json(json)
# print the JSON string representation of the object
print OwnerLevelReference.to_json()

# convert the object into a dict
owner_level_reference_dict = owner_level_reference_instance.to_dict()
# create an instance of OwnerLevelReference from a dict
owner_level_reference_form_dict = owner_level_reference.from_dict(owner_level_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


