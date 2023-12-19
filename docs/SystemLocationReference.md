# SystemLocationReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.system_location_reference import SystemLocationReference

# TODO update the JSON string below
json = "{}"
# create an instance of SystemLocationReference from a JSON string
system_location_reference_instance = SystemLocationReference.from_json(json)
# print the JSON string representation of the object
print SystemLocationReference.to_json()

# convert the object into a dict
system_location_reference_dict = system_location_reference_instance.to_dict()
# create an instance of SystemLocationReference from a dict
system_location_reference_form_dict = system_location_reference.from_dict(system_location_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


