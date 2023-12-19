# MySecurity


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_level** | **str** |  | [optional] 
**custom_flag** | **bool** |  | [optional] 
**delete_level** | **str** |  | [optional] 
**edit_level** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inquire_level** | **str** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**module_description** | **str** |  | [optional] 
**module_function_description** | **str** |  | [optional] 
**module_function_identifier** | **str** |  | [optional] 
**module_function_name** | **str** |  | [optional] 
**module_identifier** | **str** |  | [optional] 
**module_name** | **str** |  | [optional] 
**my_all_flag** | **bool** |  | [optional] 
**report_flag** | **bool** |  | [optional] 
**restrict_flag** | **bool** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.my_security import MySecurity

# TODO update the JSON string below
json = "{}"
# create an instance of MySecurity from a JSON string
my_security_instance = MySecurity.from_json(json)
# print the JSON string representation of the object
print MySecurity.to_json()

# convert the object into a dict
my_security_dict = my_security_instance.to_dict()
# create an instance of MySecurity from a dict
my_security_form_dict = my_security.from_dict(my_security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


