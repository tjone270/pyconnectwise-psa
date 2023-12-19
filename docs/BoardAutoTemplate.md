# BoardAutoTemplate


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**auto_apply_flag** | **bool** |  | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**budget_hours_setting** | **str** |  | [optional] 
**discussion_setting** | **str** |  | [optional] 
**documents_setting** | **str** |  | [optional] 
**finance_information_setting** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**impact_urgency_setting** | **str** |  | [optional] 
**internal_analysis_setting** | **str** |  | [optional] 
**item** | [**ServiceItemReference**](ServiceItemReference.md) |  | [optional] 
**resolution_setting** | **str** |  | [optional] 
**resources_setting** | **str** |  | [optional] 
**send_notes_as_email_setting** | **str** |  | [optional] 
**service_template** | [**ServiceTemplateReference**](ServiceTemplateReference.md) |  | [optional] 
**subtype** | [**ServiceSubTypeReference**](ServiceSubTypeReference.md) |  | [optional] 
**summary_setting** | **str** |  | [optional] 
**tasks_setting** | **str** |  | [optional] 
**template_priority_setting** | **str** |  | [optional] 
**type** | [**ServiceTypeReference**](ServiceTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.board_auto_template import BoardAutoTemplate

# TODO update the JSON string below
json = "{}"
# create an instance of BoardAutoTemplate from a JSON string
board_auto_template_instance = BoardAutoTemplate.from_json(json)
# print the JSON string representation of the object
print BoardAutoTemplate.to_json()

# convert the object into a dict
board_auto_template_dict = board_auto_template_instance.to_dict()
# create an instance of BoardAutoTemplate from a dict
board_auto_template_form_dict = board_auto_template.from_dict(board_auto_template_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


