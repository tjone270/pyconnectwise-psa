# Campaign


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**actual_cost** | **float** |  | [optional] 
**actual_gross_margin** | **float** |  | [optional] 
**actual_roi** | **float** |  | [optional] 
**actual_revenue** | **float** |  | [optional] 
**budget_cost** | **float** |  | [optional] 
**budget_gross_margin** | **float** |  | [optional] 
**budget_roi** | **float** |  | [optional] 
**budget_revenue** | **float** |  | [optional] 
**default_group** | [**GroupReference**](GroupReference.md) |  | [optional] 
**emails_sent** | **int** |  | [optional] 
**end_date** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**impressions** | **int** |  | [optional] 
**inactive** | **bool** |  | [optional] 
**inactive_days_after_end** | **int** |  | [optional] 
**location_id** | **int** |  | [optional] 
**marketing_manager_default_track_id** | **int** |  | [optional] 
**member** | [**MemberReference**](MemberReference.md) |  | [optional] 
**name** | **str** |  Max length: 50; | 
**notes** | **str** |  | [optional] 
**opportunity_default_track_id** | **int** |  | [optional] 
**start_date** | **datetime** |  | 
**status** | [**CampaignStatusReference**](CampaignStatusReference.md) |  | [optional] 
**sub_type** | [**CampaignSubTypeReference**](CampaignSubTypeReference.md) |  | [optional] 
**type** | [**CampaignTypeReference**](CampaignTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.campaign import Campaign

# TODO update the JSON string below
json = "{}"
# create an instance of Campaign from a JSON string
campaign_instance = Campaign.from_json(json)
# print the JSON string representation of the object
print Campaign.to_json()

# convert the object into a dict
campaign_dict = campaign_instance.to_dict()
# create an instance of Campaign from a dict
campaign_form_dict = campaign.from_dict(campaign_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


