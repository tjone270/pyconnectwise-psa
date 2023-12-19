# AddressFormat


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_all_countries** | **bool** |  | [optional] 
**country_ids** | **List[int]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**format** | **str** |  Max length: 250; | 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**remove_all_countries** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.address_format import AddressFormat

# TODO update the JSON string below
json = "{}"
# create an instance of AddressFormat from a JSON string
address_format_instance = AddressFormat.from_json(json)
# print the JSON string representation of the object
print AddressFormat.to_json()

# convert the object into a dict
address_format_dict = address_format_instance.to_dict()
# create an instance of AddressFormat from a dict
address_format_form_dict = address_format.from_dict(address_format_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


