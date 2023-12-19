# SalesTeamReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.sales_team_reference import SalesTeamReference

# TODO update the JSON string below
json = "{}"
# create an instance of SalesTeamReference from a JSON string
sales_team_reference_instance = SalesTeamReference.from_json(json)
# print the JSON string representation of the object
print SalesTeamReference.to_json()

# convert the object into a dict
sales_team_reference_dict = sales_team_reference_instance.to_dict()
# create an instance of SalesTeamReference from a dict
sales_team_reference_form_dict = sales_team_reference.from_dict(sales_team_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


