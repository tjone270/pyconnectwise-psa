# CountryInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**city_caption** | **str** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**dialing_prefix** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**localization_caption_one** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**state_caption** | **str** |  | [optional] 
**zip_caption** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.country_info import CountryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CountryInfo from a JSON string
country_info_instance = CountryInfo.from_json(json)
# print the JSON string representation of the object
print CountryInfo.to_json()

# convert the object into a dict
country_info_dict = country_info_instance.to_dict()
# create an instance of CountryInfo from a dict
country_info_form_dict = country_info.from_dict(country_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


