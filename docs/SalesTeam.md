# SalesTeam


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**sales_team_description** | **str** |  Max length: 50; | 
**sales_team_identifier** | **str** |  Max length: 20; | 
**sales_team_location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.sales_team import SalesTeam

# TODO update the JSON string below
json = "{}"
# create an instance of SalesTeam from a JSON string
sales_team_instance = SalesTeam.from_json(json)
# print the JSON string representation of the object
print SalesTeam.to_json()

# convert the object into a dict
sales_team_dict = sales_team_instance.to_dict()
# create an instance of SalesTeam from a dict
sales_team_form_dict = sales_team.from_dict(sales_team_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


