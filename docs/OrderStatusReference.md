# OrderStatusReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.order_status_reference import OrderStatusReference

# TODO update the JSON string below
json = "{}"
# create an instance of OrderStatusReference from a JSON string
order_status_reference_instance = OrderStatusReference.from_json(json)
# print the JSON string representation of the object
print OrderStatusReference.to_json()

# convert the object into a dict
order_status_reference_dict = order_status_reference_instance.to_dict()
# create an instance of OrderStatusReference from a dict
order_status_reference_form_dict = order_status_reference.from_dict(order_status_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


