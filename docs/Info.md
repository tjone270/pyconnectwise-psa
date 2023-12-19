# Info


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_region** | **str** |  | [optional] 
**is_cloud** | **bool** |  | [optional] 
**license_bits** | [**List[LicenseBit]**](LicenseBit.md) |  | [optional] 
**server_time_zone** | **str** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.info import Info

# TODO update the JSON string below
json = "{}"
# create an instance of Info from a JSON string
info_instance = Info.from_json(json)
# print the JSON string representation of the object
print Info.to_json()

# convert the object into a dict
info_dict = info_instance.to_dict()
# create an instance of Info from a dict
info_form_dict = info.from_dict(info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


