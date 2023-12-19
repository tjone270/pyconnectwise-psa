# CampaignStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 100; | 

## Example

```python
from connectwise_psa.models.campaign_status import CampaignStatus

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignStatus from a JSON string
campaign_status_instance = CampaignStatus.from_json(json)
# print the JSON string representation of the object
print CampaignStatus.to_json()

# convert the object into a dict
campaign_status_dict = campaign_status_instance.to_dict()
# create an instance of CampaignStatus from a dict
campaign_status_form_dict = campaign_status.from_dict(campaign_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


