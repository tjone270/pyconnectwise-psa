# OpportunityRatingInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_rating_info import OpportunityRatingInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityRatingInfo from a JSON string
opportunity_rating_info_instance = OpportunityRatingInfo.from_json(json)
# print the JSON string representation of the object
print OpportunityRatingInfo.to_json()

# convert the object into a dict
opportunity_rating_info_dict = opportunity_rating_info_instance.to_dict()
# create an instance of OpportunityRatingInfo from a dict
opportunity_rating_info_form_dict = opportunity_rating_info.from_dict(opportunity_rating_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


