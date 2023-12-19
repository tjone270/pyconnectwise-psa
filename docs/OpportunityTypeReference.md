# OpportunityTypeReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_type_reference import OpportunityTypeReference

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityTypeReference from a JSON string
opportunity_type_reference_instance = OpportunityTypeReference.from_json(json)
# print the JSON string representation of the object
print OpportunityTypeReference.to_json()

# convert the object into a dict
opportunity_type_reference_dict = opportunity_type_reference_instance.to_dict()
# create an instance of OpportunityTypeReference from a dict
opportunity_type_reference_form_dict = opportunity_type_reference.from_dict(opportunity_type_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


