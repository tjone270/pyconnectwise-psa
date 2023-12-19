# OpportunityRating


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**sort_order** | **int** |  | [optional] 

## Example

```python
from connectwise_psa.models.opportunity_rating import OpportunityRating

# TODO update the JSON string below
json = "{}"
# create an instance of OpportunityRating from a JSON string
opportunity_rating_instance = OpportunityRating.from_json(json)
# print the JSON string representation of the object
print OpportunityRating.to_json()

# convert the object into a dict
opportunity_rating_dict = opportunity_rating_instance.to_dict()
# create an instance of OpportunityRating from a dict
opportunity_rating_form_dict = opportunity_rating.from_dict(opportunity_rating_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


