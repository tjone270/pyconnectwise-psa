# OpportunityType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  Max length: 50; | 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_type import OpportunityType

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityType from a JSON string
opportunity_type_instance = OpportunityType.from_json(json)
# print the JSON string representation of the object
print OpportunityType.to_json()

# convert the object into a dict
opportunity_type_dict = opportunity_type_instance.to_dict()
# create an instance of OpportunityType from a dict
opportunity_type_form_dict = opportunity_type.from_dict(opportunity_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


