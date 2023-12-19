# MySecurityCustomizeItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**customize_identifier** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**item_identifier** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.my_security_customize_item import MySecurityCustomizeItem

# TODO update the JSON string below
json = "{}"
# create an instance of MySecurityCustomizeItem from a JSON string
my_security_customize_item_instance = MySecurityCustomizeItem.from_json(json)
# print the JSON string representation of the object
print MySecurityCustomizeItem.to_json()

# convert the object into a dict
my_security_customize_item_dict = my_security_customize_item_instance.to_dict()
# create an instance of MySecurityCustomizeItem from a dict
my_security_customize_item_form_dict = my_security_customize_item.from_dict(my_security_customize_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


