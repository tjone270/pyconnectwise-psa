# LocaleReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.locale_reference import LocaleReference

# TODO update the JSON string below
json = "{}"
# create an instance of LocaleReference from a JSON string
locale_reference_instance = LocaleReference.from_json(json)
# print the JSON string representation of the object
print LocaleReference.to_json()

# convert the object into a dict
locale_reference_dict = locale_reference_instance.to_dict()
# create an instance of LocaleReference from a dict
locale_reference_form_dict = locale_reference.from_dict(locale_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


