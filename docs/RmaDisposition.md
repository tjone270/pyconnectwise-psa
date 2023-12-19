# RmaDisposition


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.rma_disposition import RmaDisposition

# TODO update the JSON string below
json = "{}"
# create an instance of RmaDisposition from a JSON string
rma_disposition_instance = RmaDisposition.from_json(json)
# print the JSON string representation of the object
print RmaDisposition.to_json()

# convert the object into a dict
rma_disposition_dict = rma_disposition_instance.to_dict()
# create an instance of RmaDisposition from a dict
rma_disposition_form_dict = rma_disposition.from_dict(rma_disposition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


