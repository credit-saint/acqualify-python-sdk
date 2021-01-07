# coding: utf-8

"""
    Acqualify API Documentation

    The Acqualify API provides services to mortgage brokers and realtors to help applicants qualify for loans.  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: info@creditsaint.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class ApplicantsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def lookup_applicant(self, first_name, last_name, addr_line1, city, state, zip, dob, **kwargs):  # noqa: E501
        """Returns public information about a loan applicant  # noqa: E501

        See publicly available financial info about a loan applicant including credit score, based on name, address and date of birth  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lookup_applicant(first_name, last_name, addr_line1, city, state, zip, dob, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str first_name: Applicant first name (required)
        :param str last_name: Applicant last name (required)
        :param str addr_line1: Address line 1 (required)
        :param str city: City (required)
        :param str state: State (2-letter abbreviation) (required)
        :param int zip: Zip code (required)
        :param str dob: Date of birth (MM/DD/YYYY) (required)
        :param str addr_line2: Address line 2
        :param str email: Applicant email address
        :param str phone_number: Phone number
        :param str loan_amount: Loan amount
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.lookup_applicant_with_http_info(first_name, last_name, addr_line1, city, state, zip, dob, **kwargs)  # noqa: E501
        else:
            (data) = self.lookup_applicant_with_http_info(first_name, last_name, addr_line1, city, state, zip, dob, **kwargs)  # noqa: E501
            return data

    def lookup_applicant_with_http_info(self, first_name, last_name, addr_line1, city, state, zip, dob, **kwargs):  # noqa: E501
        """Returns public information about a loan applicant  # noqa: E501

        See publicly available financial info about a loan applicant including credit score, based on name, address and date of birth  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.lookup_applicant_with_http_info(first_name, last_name, addr_line1, city, state, zip, dob, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str first_name: Applicant first name (required)
        :param str last_name: Applicant last name (required)
        :param str addr_line1: Address line 1 (required)
        :param str city: City (required)
        :param str state: State (2-letter abbreviation) (required)
        :param int zip: Zip code (required)
        :param str dob: Date of birth (MM/DD/YYYY) (required)
        :param str addr_line2: Address line 2
        :param str email: Applicant email address
        :param str phone_number: Phone number
        :param str loan_amount: Loan amount
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['first_name', 'last_name', 'addr_line1', 'city', 'state', 'zip', 'dob', 'addr_line2', 'email', 'phone_number', 'loan_amount']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method lookup_applicant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'first_name' is set
        if ('first_name' not in params or
                params['first_name'] is None):
            raise ValueError("Missing the required parameter `first_name` when calling `lookup_applicant`")  # noqa: E501
        # verify the required parameter 'last_name' is set
        if ('last_name' not in params or
                params['last_name'] is None):
            raise ValueError("Missing the required parameter `last_name` when calling `lookup_applicant`")  # noqa: E501
        # verify the required parameter 'addr_line1' is set
        if ('addr_line1' not in params or
                params['addr_line1'] is None):
            raise ValueError("Missing the required parameter `addr_line1` when calling `lookup_applicant`")  # noqa: E501
        # verify the required parameter 'city' is set
        if ('city' not in params or
                params['city'] is None):
            raise ValueError("Missing the required parameter `city` when calling `lookup_applicant`")  # noqa: E501
        # verify the required parameter 'state' is set
        if ('state' not in params or
                params['state'] is None):
            raise ValueError("Missing the required parameter `state` when calling `lookup_applicant`")  # noqa: E501
        # verify the required parameter 'zip' is set
        if ('zip' not in params or
                params['zip'] is None):
            raise ValueError("Missing the required parameter `zip` when calling `lookup_applicant`")  # noqa: E501
        # verify the required parameter 'dob' is set
        if ('dob' not in params or
                params['dob'] is None):
            raise ValueError("Missing the required parameter `dob` when calling `lookup_applicant`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'first_name' in params:
            query_params.append(('firstName', params['first_name']))  # noqa: E501
        if 'last_name' in params:
            query_params.append(('lastName', params['last_name']))  # noqa: E501
        if 'addr_line1' in params:
            query_params.append(('addrLine1', params['addr_line1']))  # noqa: E501
        if 'addr_line2' in params:
            query_params.append(('addrLine2', params['addr_line2']))  # noqa: E501
        if 'city' in params:
            query_params.append(('city', params['city']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'zip' in params:
            query_params.append(('zip', params['zip']))  # noqa: E501
        if 'dob' in params:
            query_params.append(('dob', params['dob']))  # noqa: E501
        if 'email' in params:
            query_params.append(('email', params['email']))  # noqa: E501
        if 'phone_number' in params:
            query_params.append(('phoneNumber', params['phone_number']))  # noqa: E501
        if 'loan_amount' in params:
            query_params.append(('loanAmount', params['loan_amount']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/xml', 'application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'application/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer_token']  # noqa: E501

        return self.api_client.call_api(
            '/lookup-applicant', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
