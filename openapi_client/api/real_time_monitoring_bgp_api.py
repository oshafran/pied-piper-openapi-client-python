"""
    Cisco SD-WAN vManage API

    The vManage API exposes the functionality of operations maintaining devices and the overlay network  # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: vmanage@cisco.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from openapi_client.api_client import ApiClient, Endpoint as _Endpoint
from openapi_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)


class RealTimeMonitoringBGPApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.create_bgp_neighbors_list_endpoint = _Endpoint(
            settings={
                'response_type': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),
                'auth': [],
                'endpoint_path': '/device/bgp/neighbors',
                'operation_id': 'create_bgp_neighbors_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'device_id',
                    'vpn_id',
                    'peer_addr',
                    '_as',
                ],
                'required': [
                    'device_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'vpn_id',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('vpn_id',): {

                        "0": "0",
                        "512": "512"
                    },
                },
                'openapi_types': {
                    'device_id':
                        (str,),
                    'vpn_id':
                        (str,),
                    'peer_addr':
                        (str,),
                    '_as':
                        (str,),
                },
                'attribute_map': {
                    'device_id': 'deviceId',
                    'vpn_id': 'vpn-id',
                    'peer_addr': 'peer-addr',
                    '_as': 'as',
                },
                'location_map': {
                    'device_id': 'query',
                    'vpn_id': 'query',
                    'peer_addr': 'query',
                    '_as': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.create_bgp_routes_list_endpoint = _Endpoint(
            settings={
                'response_type': ([{str: (bool, date, datetime, dict, float, int, list, str, none_type)}],),
                'auth': [],
                'endpoint_path': '/device/bgp/routes',
                'operation_id': 'create_bgp_routes_list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'device_id',
                    'vpn_id',
                    'prefix',
                    'nexthop',
                ],
                'required': [
                    'device_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'vpn_id',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('vpn_id',): {

                        "0": "0",
                        "512": "512"
                    },
                },
                'openapi_types': {
                    'device_id':
                        (str,),
                    'vpn_id':
                        (str,),
                    'prefix':
                        (str,),
                    'nexthop':
                        (str,),
                },
                'attribute_map': {
                    'device_id': 'deviceId',
                    'vpn_id': 'vpn-id',
                    'prefix': 'prefix',
                    'nexthop': 'nexthop',
                },
                'location_map': {
                    'device_id': 'query',
                    'vpn_id': 'query',
                    'prefix': 'query',
                    'nexthop': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.create_bgp_summary_endpoint = _Endpoint(
            settings={
                'response_type': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),
                'auth': [],
                'endpoint_path': '/device/bgp/summary',
                'operation_id': 'create_bgp_summary',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'device_id',
                ],
                'required': [
                    'device_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'device_id':
                        (str,),
                },
                'attribute_map': {
                    'device_id': 'deviceId',
                },
                'location_map': {
                    'device_id': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def create_bgp_neighbors_list(
        self,
        device_id,
        **kwargs
    ):
        """create_bgp_neighbors_list  # noqa: E501

        Get BGP neighbors list (Real Time)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_bgp_neighbors_list(device_id, async_req=True)
        >>> result = thread.get()

        Args:
            device_id (str): Device Id

        Keyword Args:
            vpn_id (str): VPN Id. [optional]
            peer_addr (str): Peer address. [optional]
            _as (str): AS number. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['device_id'] = \
            device_id
        return self.create_bgp_neighbors_list_endpoint.call_with_http_info(**kwargs)

    def create_bgp_routes_list(
        self,
        device_id,
        **kwargs
    ):
        """create_bgp_routes_list  # noqa: E501

        Get BGP routes list (Real Time)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_bgp_routes_list(device_id, async_req=True)
        >>> result = thread.get()

        Args:
            device_id (str): Device Id

        Keyword Args:
            vpn_id (str): VPN Id. [optional]
            prefix (str): IP prefix. [optional]
            nexthop (str): Next hop. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            [{str: (bool, date, datetime, dict, float, int, list, str, none_type)}]
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['device_id'] = \
            device_id
        return self.create_bgp_routes_list_endpoint.call_with_http_info(**kwargs)

    def create_bgp_summary(
        self,
        device_id,
        **kwargs
    ):
        """create_bgp_summary  # noqa: E501

        Get BGP summary (Real Time)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_bgp_summary(device_id, async_req=True)
        >>> result = thread.get()

        Args:
            device_id (str): Device Id

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            {str: (bool, date, datetime, dict, float, int, list, str, none_type)}
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['device_id'] = \
            device_id
        return self.create_bgp_summary_endpoint.call_with_http_info(**kwargs)

