# Workflow


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**activate_flag** | **bool** | Batches can not be turned on until after the workflow is created and it has atleast one event associated with it | [optional] 
**batch_frequency_unit** | **str** | If not specified, defaults to Minutes. Months is not supported as month length varies | [optional] 
**batch_interval** | **int** |  | [optional] 
**batch_last_ran** | **datetime** |  | [optional] 
**batch_schedule** | **str** | If activateFlag is true, batchSchedule is required | [optional] 
**board** | [**BoardReference**](BoardReference.md) |  | [optional] 
**department** | [**SystemDepartmentReference**](SystemDepartmentReference.md) |  | [optional] 
**id** | **int** |  | [optional] 
**location** | [**SystemLocationReference**](SystemLocationReference.md) |  | [optional] 
**name** | **str** |  Max length: 100; | 
**table_type** | [**WorkflowTableTypeReference**](WorkflowTableTypeReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.workflow import Workflow

# TODO update the JSON string below
json = "{}"
# create an instance of Workflow from a JSON string
workflow_instance = Workflow.from_json(json)
# print the JSON string representation of the object
print Workflow.to_json()

# convert the object into a dict
workflow_dict = workflow_instance.to_dict()
# create an instance of Workflow from a dict
workflow_form_dict = workflow.from_dict(workflow_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


