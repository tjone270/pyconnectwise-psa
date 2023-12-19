# LinkClicked


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** |  | [optional] 
**contact_id** | **int** |  | 
**date_clicked** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**query_string** | **str** |  | [optional] 
**url** | **str** |  Max length: 2083; | 

## Example

```python
from connectwise_psa.models.link_clicked import LinkClicked

# TODO update the JSON string below
json = "{}"
# create an instance of LinkClicked from a JSON string
link_clicked_instance = LinkClicked.from_json(json)
# print the JSON string representation of the object
print LinkClicked.to_json()

# convert the object into a dict
link_clicked_dict = link_clicked_instance.to_dict()
# create an instance of LinkClicked from a dict
link_clicked_form_dict = link_clicked.from_dict(link_clicked_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


