# MileageCalculatorViewModel


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end** | **float** |  | [optional] 
**is_miles** | **bool** |  | [optional] 
**is_odometer** | **bool** |  | [optional] 
**miles** | **float** |  | [optional] 
**start** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.mileage_calculator_view_model import MileageCalculatorViewModel

# TODO update the JSON string below
json = "{}"
# create an instance of MileageCalculatorViewModel from a JSON string
mileage_calculator_view_model_instance = MileageCalculatorViewModel.from_json(json)
# print the JSON string representation of the object
print MileageCalculatorViewModel.to_json()

# convert the object into a dict
mileage_calculator_view_model_dict = mileage_calculator_view_model_instance.to_dict()
# create an instance of MileageCalculatorViewModel from a dict
mileage_calculator_view_model_form_dict = mileage_calculator_view_model.from_dict(mileage_calculator_view_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


