# Country


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**address_format** | [**AddressFormatReference**](AddressFormatReference.md) |  | [optional] 
**city_caption** | **str** |  Max length: 25; | [optional] 
**core_entity_country_code** | **str** |  | [optional] 
**country_code** | **str** |  Max length: 2; | [optional] 
**currency** | [**CurrencyReference**](CurrencyReference.md) |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**dialing_prefix** | **str** |  Max length: 5; | [optional] 
**id** | **int** |  | [optional] 
**localization_caption_one** | **str** |  Max length: 25; | [optional] 
**localization_value_one** | **str** |  Max length: 50; | [optional] 
**name** | **str** |  Max length: 50; | 
**state_caption** | **str** |  Max length: 25; | [optional] 
**zip_caption** | **str** |  Max length: 25; | [optional] 
**zip_minimum_length** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.country import Country

# TODO update the JSON string below
json = "{}"
# create an instance of Country from a JSON string
country_instance = Country.from_json(json)
# print the JSON string representation of the object
print Country.to_json()

# convert the object into a dict
country_dict = country_instance.to_dict()
# create an instance of Country from a dict
country_form_dict = country.from_dict(country_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


