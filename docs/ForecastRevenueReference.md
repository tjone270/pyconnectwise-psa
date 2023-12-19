# ForecastRevenueReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**cost** | **float** |  | [optional] 
**id** | **int** |  | [optional] 
**margin** | **float** |  | [optional] 
**percentage** | **float** |  | [optional] 
**revenue** | **float** |  | [optional] 

## Example

```python
from connectwise_psa.models.forecast_revenue_reference import ForecastRevenueReference

# TODO update the JSON string below
json = "{}"
# create an instance of ForecastRevenueReference from a JSON string
forecast_revenue_reference_instance = ForecastRevenueReference.from_json(json)
# print the JSON string representation of the object
print ForecastRevenueReference.to_json()

# convert the object into a dict
forecast_revenue_reference_dict = forecast_revenue_reference_instance.to_dict()
# create an instance of ForecastRevenueReference from a dict
forecast_revenue_reference_form_dict = forecast_revenue_reference.from_dict(forecast_revenue_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


