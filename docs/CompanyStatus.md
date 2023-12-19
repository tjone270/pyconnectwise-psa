# CompanyStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**cancel_open_tracks_flag** | **bool** |  | [optional] 
**custom_note_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**disallow_saving_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**notification_message** | **str** |  Max length: 500; | [optional] 
**notify_flag** | **bool** |  | [optional] 
**track** | [**TrackReference**](TrackReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.company_status import CompanyStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CompanyStatus from a JSON string
company_status_instance = CompanyStatus.from_json(json)
# print the JSON string representation of the object
print CompanyStatus.to_json()

# convert the object into a dict
company_status_dict = company_status_instance.to_dict()
# create an instance of CompanyStatus from a dict
company_status_form_dict = company_status.from_dict(company_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


