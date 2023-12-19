# Experiment


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**description** | **str** |  | [optional] 
**experiment_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**member_inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 
**properties** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.experiment import Experiment

# TODO update the JSON string below
json = "{}"
# create an instance of Experiment from a JSON string
experiment_instance = Experiment.from_json(json)
# print the JSON string representation of the object
print Experiment.to_json()

# convert the object into a dict
experiment_dict = experiment_instance.to_dict()
# create an instance of Experiment from a dict
experiment_form_dict = experiment.from_dict(experiment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


