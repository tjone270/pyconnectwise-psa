# CampaignType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 100; | 

## Example

```python
from connectwise_psa.models.campaign_type import CampaignType

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignType from a JSON string
campaign_type_instance = CampaignType.from_json(json)
# print the JSON string representation of the object
print CampaignType.to_json()

# convert the object into a dict
campaign_type_dict = campaign_type_instance.to_dict()
# create an instance of CampaignType from a dict
campaign_type_form_dict = campaign_type.from_dict(campaign_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


