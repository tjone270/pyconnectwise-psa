# CountryReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.country_reference import CountryReference

# TODO update the JSON string below
json = "{}"
# create an instance of CountryReference from a JSON string
country_reference_instance = CountryReference.from_json(json)
# print the JSON string representation of the object
print CountryReference.to_json()

# convert the object into a dict
country_reference_dict = country_reference_instance.to_dict()
# create an instance of CountryReference from a dict
country_reference_form_dict = country_reference.from_dict(country_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


