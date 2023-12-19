# RmaDispositionInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.rma_disposition_info import RmaDispositionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RmaDispositionInfo from a JSON string
rma_disposition_info_instance = RmaDispositionInfo.from_json(json)
# print the JSON string representation of the object
print RmaDispositionInfo.to_json()

# convert the object into a dict
rma_disposition_info_dict = rma_disposition_info_instance.to_dict()
# create an instance of RmaDispositionInfo from a dict
rma_disposition_info_form_dict = rma_disposition_info.from_dict(rma_disposition_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


