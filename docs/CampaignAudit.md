# CampaignAudit


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** |  | [optional] 
**created_by** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**documents_created** | **int** |  | [optional] 
**email_subject** | **str** |  Max length: 1000; | [optional] 
**emails_sent** | **int** |  | 
**emails_unsent** | **int** |  | [optional] 
**group** | [**GroupReference**](GroupReference.md) |  | [optional] 
**id** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.campaign_audit import CampaignAudit

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignAudit from a JSON string
campaign_audit_instance = CampaignAudit.from_json(json)
# print the JSON string representation of the object
print CampaignAudit.to_json()

# convert the object into a dict
campaign_audit_dict = campaign_audit_instance.to_dict()
# create an instance of CampaignAudit from a dict
campaign_audit_form_dict = campaign_audit.from_dict(campaign_audit_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


