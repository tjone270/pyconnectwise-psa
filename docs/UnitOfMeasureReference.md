# UnitOfMeasureReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.unit_of_measure_reference import UnitOfMeasureReference

# TODO update the JSON string below
json = "{}"
# create an instance of UnitOfMeasureReference from a JSON string
unit_of_measure_reference_instance = UnitOfMeasureReference.from_json(json)
# print the JSON string representation of the object
print UnitOfMeasureReference.to_json()

# convert the object into a dict
unit_of_measure_reference_dict = unit_of_measure_reference_instance.to_dict()
# create an instance of UnitOfMeasureReference from a dict
unit_of_measure_reference_form_dict = unit_of_measure_reference.from_dict(unit_of_measure_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


