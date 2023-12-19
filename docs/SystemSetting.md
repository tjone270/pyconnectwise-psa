# SystemSetting


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**value** | **str** |  | 
**value_type** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.system_setting import SystemSetting

# TODO update the JSON string below
json = "{}"
# create an instance of SystemSetting from a JSON string
system_setting_instance = SystemSetting.from_json(json)
# print the JSON string representation of the object
print SystemSetting.to_json()

# convert the object into a dict
system_setting_dict = system_setting_instance.to_dict()
# create an instance of SystemSetting from a dict
system_setting_form_dict = system_setting.from_dict(system_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


