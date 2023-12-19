# WorkType


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**accrual_type** | **str** |  | [optional] 
**activity_default_flag** | **bool** |  | [optional] 
**add_all_agreement_exclusions** | **bool** | Used only on create to add the work type to all agreement and agreement type exclusion lists | [optional] 
**bill_time** | **str** |  | 
**cost_multiplier** | **float** |  | [optional] 
**hours_max** | **float** |  | [optional] 
**hours_min** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**integration_x_ref** | **str** |  Max length: 50; | [optional] 
**name** | **str** |  Max length: 50; | 
**overall_default_flag** | **bool** |  | [optional] 
**rate** | **float** |  | 
**rate_type** | **str** |  | 
**round_bill_hours_to** | **float** |  | [optional] 
**utilization_flag** | **bool** |  | [optional] 

## Example

```python
from connectwise_psa.models.work_type import WorkType

# TODO update the JSON string below
json = "{}"
# create an instance of WorkType from a JSON string
work_type_instance = WorkType.from_json(json)
# print the JSON string representation of the object
print WorkType.to_json()

# convert the object into a dict
work_type_dict = work_type_instance.to_dict()
# create an instance of WorkType from a dict
work_type_form_dict = work_type.from_dict(work_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


