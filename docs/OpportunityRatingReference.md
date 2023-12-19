# OpportunityRatingReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_rating_reference import OpportunityRatingReference

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityRatingReference from a JSON string
opportunity_rating_reference_instance = OpportunityRatingReference.from_json(json)
# print the JSON string representation of the object
print OpportunityRatingReference.to_json()

# convert the object into a dict
opportunity_rating_reference_dict = opportunity_rating_reference_instance.to_dict()
# create an instance of OpportunityRatingReference from a dict
opportunity_rating_reference_form_dict = opportunity_rating_reference.from_dict(opportunity_rating_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


