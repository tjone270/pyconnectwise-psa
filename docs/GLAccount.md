# GLAccount


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**cogs1** | **str** |  Max length: 255; | [optional] 
**cogs10** | **str** |  Max length: 255; | [optional] 
**cogs2** | **str** |  Max length: 255; | [optional] 
**cogs3** | **str** |  Max length: 255; | [optional] 
**cogs4** | **str** |  Max length: 255; | [optional] 
**cogs5** | **str** |  Max length: 255; | [optional] 
**cogs6** | **str** |  Max length: 255; | [optional] 
**cogs7** | **str** |  Max length: 255; | [optional] 
**cogs8** | **str** |  Max length: 255; | [optional] 
**cogs9** | **str** |  Max length: 255; | [optional] 
**gl_type** | **str** |  | 
**id** | **int** |  | [optional] 
**inventory** | **str** |  Max length: 255; | [optional] 
**mapped_record** | [**MappedRecordReference**](MappedRecordReference.md) |  | 
**mapped_type** | [**MappedTypeReference**](MappedTypeReference.md) |  | 
**product_id** | **str** |  Max length: 255; | [optional] 
**sales_code** | **str** |  Max length: 255; | [optional] 
**segment1** | **str** |  Max length: 255; | [optional] 
**segment10** | **str** |  Max length: 255; | [optional] 
**segment2** | **str** |  Max length: 255; | [optional] 
**segment3** | **str** |  Max length: 255; | [optional] 
**segment4** | **str** |  Max length: 255; | [optional] 
**segment5** | **str** |  Max length: 255; | [optional] 
**segment6** | **str** |  Max length: 255; | [optional] 
**segment7** | **str** |  Max length: 255; | [optional] 
**segment8** | **str** |  Max length: 255; | [optional] 
**segment9** | **str** |  Max length: 255; | [optional] 

## Example

```python
from connectwise_psa.models.gl_account import GLAccount

# TODO update the JSON string below
json = "{}"
# create an instance of GLAccount from a JSON string
gl_account_instance = GLAccount.from_json(json)
# print the JSON string representation of the object
print GLAccount.to_json()

# convert the object into a dict
gl_account_dict = gl_account_instance.to_dict()
# create an instance of GLAccount from a dict
gl_account_form_dict = gl_account.from_dict(gl_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


