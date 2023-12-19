# PersonasInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.personas_info import PersonasInfo

# TODO update the JSON string below
json = "{}"
# create an instance of PersonasInfo from a JSON string
personas_info_instance = PersonasInfo.from_json(json)
# print the JSON string representation of the object
print PersonasInfo.to_json()

# convert the object into a dict
personas_info_dict = personas_info_instance.to_dict()
# create an instance of PersonasInfo from a dict
personas_info_form_dict = personas_info.from_dict(personas_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


