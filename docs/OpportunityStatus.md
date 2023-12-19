# OpportunityStatus


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**date_entered** | **datetime** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**entered_by** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**lost_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 30; | 
**won_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_status import OpportunityStatus

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityStatus from a JSON string
opportunity_status_instance = OpportunityStatus.from_json(json)
# print the JSON string representation of the object
print OpportunityStatus.to_json()

# convert the object into a dict
opportunity_status_dict = opportunity_status_instance.to_dict()
# create an instance of OpportunityStatus from a dict
opportunity_status_form_dict = opportunity_status.from_dict(opportunity_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


