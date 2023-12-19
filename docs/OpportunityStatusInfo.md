# OpportunityStatusInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**closed_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_status_info import OpportunityStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityStatusInfo from a JSON string
opportunity_status_info_instance = OpportunityStatusInfo.from_json(json)
# print the JSON string representation of the object
print OpportunityStatusInfo.to_json()

# convert the object into a dict
opportunity_status_info_dict = opportunity_status_info_instance.to_dict()
# create an instance of OpportunityStatusInfo from a dict
opportunity_status_info_form_dict = opportunity_status_info.from_dict(opportunity_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


