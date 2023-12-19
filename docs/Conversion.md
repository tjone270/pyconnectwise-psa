# Conversion


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**parent_uom** | [**UnitOfMeasureReference**](UnitOfMeasureReference.md) |  | [optional] 
**quantity** | **float** |  | [optional] 
**uom_type** | [**UnitOfMeasureReference**](UnitOfMeasureReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.conversion import Conversion

# TODO update the JSON string below
json = "{}"
# create an instance of Conversion from a JSON string
conversion_instance = Conversion.from_json(json)
# print the JSON string representation of the object
print Conversion.to_json()

# convert the object into a dict
conversion_dict = conversion_instance.to_dict()
# create an instance of Conversion from a dict
conversion_form_dict = conversion.from_dict(conversion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


