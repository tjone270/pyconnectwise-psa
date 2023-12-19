# ProjectTemplateWorkPlan


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**budget_amount** | **float** |  | [optional] 
**description** | **str** |  | [optional] 
**display_id** | **str** |  | [optional] 
**i_d** | **int** |  | [optional] 
**is_new_item** | **bool** |  | [optional] 
**is_phase** | **bool** |  | [optional] 
**is_project** | **bool** |  | [optional] 
**is_ticket** | **bool** |  | [optional] 
**parent_phase_rec_id** | **int** |  | [optional] 
**project_name** | **str** |  | [optional] 
**rec_id** | **int** |  | [optional] 
**s_r_service_rec_id** | **int** |  | [optional] 
**tree_id** | **str** |  | [optional] 
**wbs_code** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.project_template_work_plan import ProjectTemplateWorkPlan

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectTemplateWorkPlan from a JSON string
project_template_work_plan_instance = ProjectTemplateWorkPlan.from_json(json)
# print the JSON string representation of the object
print ProjectTemplateWorkPlan.to_json()

# convert the object into a dict
project_template_work_plan_dict = project_template_work_plan_instance.to_dict()
# create an instance of ProjectTemplateWorkPlan from a dict
project_template_work_plan_form_dict = project_template_work_plan.from_dict(project_template_work_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


