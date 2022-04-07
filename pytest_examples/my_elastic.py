from elasticsearch import Elasticsearch

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsIng1dCI6ImpTMVhvMU9XRGpfNTJ2YndHTmd2UU8yVnpNYyIsImtpZCI6ImpTMVhvMU9XRGpfNTJ2YndHTmd2UU8yVnpNYyJ9.eyJhdWQiOiJodHRwczovL3VzZTJzZWFyY2hwb2N1c2VkdGF4aWRtZWxzMDEuc2JwLmV5Y2xpZW50aHViLmNvbSIsImlzcyI6Imh0dHBzOi8vc3RzLndpbmRvd3MubmV0LzViOTczZjk5LTc3ZGYtNGJlYi1iMjdkLWFhMGM3MGI4NDgyYy8iLCJpYXQiOjE2NDkzNTAwODgsIm5iZiI6MTY0OTM1MDA4OCwiZXhwIjoxNjQ5MzUzOTg4LCJhaW8iOiJFMlpnWUVqY3ZzYWlwVVYxd3h3eHJuZS85RjRYQUFBPSIsImFwcGlkIjoiMTU3MTRjOTItNTMwMy00ZjZmLWFlNGQtZGFkNWFmNzY4ZDJmIiwiYXBwaWRhY3IiOiIxIiwiaWRwIjoiaHR0cHM6Ly9zdHMud2luZG93cy5uZXQvNWI5NzNmOTktNzdkZi00YmViLWIyN2QtYWEwYzcwYjg0ODJjLyIsIm9pZCI6ImZhYWUxM2QyLTRmNGItNGNiZC1iOTBhLWJlNTI3M2ExZGE5NiIsInJoIjoiMC5BU0VBbVQtWFc5OTM2MHV5ZmFvTWNMaElMSzNXdHMtQnRNRkJ1SnVBVTZYZ2hIY2hBQUEuIiwic3ViIjoiZmFhZTEzZDItNGY0Yi00Y2JkLWI5MGEtYmU1MjczYTFkYTk2IiwidGlkIjoiNWI5NzNmOTktNzdkZi00YmViLWIyN2QtYWEwYzcwYjg0ODJjIiwidXRpIjoiclRtYW9naUViMEtFNjlDUzZBS0ZBQSIsInZlciI6IjEuMCJ9.OJUS3ANjELc4BJ3eNydREa2xdEw0dgpwBoJRUF0WoVP3_hYsgyrzJ7DFkm8THNMgyHb_A0ZA_iiDmhiv2QSWF4p9zpOyZD2DDZR-Ebk3sKG56PprjjQaysX-5JHnqjeAHU8tJ5PoK1SmSnVLgeooGRsd6KPTQuNY32zsUy3xVtiuSg-sOW_65iSD_AbSEfGQY5cmPspBdrocJQ1QjUeftNd4zzAmQY1gkIzSfDYVBRSLqlzSiQo50_-4ELNT8S5Uz4IYeoa_CfD13tnofQzQnkbS8Fwx4Kq0jAZnfpKpE2En45sUBIT74GrwtM1i-vLLhtQeWy_g7gHiBNq5h2QboQ"


client = Elasticsearch(
    f"https://use2searchdev.sbp.eyclienthub.com:33231",
    headers={"Authorization": "Bearer " + token},
)
# getting time out issue 


# client = Elasticsearch(
#     "https://use2searchdev.sbp.eyclienthub.com",
#     http_auth=("elastic", token),
#     verify_certs=False,
# )

print(client)
# client.info()
index_name ="dwn-test-index2"
email_id = 'test'
body={
    "query": {
        "bool": {"must": {"match_phrase": {"EmailID": email_id}}}
    }
}

client.search(index=index_name, body=body)["hits"]


# from elasticsearch import Urllib3HttpConnection

# class MyUrllib3Http(Urllib3HttpConnection):
#     def __init__(self, *args, **kwargs):
#         internal_params = kwargs.pop("internal_params", {})
#         super(MyUrllib3Http, self).__init__(*args, **kwargs)
#         self.internal_params = internal_params

#     def perform_request(self, method, url, params=None, body=None, timeout=None, ignore=(), headers=None):
#         for param,header in self.internal_params.items():
#           if param in params:
#             headers = {} if headers is None else headers
#             headers[header] = params.pop(param)

#         return super().perform_request(method, url, params=params, body=body, timeout=timeout, ignore=ignore, headers=headers)