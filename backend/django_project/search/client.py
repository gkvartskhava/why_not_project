
# # from algoliasearch.search.client import SearchClientSync
# from algoliasearch_django import algolia_engine

# import urllib.parse


# def get_client():
#     return algolia_engine.client


# # def perform_search(query, **kwargs):
# #     client = get_client()
# #     tag_filters = kwargs.pop("tags", None)
# #     facet_filters = [f"{k}:{v}" for k, v in kwargs.items() if v]

# #     raw_params = {
# #         "query": query
# #     }

# #     if tag_filters:
# #         if isinstance(tag_filters, list):
# #             raw_params["tagFilters"] = ",".join(tag_filters)
# #         else:
# #             raw_params["tagFilters"] = tag_filters

# #     if facet_filters:
# #         raw_params["facetFilters"] = facet_filters

# #     # Convert raw_params to URL-encoded string
# #     encoded_params = urllib.parse.urlencode(raw_params, doseq=True)

# #     search_method_params = {
# #         "requests": [
# #             {
# #                 "indexName": "gio_Product",
# #                 "params": encoded_params
# #             }
# #         ]
# #     }

# #     result = client.search(search_method_params)
# #     return result






# def get_index(index_name = 'gio_Product'):
#     client = get_client()
#     index = client.init_index(index_name)
#     return index

# def perform_search(query, **kwargs):
#     client = get_client()
#     tag_filters = kwargs.pop("tags", None)
#     facet_filters = [f"{k}:{v}" for k, v in kwargs.items() if v]

#     raw_params = {
#         "query": query
#     }

#     if tag_filters:
#         if isinstance(tag_filters, list):
#             raw_params["tagFilters"] = ",".join(tag_filters)
#         else:
#             raw_params["tagFilters"] = tag_filters

#     if facet_filters:
#         raw_params["facetFilters"] = facet_filters

#     # Convert raw_params to URL-encoded string
#     encoded_params = urllib.parse.urlencode(raw_params, doseq=True)

#     search_method_params = {
#         "requests": [
#             {
#                 "indexName": "gio_Product",
#                 "params": encoded_params
#             }
#         ]
#     }

#     result = client.search(search_method_params)
#     return result
# #    



# # def perform_search(query, **kwargs):
# #     index = get_index()
# #     results = index.search(query)
# #     return results
