# TicketSync


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**integrator_login** | [**IntegratorLoginReference**](IntegratorLoginReference.md) |  | [optional] 
**internal_analysis_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 80; | 
**password** | **str** |  | [optional] 
**problem_description_flag** | **bool** |  | [optional] 
**psg** | **str** |  | [optional] 
**resolution_flag** | **bool** |  | [optional] 
**url** | **str** |  | 
**user_name** | **str** |  | [optional] 
**vendor_type** | **str** |  | 

## Example

```python
from connectwise_psa.models.ticket_sync import TicketSync

# TODO update the JSON string below
json = "{}"
# create an instance of TicketSync from a JSON string
ticket_sync_instance = TicketSync.from_json(json)
# print the JSON string representation of the object
print TicketSync.to_json()

# convert the object into a dict
ticket_sync_dict = ticket_sync_instance.to_dict()
# create an instance of TicketSync from a dict
ticket_sync_form_dict = ticket_sync.from_dict(ticket_sync_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


