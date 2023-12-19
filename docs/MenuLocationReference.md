# MenuLocationReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.menu_location_reference import MenuLocationReference

# TODO update the JSON string below
json = "{}"
# create an instance of MenuLocationReference from a JSON string
menu_location_reference_instance = MenuLocationReference.from_json(json)
# print the JSON string representation of the object
print MenuLocationReference.to_json()

# convert the object into a dict
menu_location_reference_dict = menu_location_reference_instance.to_dict()
# create an instance of MenuLocationReference from a dict
menu_location_reference_form_dict = menu_location_reference.from_dict(menu_location_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


