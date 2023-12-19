# Manager


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_enabled** | **bool** |  | [optional] 
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**contact_rec_id** | **int** |  | [optional] 
**country** | **str** |  | [optional] 
**date_entered_utc** | **datetime** |  | [optional] 
**department** | **str** |  | [optional] 
**directory_roles** | **List[str]** |  | [optional] 
**display_name** | **str** |  | [optional] 
**employee_type** | **str** |  | [optional] 
**entered_by** | **str** |  | [optional] 
**fax** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**groups** | **List[str]** |  | [optional] 
**id** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**last_update_utc** | **datetime** |  | [optional] 
**licenses** | [**List[M365License]**](M365License.md) |  | [optional] 
**mail** | **str** |  | [optional] 
**mail_nickname** | **str** |  | [optional] 
**manager** | [**Manager**](Manager.md) |  | [optional] 
**manager_id** | **str** |  | [optional] 
**manager_id** | **str** |  | [optional] 
**microsoft_365_contact_rec_id** | **int** |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**office** | **str** |  | [optional] 
**phone_number** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**principal_name** | **str** |  | [optional] 
**proxy_addresses** | **List[str]** |  | [optional] 
**state** | **str** |  | [optional] 
**tenant_id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**updated_by** | **str** |  | [optional] 
**usage_location** | **str** |  | [optional] 
**user_type** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.manager import Manager

# TODO update the JSON string below
json = "{}"
# create an instance of Manager from a JSON string
manager_instance = Manager.from_json(json)
# print the JSON string representation of the object
print Manager.to_json()

# convert the object into a dict
manager_dict = manager_instance.to_dict()
# create an instance of Manager from a dict
manager_form_dict = manager.from_dict(manager_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


