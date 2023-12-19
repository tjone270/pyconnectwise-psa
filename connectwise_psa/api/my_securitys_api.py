# coding: utf-8

"""
    ConnectWise PSA

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 2022.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import io
import warnings

from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Dict, List, Optional, Tuple, Union, Any

try:
    from typing import Annotated
except ImportError:
    from typing_extensions import Annotated

from pydantic import StrictInt, StrictStr

from typing import List, Optional

from connectwise_psa.models.my_security import MySecurity

from connectwise_psa.api_client import ApiClient
from connectwise_psa.api_response import ApiResponse
from connectwise_psa.rest import RESTResponseType


class MySecuritysApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_system_my_security(
        self,
        client_id: StrictStr,
        conditions: Optional[StrictStr] = None,
        child_conditions: Optional[StrictStr] = None,
        custom_field_conditions: Optional[StrictStr] = None,
        order_by: Optional[StrictStr] = None,
        fields: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[StrictInt] = None,
        page_id: Optional[StrictInt] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> List[MySecurity]:
        """Get List of MySecurity


        :param client_id:  (required)
        :type client_id: str
        :param conditions: 
        :type conditions: str
        :param child_conditions: 
        :type child_conditions: str
        :param custom_field_conditions: 
        :type custom_field_conditions: str
        :param order_by: 
        :type order_by: str
        :param fields: 
        :type fields: str
        :param page: 
        :type page: int
        :param page_size: 
        :type page_size: int
        :param page_id: 
        :type page_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_system_my_security_serialize(
            client_id=client_id,
            conditions=conditions,
            child_conditions=child_conditions,
            custom_field_conditions=custom_field_conditions,
            order_by=order_by,
            fields=fields,
            page=page,
            page_size=page_size,
            page_id=page_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[MySecurity]"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_system_my_security_with_http_info(
        self,
        client_id: StrictStr,
        conditions: Optional[StrictStr] = None,
        child_conditions: Optional[StrictStr] = None,
        custom_field_conditions: Optional[StrictStr] = None,
        order_by: Optional[StrictStr] = None,
        fields: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[StrictInt] = None,
        page_id: Optional[StrictInt] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[List[MySecurity]]:
        """Get List of MySecurity


        :param client_id:  (required)
        :type client_id: str
        :param conditions: 
        :type conditions: str
        :param child_conditions: 
        :type child_conditions: str
        :param custom_field_conditions: 
        :type custom_field_conditions: str
        :param order_by: 
        :type order_by: str
        :param fields: 
        :type fields: str
        :param page: 
        :type page: int
        :param page_size: 
        :type page_size: int
        :param page_id: 
        :type page_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_system_my_security_serialize(
            client_id=client_id,
            conditions=conditions,
            child_conditions=child_conditions,
            custom_field_conditions=custom_field_conditions,
            order_by=order_by,
            fields=fields,
            page=page,
            page_size=page_size,
            page_id=page_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[MySecurity]"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_system_my_security_without_preload_content(
        self,
        client_id: StrictStr,
        conditions: Optional[StrictStr] = None,
        child_conditions: Optional[StrictStr] = None,
        custom_field_conditions: Optional[StrictStr] = None,
        order_by: Optional[StrictStr] = None,
        fields: Optional[StrictStr] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[StrictInt] = None,
        page_id: Optional[StrictInt] = None,
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Get List of MySecurity


        :param client_id:  (required)
        :type client_id: str
        :param conditions: 
        :type conditions: str
        :param child_conditions: 
        :type child_conditions: str
        :param custom_field_conditions: 
        :type custom_field_conditions: str
        :param order_by: 
        :type order_by: str
        :param fields: 
        :type fields: str
        :param page: 
        :type page: int
        :param page_size: 
        :type page_size: int
        :param page_id: 
        :type page_id: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_system_my_security_serialize(
            client_id=client_id,
            conditions=conditions,
            child_conditions=child_conditions,
            custom_field_conditions=custom_field_conditions,
            order_by=order_by,
            fields=fields,
            page=page,
            page_size=page_size,
            page_id=page_id,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "List[MySecurity]"
            
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_system_my_security_serialize(
        self,
        client_id,
        conditions,
        child_conditions,
        custom_field_conditions,
        order_by,
        fields,
        page,
        page_size,
        page_id,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> Tuple:

        _host = None

        _collection_formats: Dict[str, str] = {
            
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if conditions is not None:
            
            _query_params.append(('conditions', conditions))
            
        if child_conditions is not None:
            
            _query_params.append(('childConditions', child_conditions))
            
        if custom_field_conditions is not None:
            
            _query_params.append(('customFieldConditions', custom_field_conditions))
            
        if order_by is not None:
            
            _query_params.append(('orderBy', order_by))
            
        if fields is not None:
            
            _query_params.append(('fields', fields))
            
        if page is not None:
            
            _query_params.append(('page', page))
            
        if page_size is not None:
            
            _query_params.append(('pageSize', page_size))
            
        if page_id is not None:
            
            _query_params.append(('pageId', page_id))
            
        # process the header parameters
        if client_id is not None:
            _header_params['clientId'] = client_id
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'application/vnd.connectwise.com+json; version=2022.2'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/system/mySecurity',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


