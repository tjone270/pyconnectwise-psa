# ApiMember


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**block_cost_flag** | **bool** |  | [optional] 
**block_price_flag** | **bool** |  | [optional] 
**default_department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**email_address** | **str** |  Max length: 250; | [optional] 
**excluded_service_board_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  Max length: 15; | 
**inactive_date** | **datetime** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 30; Required On Updates; | [optional] 
**notes** | **str** |  | [optional] 
**sales_default_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**security_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**security_role** | [**SecurityRoleReference**](SecurityRoleReference.md) |  | [optional] 
**service_default_board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**structure_level** | [**StructureReference**](StructureReference.md) |  | [optional] 
**time_zone** | [**TimeZoneSetupReference**](TimeZoneSetupReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.api_member import ApiMember

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMember from a JSON string
api_member_instance = ApiMember.from_json(json)
# print the JSON string representation of the object
print ApiMember.to_json()

# convert the object into a dict
api_member_dict = api_member_instance.to_dict()
# create an instance of ApiMember from a dict
api_member_form_dict = api_member.from_dict(api_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


