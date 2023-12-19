# UserDefinedField


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**add_all_business_units** | **bool** |  | [optional] 
**add_all_locations** | **bool** |  | [optional] 
**business_unit_ids** | **List[int]** |  | [optional] 
**button_url** | **str** | Only available with Button Field Type. Required when entryTypeIdentifier is button Max length: 1000; | [optional] 
**caption** | **str** | Field caption Max length: 25; | 
**date_created** | **datetime** | Date in UTC the custom field was created | [optional] 
**display_on_screen_flag** | **bool** |  | [optional] 
**entry_type_identifier** | **str** |  | [optional] 
**field_type_identifier** | **str** |  | 
**help_text** | **str** | Help text to accompany the custom field Max length: 1000; | [optional] 
**id** | **int** | ID of the custom user defined field | [optional] 
**list_view_flag** | **bool** | Denotes that this custom field is included on a list view | [optional] 
**location_ids** | **List[int]** |  | [optional] 
**number_decimals** | **int** | Only valid for Number or percent | [optional] 
**options** | [**List[UserDefinedFieldOption]**](UserDefinedFieldOption.md) |  | [optional] 
**pod_id** | **int** | Id of the Pod where the custom field will be placed | 
**read_only_flag** | **bool** |  | [optional] 
**remove_all_business_units** | **bool** |  | [optional] 
**remove_all_locations** | **bool** |  | [optional] 
**required_flag** | **bool** |  | [optional] 
**screen_id** | **str** | Field ScreenID Max length: 25; | [optional] 
**sequence_number** | **int** | Must be between 1 and 500.  This defines the order in which the custom fields will appear | 

## Example

```python
from connectwise_psa.models.user_defined_field import UserDefinedField

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefinedField from a JSON string
user_defined_field_instance = UserDefinedField.from_json(json)
# print the JSON string representation of the object
print UserDefinedField.to_json()

# convert the object into a dict
user_defined_field_dict = user_defined_field_instance.to_dict()
# create an instance of UserDefinedField from a dict
user_defined_field_form_dict = user_defined_field.from_dict(user_defined_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


