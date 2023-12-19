# FormSubmitted


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**campaign_id** | **int** |  | [optional] 
**contact_id** | **int** |  | 
**date_submitted** | **datetime** |  | [optional] 
**id** | **int** |  | [optional] 
**page_sub_type** | **str** |  | [optional] 
**page_type** | **str** |  | [optional] 
**query_string** | **str** |  | [optional] 
**status** | **str** |  | [optional] 
**topic** | **str** |  | [optional] 
**url** | **str** |  Max length: 2083; | 
**version** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.form_submitted import FormSubmitted

# TODO update the JSON string below
json = "{}"
# create an instance of FormSubmitted from a JSON string
form_submitted_instance = FormSubmitted.from_json(json)
# print the JSON string representation of the object
print FormSubmitted.to_json()

# convert the object into a dict
form_submitted_dict = form_submitted_instance.to_dict()
# create an instance of FormSubmitted from a dict
form_submitted_form_dict = form_submitted.from_dict(form_submitted_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


