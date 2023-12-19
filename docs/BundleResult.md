# BundleResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**entities** | [**List[IRestIdentifiedItem]**](IRestIdentifiedItem.md) |  | [optional] 
**error** | [**ErrorResponseMessage**](ErrorResponseMessage.md) |  | [optional] 
**resource_type** | **str** |  | [optional] 
**sequence_number** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 
**success** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.bundle_result import BundleResult

# TODO update the JSON string below
json = "{}"
# create an instance of BundleResult from a JSON string
bundle_result_instance = BundleResult.from_json(json)
# print the JSON string representation of the object
print BundleResult.to_json()

# convert the object into a dict
bundle_result_dict = bundle_result_instance.to_dict()
# create an instance of BundleResult from a dict
bundle_result_form_dict = bundle_result.from_dict(bundle_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


