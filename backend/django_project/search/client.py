
from algoliasearch.search.client import SearchClientSync
from algoliasearch_django import algolia_engine


def get_client():
    client = SearchClientSync("UO647ZSSUT", "7d4b34609d91ccbb9a947881d462495b")
    return client

def get_index(index_name='gio_Product'):
    client = SearchClientSync("UO647ZSSUT", "7d4b34609d91ccbb9a947881d462495b")
    index = client.search_single_index(index_name)
    return index



def perform_search(query, **kwargs):
    index = get_index()
    params = {}
    client = get_client()
    tags = ''
    if 'tags' in kwargs:
        tags = kwargs.pop("tags") or []
        if len(tags) != 0:
            params['tagFilters'] = tags
    index_filters = [f"{k}:{v}" for k,v in kwargs.items() if v]
    if len(index_filters) != 0:
        params['facetFilters'] = index_filters
    result = client.search(
    search_method_params={
        "requests": [
            {
                "indexName": "gio_Product",
                "query": query,
               
            },
        ],
    },
)
    return result



# def get_index(index_name = 'gio_Product'):
#     client = get_client()
#     index = client.init_index(index_name)
#     return index

# def perform_search(query, **kwargs):
#     index = get_index()
#     results = index.search(query)
#     return results
