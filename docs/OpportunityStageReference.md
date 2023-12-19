# OpportunityStageReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_stage_reference import OpportunityStageReference

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityStageReference from a JSON string
opportunity_stage_reference_instance = OpportunityStageReference.from_json(json)
# print the JSON string representation of the object
print OpportunityStageReference.to_json()

# convert the object into a dict
opportunity_stage_reference_dict = opportunity_stage_reference_instance.to_dict()
# create an instance of OpportunityStageReference from a dict
opportunity_stage_reference_form_dict = opportunity_stage_reference.from_dict(opportunity_stage_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


