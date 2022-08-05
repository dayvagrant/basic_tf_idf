# basic_tf_idf
Basic method for TF-IDF

You can modify calculation formula.

* example of predata_docs_dict
```
{'this': {'count': 4, 'docs_num': [0, 1, 2, 3]},
 'is': {'count': 4, 'docs_num': [0, 1, 2, 3]},
 'the': {'count': 4, 'docs_num': [0, 1, 2, 3]},
 'first': {'count': 2, 'docs_num': [0, 3]},
 'document': {'count': 4, 'docs_num': [0, 1, 1, 3]},
 'second': {'count': 1, 'docs_num': [1]},
 'and': {'count': 1, 'docs_num': [2]},
 'third': {'count': 1, 'docs_num': [2]},
 'one': {'count': 1, 'docs_num': [2]}}
 ```
 
 * example of result
 ```
 [{'this': 0.0,
  'is': 0.0,
  'the': 0.0,
  'first': 0.06020599913279624,
  'document': 0.0},
 {'this': 0.0,
  'document': 0.0,
  'is': 0.0,
  'the': 0.0,
  'second': 0.10034333188799373},
 {'and': 0.10034333188799373,
  'this': 0.0,
  'is': 0.0,
  'the': 0.0,
  'third': 0.10034333188799373,
  'one': 0.10034333188799373},
 {'is': 0.0,
  'this': 0.0,
  'the': 0.0,
  'first': 0.06020599913279624,
  'document': 0.0}]
  ```
