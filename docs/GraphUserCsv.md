# GraphUserCsv


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_enabled** | **bool** |  | [optional] 
**address** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**department** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**employee_type** | **str** |  | [optional] 
**first_name** | **str** |  | [optional] 
**id** | **str** |  | [optional] 
**is_matched_contact** | **bool** |  | [optional] 
**job_title** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**mail** | **str** |  | [optional] 
**manage_contact_name** | **str** |  | [optional] 
**manage_contact_rec_id** | **int** |  | [optional] 
**manager** | [**Manager**](Manager.md) |  | [optional] 
**mobile_phone** | **str** |  | [optional] 
**nick_name** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**principal_name** | **str** |  | [optional] 
**proxy_addresses** | **List[str]** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.graph_user_csv import GraphUserCsv

# TODO update the JSON string below
json = "{}"
# create an instance of GraphUserCsv from a JSON string
graph_user_csv_instance = GraphUserCsv.from_json(json)
# print the JSON string representation of the object
print GraphUserCsv.to_json()

# convert the object into a dict
graph_user_csv_dict = graph_user_csv_instance.to_dict()
# create an instance of GraphUserCsv from a dict
graph_user_csv_form_dict = graph_user_csv.from_dict(graph_user_csv_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


