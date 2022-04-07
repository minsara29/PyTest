pytest -v -> verbose 
pytest -m -> marker 
pytest -k -> pass expression with testname 
pytest -vk "str" ->only run modules/function has str 
pytest -vk "module" ->only run modules/function has module 
pytest -vk "case" --tb=no -> no traceback 
pytest -vk "case or xfail"
pytest -vx -> come out once first fail 
pytest -vx --maxfail=2  -> come out after 2 fails 
pytest -v --collect-only  -> colect the module and function details alone 
pytest -vq -> gerate the report in xml/..

pytest -v --lf -> execute last failed functions 
pytest -v --ff -> execute failed first functions  (ordering)
=========================================
















