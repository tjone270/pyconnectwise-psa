# OpportunityStageInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**color** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**probability** | [**OpportunityProbabilityReference**](OpportunityProbabilityReference.md) |  | [optional] 
**sequence_number** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_stage_info import OpportunityStageInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityStageInfo from a JSON string
opportunity_stage_info_instance = OpportunityStageInfo.from_json(json)
# print the JSON string representation of the object
print OpportunityStageInfo.to_json()

# convert the object into a dict
opportunity_stage_info_dict = opportunity_stage_info_instance.to_dict()
# create an instance of OpportunityStageInfo from a dict
opportunity_stage_info_form_dict = opportunity_stage_info.from_dict(opportunity_stage_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


