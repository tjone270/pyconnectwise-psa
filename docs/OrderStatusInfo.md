# OrderStatusInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**inactive_flag** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.order_status_info import OrderStatusInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatusInfo from a JSON string
order_status_info_instance = OrderStatusInfo.from_json(json)
# print the JSON string representation of the object
print OrderStatusInfo.to_json()

# convert the object into a dict
order_status_info_dict = order_status_info_instance.to_dict()
# create an instance of OrderStatusInfo from a dict
order_status_info_form_dict = order_status_info.from_dict(order_status_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


