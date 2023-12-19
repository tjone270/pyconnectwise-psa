# UnitOfMeasure


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**uom_schedule_xref** | **str** |  Max length: 31; | [optional] 

## Example

```python
from connectwise_psa.models.unit_of_measure import UnitOfMeasure

# TODO update the JSON string below
json = "{}"
# create an instance of UnitOfMeasure from a JSON string
unit_of_measure_instance = UnitOfMeasure.from_json(json)
# print the JSON string representation of the object
print UnitOfMeasure.to_json()

# convert the object into a dict
unit_of_measure_dict = unit_of_measure_instance.to_dict()
# create an instance of UnitOfMeasure from a dict
unit_of_measure_form_dict = unit_of_measure.from_dict(unit_of_measure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


