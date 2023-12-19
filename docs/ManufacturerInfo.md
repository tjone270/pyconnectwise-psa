# ManufacturerInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.manufacturer_info import ManufacturerInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ManufacturerInfo from a JSON string
manufacturer_info_instance = ManufacturerInfo.from_json(json)
# print the JSON string representation of the object
print ManufacturerInfo.to_json()

# convert the object into a dict
manufacturer_info_dict = manufacturer_info_instance.to_dict()
# create an instance of ManufacturerInfo from a dict
manufacturer_info_form_dict = manufacturer_info.from_dict(manufacturer_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


