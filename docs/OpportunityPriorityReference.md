# OpportunityPriorityReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_priority_reference import OpportunityPriorityReference

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityPriorityReference from a JSON string
opportunity_priority_reference_instance = OpportunityPriorityReference.from_json(json)
# print the JSON string representation of the object
print OpportunityPriorityReference.to_json()

# convert the object into a dict
opportunity_priority_reference_dict = opportunity_priority_reference_instance.to_dict()
# create an instance of OpportunityPriorityReference from a dict
opportunity_priority_reference_form_dict = opportunity_priority_reference.from_dict(opportunity_priority_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


