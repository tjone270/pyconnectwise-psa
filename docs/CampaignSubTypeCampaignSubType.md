# CampaignSubTypeCampaignSubType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 100; | 
**type** | [**CampaignTypeReference**](CampaignTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.campaign_sub_type_campaign_sub_type import CampaignSubTypeCampaignSubType

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignSubTypeCampaignSubType from a JSON string
campaign_sub_type_campaign_sub_type_instance = CampaignSubTypeCampaignSubType.from_json(json)
# print the JSON string representation of the object
print CampaignSubTypeCampaignSubType.to_json()

# convert the object into a dict
campaign_sub_type_campaign_sub_type_dict = campaign_sub_type_campaign_sub_type_instance.to_dict()
# create an instance of CampaignSubTypeCampaignSubType from a dict
campaign_sub_type_campaign_sub_type_form_dict = campaign_sub_type_campaign_sub_type.from_dict(campaign_sub_type_campaign_sub_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


