# OpportunityTypeInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_type_info import OpportunityTypeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityTypeInfo from a JSON string
opportunity_type_info_instance = OpportunityTypeInfo.from_json(json)
# print the JSON string representation of the object
print OpportunityTypeInfo.to_json()

# convert the object into a dict
opportunity_type_info_dict = opportunity_type_info_instance.to_dict()
# create an instance of OpportunityTypeInfo from a dict
opportunity_type_info_form_dict = opportunity_type_info.from_dict(opportunity_type_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


