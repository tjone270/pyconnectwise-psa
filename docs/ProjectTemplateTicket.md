# ProjectTemplateTicket


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**bill_separately_flag** | **bool** |  | [optional] 
**budget_hours** | **float** |  | [optional] 
**description** | **str** |  Max length: 100; | 
**duration** | **int** |  | [optional] 
**id** | **int** |  | [optional] 
**internal_analysis** | **str** |  | [optional] 
**line_number** | **float** |  | [optional] 
**mark_as_milestone_flag** | **bool** |  | [optional] 
**notes** | **str** |  | [optional] 
**pm_tmp_project_rec_id** | **int** |  | [optional] 
**priority** | [**PriorityReference**](PriorityReference.md) |  | [optional] 
**project_template_id** | **int** |  | [optional] 
**project_template_phase_id** | **int** |  | [optional] 
**record_type** | **str** |  Max length: 1; | [optional] 
**resolution** | **str** |  | [optional] 
**source** | [**ServiceSourceReference**](ServiceSourceReference.md) |  | [optional] 
**wbs_code** | **str** |  Max length: 50; | [optional] 
**work_role** | [**WorkRoleReference**](WorkRoleReference.md) |  | [optional] 
**work_type** | [**WorkTypeReference**](WorkTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.project_template_ticket import ProjectTemplateTicket

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateTicket from a JSON string
project_template_ticket_instance = ProjectTemplateTicket.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateTicket.to_json()

# convert the object into a dict
project_template_ticket_dict = project_template_ticket_instance.to_dict()
# create an instance of ProjectTemplateTicket from a dict
project_template_ticket_form_dict = project_template_ticket.from_dict(project_template_ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


