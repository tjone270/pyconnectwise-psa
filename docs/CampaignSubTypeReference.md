# CampaignSubTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.campaign_sub_type_reference import CampaignSubTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of CampaignSubTypeReference from a JSON string
campaign_sub_type_reference_instance = CampaignSubTypeReference.from_json(json)
# print the JSON string representation of the object
print CampaignSubTypeReference.to_json()

# convert the object into a dict
campaign_sub_type_reference_dict = campaign_sub_type_reference_instance.to_dict()
# create an instance of CampaignSubTypeReference from a dict
campaign_sub_type_reference_form_dict = campaign_sub_type_reference.from_dict(campaign_sub_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


