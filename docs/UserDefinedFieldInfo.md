# UserDefinedFieldInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**business_unit_ids** | **List[int]** | List of business unit ids using custom field | [optional] 
**button_url** | **str** | Only available with Button Field Type. Required when entryTypeIdentifier is button | [optional] 
**caption** | **str** | Field caption | [optional] 
**date_created** | **str** | Date in UTC the custom field was created | [optional] 
**display_on_screen_flag** | **bool** |  | [optional] 
**entry_type_identifier** | **str** |  | [optional] 
**field_type_identifier** | **str** |  | [optional] 
**help_text** | **str** | Help text to accompany the custom field | [optional] 
**id** | **int** | ID of the custom user defined field | [optional] 
**list_view_flag** | **bool** | Denotes that this custom field is included on a list view | [optional] 
**location_ids** | **List[int]** | List of locations ids using custom field | [optional] 
**number_decimals** | **int** | Only valid for Number or percent | [optional] 
**options** | [**List[UserDefinedFieldOption]**](UserDefinedFieldOption.md) |  | [optional] 
**pod_id** | **int** | Id of the Pod where the custom field will be placed | [optional] 
**read_only_flag** | **bool** |  | [optional] 
**required_flag** | **bool** |  | [optional] 
**sequence_number** | **int** | Must be between 1 and 500.  This defines the order in which the custom fields will appear | [optional] 

## Example

```python
from connectwise_psa.models.user_defined_field_info import UserDefinedFieldInfo

# TODO update the JSON string below
json = "{}"
# create an instance of UserDefinedFieldInfo from a JSON string
user_defined_field_info_instance = UserDefinedFieldInfo.from_json(json)
# print the JSON string representation of the object
print UserDefinedFieldInfo.to_json()

# convert the object into a dict
user_defined_field_info_dict = user_defined_field_info_instance.to_dict()
# create an instance of UserDefinedFieldInfo from a dict
user_defined_field_info_form_dict = user_defined_field_info.from_dict(user_defined_field_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


