# Location


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**calendar** | [**CalendarReference**](CalendarReference.md) |  | [optional] 
**client_flag** | **bool** |  | [optional] 
**department_ids** | **List[int]** |  | [optional] 
**id** | **int** |  | [optional] 
**location_flag** | **bool** |  | [optional] 
**manager** | [**MemberReference**](MemberReference.md) |  | [optional] 
**name** | **str** |  Max length: 50; | 
**override_address_line1** | **str** |  Max length: 50; | [optional] 
**override_address_line2** | **str** |  Max length: 50; | [optional] 
**override_city** | **str** |  Max length: 50; | [optional] 
**override_country** | [**CountryReference**](CountryReference.md) |  | [optional] 
**override_fax_number** | **str** |  Max length: 15; | [optional] 
**override_phone_number** | **str** |  Max length: 15; | [optional] 
**override_state** | **str** |  Max length: 50; | [optional] 
**override_zip** | **str** |  Max length: 12; | [optional] 
**owa_url** | **str** |  Max length: 100; | [optional] 
**owner_level_id** | **int** |  | [optional] 
**payroll_xref** | **str** |  Max length: 10; | [optional] 
**reports_to** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**sales_rep** | **str** |  Max length: 50; | [optional] 
**structure_level** | [**CorporateStructureLevelReference**](CorporateStructureLevelReference.md) |  | [optional] 
**time_zone_setup** | [**TimeZoneSetupReference**](TimeZoneSetupReference.md) |  | [optional] 
**work_role_ids** | **List[int]** |  | [optional] 

## Example

```python
from connectwise_psa.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print Location.to_json()

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_form_dict = location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


