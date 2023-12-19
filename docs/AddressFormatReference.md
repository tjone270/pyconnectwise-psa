# AddressFormatReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.address_format_reference import AddressFormatReference

# TODO update the JSON string below
json = "{}"
# create an instance of AddressFormatReference from a JSON string
address_format_reference_instance = AddressFormatReference.from_json(json)
# print the JSON string representation of the object
print AddressFormatReference.to_json()

# convert the object into a dict
address_format_reference_dict = address_format_reference_instance.to_dict()
# create an instance of AddressFormatReference from a dict
address_format_reference_form_dict = address_format_reference.from_dict(address_format_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


