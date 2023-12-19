# LocaleInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**locale_code** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.locale_info import LocaleInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LocaleInfo from a JSON string
locale_info_instance = LocaleInfo.from_json(json)
# print the JSON string representation of the object
print LocaleInfo.to_json()

# convert the object into a dict
locale_info_dict = locale_info_instance.to_dict()
# create an instance of LocaleInfo from a dict
locale_info_form_dict = locale_info.from_dict(locale_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


