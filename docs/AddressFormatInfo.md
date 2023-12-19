# AddressFormatInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.address_format_info import AddressFormatInfo

# TODO update the JSON string below
json = "{}"
# create an instance of AddressFormatInfo from a JSON string
address_format_info_instance = AddressFormatInfo.from_json(json)
# print the JSON string representation of the object
print AddressFormatInfo.to_json()

# convert the object into a dict
address_format_info_dict = address_format_info_instance.to_dict()
# create an instance of AddressFormatInfo from a dict
address_format_info_form_dict = address_format_info.from_dict(address_format_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


