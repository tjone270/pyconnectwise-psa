# BulkResult


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**payload** | [**List[ResultInfo]**](ResultInfo.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.bulk_result import BulkResult

# TODO update the JSON string below
json = "{}"
# create an instance of BulkResult from a JSON string
bulk_result_instance = BulkResult.from_json(json)
# print the JSON string representation of the object
print BulkResult.to_json()

# convert the object into a dict
bulk_result_dict = bulk_result_instance.to_dict()
# create an instance of BulkResult from a dict
bulk_result_form_dict = bulk_result.from_dict(bulk_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


