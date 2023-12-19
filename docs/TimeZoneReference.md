# TimeZoneReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.time_zone_reference import TimeZoneReference

# TODO update the JSON string below
json = "{}"
# create an instance of TimeZoneReference from a JSON string
time_zone_reference_instance = TimeZoneReference.from_json(json)
# print the JSON string representation of the object
print TimeZoneReference.to_json()

# convert the object into a dict
time_zone_reference_dict = time_zone_reference_instance.to_dict()
# create an instance of TimeZoneReference from a dict
time_zone_reference_form_dict = time_zone_reference.from_dict(time_zone_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


